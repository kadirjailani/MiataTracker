"""MiataTracker main entry point."""

from __future__ import annotations

from pathlib import Path

import analysis
import collector
import forecast
import report
import storage
from config import get_config
from logger import get_logger


def main() -> None:
    """Run the full workflow: load listings, analyze, forecast, report."""
    print('=' * 68)
    print('      MiataTracker')
    print('   Find, Track & Manage Your Mazda MX-5 Prices Everywhere.')
    print('=' * 68)

    config = get_config()
    log = get_logger(level_name=config['LOG_LEVEL'])
    data_dir = Path(config['DATA_DIR'])
    listings_path = data_dir / 'listings.csv'

    listings = storage.load_listings(listings_path)

    collected = collector.collect_saved_pages(data_dir / 'pages')
    stored_keys = {(listing.url, listing.listing_date) for listing in listings}
    new_listings = [
        listing for listing in collected
        if (listing.url, listing.listing_date) not in stored_keys
    ]
    if new_listings:
        storage.save_listings(new_listings, listings_path)
        listings += new_listings
        log.info('Collected %d new listings from saved pages.', len(new_listings))

    if not listings:
        log.warning('No listings found in %s. Collect or add data first.', listings_path)
        return
    log.info('Working with %d listings from %s.', len(listings), listings_path)

    stats = analysis.market_stats(listings)
    log.info('Market statistics calculated.')

    prediction = None
    chart_path = None
    try:
        prediction = forecast.forecast_prices(listings)
        chart_path = str(data_dir / 'forecast.png')
        forecast.save_forecast_chart(forecast.prepare_history(listings), prediction, chart_path)
        log.info('Forecast generated, chart saved to %s.', chart_path)
    except ValueError as exc:
        log.warning('Forecast skipped: %s', exc)

    ai_analysis = report.generate_ai_analysis(stats, prediction)
    content = report.build_report(stats, prediction, ai_analysis, chart_path)
    report_path = data_dir / 'report.md'
    report.write_report(content, report_path)
    log.info('Report written to %s.', report_path)


if __name__ == '__main__':
    main()
