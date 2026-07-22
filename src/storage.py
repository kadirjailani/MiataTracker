"""CSV storage for MiataTracker listings."""

from __future__ import annotations

import csv
from dataclasses import asdict, fields
from datetime import date
from pathlib import Path

from logger import get_logger
from models import CarListing

FIELD_NAMES = [field.name for field in fields(CarListing)]

log = get_logger(__name__)


def save_listings(listings: list[CarListing], path: str | Path) -> None:
    """Append listings to a CSV file, writing the header if the file is new."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    write_header = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)
        if write_header:
            writer.writeheader()
        for listing in listings:
            row = asdict(listing)
            row["listing_date"] = (
                listing.listing_date.isoformat() if listing.listing_date else ""
            )
            writer.writerow(row)


def load_listings(path: str | Path) -> list[CarListing]:
    """Load listings from a CSV file, skipping rows that fail to parse."""
    path = Path(path)
    if not path.exists():
        return []
    listings: list[CarListing] = []
    with path.open(newline="", encoding="utf-8") as file:
        for line_number, row in enumerate(csv.DictReader(file), start=2):
            try:
                listings.append(_row_to_listing(row))
            except (KeyError, ValueError) as exc:
                log.warning("Skipping invalid row %d in %s: %s", line_number, path, exc)
    return listings


def _row_to_listing(row: dict[str, str]) -> CarListing:
    """Convert a CSV row into a CarListing, raising ValueError on bad data."""
    return CarListing(
        title=row["title"],
        price=float(row["price"]),
        year=int(row["year"]),
        mileage=int(row["mileage"]),
        transmission=row["transmission"],
        location=row["location"],
        url=row["url"],
        listing_date=(
            date.fromisoformat(row["listing_date"]) if row["listing_date"] else None
        ),
    )
