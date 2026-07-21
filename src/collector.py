"""Listing collection for MiataTracker.

Parses carlist.my and mudah.my listing pages that the user saved manually
while browsing (File > Save Page As). Live fetching is kept for pages that
allow it.
"""

from __future__ import annotations

import json
import re
from datetime import date, datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup

from logger import get_logger
from models import CarListing

USER_AGENT = 'MiataTracker/0.1 (personal market research)'
REQUEST_TIMEOUT = 20

log = get_logger(__name__)


def fetch_html(url: str) -> str:
    """Download a listing page and return its HTML.

    Raises requests.HTTPError on non-success status codes.
    """
    response = requests.get(
        url, headers={'User-Agent': USER_AGENT}, timeout=REQUEST_TIMEOUT
    )
    response.raise_for_status()
    return response.text


def collect_saved_pages(pages_dir: str | Path) -> list[CarListing]:
    """Parse all saved carlist.my pages in a directory, skipping bad files."""
    pages_dir = Path(pages_dir)
    if not pages_dir.exists():
        return []
    listings: list[CarListing] = []
    for path in sorted(pages_dir.glob('*.htm*')):
        listing = parse_saved_page(path)
        if listing is not None:
            listings.append(listing)
    return listings


def parse_saved_page(path: str | Path) -> CarListing | None:
    """Parse one saved carlist.my listing detail page into a CarListing.

    Returns None (with a warning) when required fields are missing, so one
    bad file never stops a collection run.
    """
    path = Path(path)
    try:
        html = path.read_text(encoding='utf-8', errors='replace')
        listing = _parse_listing_html(html)
        # Saved pages carry no reliable posted date; the save date is when
        # this price was observed, which is what the forecast needs.
        listing.listing_date = _file_saved_date(path)
        return listing
    except (KeyError, ValueError, TypeError, AttributeError) as exc:
        log.warning('Skipping %s: %s', path.name, exc)
        return None


def _parse_listing_html(html: str) -> CarListing:
    """Extract listing fields from a saved page, dispatching on the site."""
    soup = BeautifulSoup(html, 'lxml')
    next_data = soup.find('script', id='__NEXT_DATA__')
    if next_data is not None and next_data.string:
        return _parse_mudah(json.loads(next_data.string))
    car = _json_ld_car(soup)
    price_tag = soup.find('meta', attrs={'itemprop': 'price'})
    if price_tag is None:
        raise ValueError('price meta tag not found')
    transmission_tag = soup.find('meta', attrs={'name': 'WT.z_transmission'})
    return CarListing(
        title=str(car['name']).strip(),
        price=float(price_tag['content']),
        year=int(car['vehicleModelDate']),
        mileage=int(car['mileageFromOdometer']['value']),
        transmission=transmission_tag['content'].strip() if transmission_tag else '',
        location=_location(html),
        url=str(car['url']).strip(),
    )


def _parse_mudah(next_data: dict) -> CarListing:
    """Extract listing fields from mudah.my's __NEXT_DATA__ JSON."""
    ads = next_data['props']['initialState']['adDetails']['byID']
    attrs = next(iter(ads.values()))['attributes']
    params = {p['id']: p['value'] for p in attrs['categoryParams']}
    # mudah gives mileage as a bucket like "25 000 - 29 999"; use the midpoint
    bounds = [int(n.replace(' ', '')) for n in params.get('mileage', '').split('-') if n.strip()]
    mileage = sum(bounds) // len(bounds) if bounds else 0
    return CarListing(
        title=attrs['subject'].strip(),
        price=float(attrs['carForSalePrice']),
        year=int(params['manufactured_date']),
        mileage=mileage,
        transmission=params.get('transmission', ''),
        location=f"{attrs['subregionName']}, {attrs['regionName']}",
        url=attrs['adviewUrl'].strip(),
    )


def _json_ld_car(soup: BeautifulSoup) -> dict:
    """Return the schema.org Car object from the page's JSON-LD script."""
    tag = soup.find('script', type='application/ld+json')
    if tag is None or not tag.string:
        raise ValueError('JSON-LD script not found')
    data = json.loads(tag.string)
    items = data if isinstance(data, list) else [data]
    for item in items:
        if item.get('@type') == 'Car':
            return item
    raise ValueError('no Car object in JSON-LD')


def _location(html: str) -> str:
    """Extract 'City, Region' from address data embedded in page JSON."""
    locality = re.search(r'"addressLocality"\s*:\s*"([^"]+)"', html)
    region = re.search(r'"addressRegion"\s*:\s*"([^"]+)"', html)
    parts = [match.group(1) for match in (locality, region) if match]
    return ', '.join(parts)


def _file_saved_date(path: Path) -> date:
    """Date the page was saved, from the file's modification time."""
    return datetime.fromtimestamp(path.stat().st_mtime).date()
