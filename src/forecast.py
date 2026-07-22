"""Price forecasting with Prophet."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
from prophet import Prophet

from models import CarListing

MIN_RECORDS = 10
MIN_DISTINCT_DATES = 5


def prepare_history(listings: list[CarListing]) -> pd.DataFrame:
    """Build a Prophet-ready DataFrame (ds, y) from dated, valid-priced listings."""
    rows = [
        {"ds": pd.Timestamp(listing.listing_date), "y": listing.price}
        for listing in listings
        if listing.listing_date is not None and listing.price > 0
    ]
    if not rows:
        return pd.DataFrame(columns=["ds", "y"])
    return pd.DataFrame(rows).drop_duplicates().sort_values("ds").reset_index(drop=True)


def forecast_prices(listings: list[CarListing], periods: int = 30) -> pd.DataFrame:
    """Forecast prices for the coming days using a default Prophet model.

    Raises ValueError when there is not enough dated history to model.
    """
    history = prepare_history(listings)
    if len(history) < MIN_RECORDS:
        raise ValueError(
            f"Need at least {MIN_RECORDS} dated listings to forecast, got {len(history)}."
        )
    distinct_dates = history["ds"].nunique()
    if distinct_dates < MIN_DISTINCT_DATES:
        raise ValueError(
            f"Need listings from at least {MIN_DISTINCT_DATES} different dates "
            f"to forecast a trend, got {distinct_dates}."
        )
    model = Prophet()
    model.fit(history)
    future = model.make_future_dataframe(periods=periods)
    prediction = model.predict(future)
    return prediction[["ds", "yhat", "yhat_lower", "yhat_upper"]]


def save_forecast_chart(
    history: pd.DataFrame, prediction: pd.DataFrame, path: str | Path
) -> None:
    """Save a chart of historical prices, forecast, and confidence interval."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    figure, axes = plt.subplots(figsize=(10, 6))
    axes.scatter(
        history["ds"], history["y"], s=12, color="black", label="Historical prices"
    )
    axes.plot(prediction["ds"], prediction["yhat"], color="tab:blue", label="Forecast")
    axes.fill_between(
        prediction["ds"],
        prediction["yhat_lower"],
        prediction["yhat_upper"],
        color="tab:blue",
        alpha=0.2,
        label="Confidence interval",
    )
    axes.set_xlabel("Date")
    axes.set_ylabel("Price")
    axes.set_title("Mazda MX-5 price forecast")
    axes.legend()
    figure.autofmt_xdate()
    figure.savefig(path, dpi=100, bbox_inches="tight")
    plt.close(figure)
