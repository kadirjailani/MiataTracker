"""Domain model definitions for MiataTracker."""

from dataclasses import dataclass
from datetime import date


@dataclass
class CarListing:
    """Represents a used Mazda MX-5 listing collected from websites."""

    title: str
    price: float
    year: int
    mileage: int
    transmission: str
    location: str
    url: str
    listing_date: date | None = None
