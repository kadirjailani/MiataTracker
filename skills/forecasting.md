# Forecasting Guide

## Purpose

Forecast used Mazda MX-5 market prices using historical listing data.

## Library

- Prophet

Do not introduce alternative forecasting libraries unless requested.

## Data Requirements

Forecasts require historical data.

Minimum fields:

- Date
- Price

Additional fields may be analyzed separately but should not replace the primary forecasting model.

## Workflow

1. Load historical CSV data.
2. Validate required fields.
3. Clean invalid records.
4. Prepare Prophet dataset.
5. Train the forecasting model.
6. Generate future predictions.
7. Return structured forecast results.

## Data Preparation

- Remove duplicate records.
- Ignore invalid prices.
- Normalize dates.
- Keep historical data unchanged.
- Never modify the original dataset.

## Forecasting Principles

- Prefer simple Prophet models.
- Avoid unnecessary parameter tuning.
- Use default Prophet settings unless requested.
- Document assumptions.

## Validation

Always verify:

- Sufficient historical records.
- Valid dates.
- Numeric prices.
- Missing values.

Stop gracefully if data quality is insufficient.

## Visualization

Generate simple matplotlib charts.

Include:

- Historical prices
- Forecast
- Confidence interval

Avoid unnecessary styling.

## Project Rules

Never:

- invent historical data
- fill missing prices
- overfit the model
- manipulate forecast results

Always report uncertainty honestly.
