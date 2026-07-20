# Architecture Documentation - MiataTracker

## Purpose

This document describes the architectural design and component organization of the MiataTracker application. The system is designed to collect used Mazda MX-5 listings from websites, analyze market data, forecast prices using Prophet, and generate Markdown reports.

The architecture follows clean principles with clear separation between data collection, storage, analysis, forecasting, reporting, and orchestration layers. This design enables easy extension while maintaining code quality.

## High-level workflow

1. **Data Collection** - Listing HTML is downloaded from websites
2. **Storage Layer** - Listings are stored in CSV format
3. **Analysis Engine** - Market statistics are calculated from collected data
4. **Forecasting Module** - Prophet models forecast vehicle prices
5. **Reporting System** - Analysis results and forecasts are formatted into Markdown reports

## Planned modules

### collector.py
Handles listing ingestion:
- Downloads listing HTML pages
- Extracts listing data using parsing techniques

### storage.py
Manages persistent data operations:
- Stores listings in CSV format
- Handles file I/O for list management

### forecast.py
Implements price forecasting capabilities:
- Uses Prophet to forecast prices based on historical market data

### analysis.py
Provides analytical processing functions:
- Calculates market statistics from collected listings

### report.py
Generates output documents:
- Creates Markdown reports with analysis and forecasts

### main.py
Application entry point responsible for:
- Coordinating the workflow between all components
