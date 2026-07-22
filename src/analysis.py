"""Market statistics for collected MX-5 listings."""

from __future__ import annotations

from statistics import mean, median

from models import CarListing


def market_stats(listings: list[CarListing]) -> dict[str, float | int]:
    """Calculate basic market statistics from the collected listings."""
    if not listings:
        raise ValueError("No listings to analyze.")
    prices = [listing.price for listing in listings]
    return {
        "count": len(listings),
        "price_min": min(prices),
        "price_max": max(prices),
        "price_mean": round(mean(prices), 2),
        "price_median": round(median(prices), 2),
        "mileage_mean": round(mean(listing.mileage for listing in listings)),
        "year_mean": round(mean(listing.year for listing in listings), 1),
    }
