# Web Scraping Guide

## Purpose

Collect used Mazda MX-5 listings accurately, respectfully, and reliably.

## Libraries

- requests
- BeautifulSoup4
- lxml

Do not introduce additional scraping libraries unless requested.

## Workflow

1. Download HTML using requests.
2. Validate the HTTP response.
3. Parse HTML using BeautifulSoup.
4. Extract only the required information.
5. Normalize the extracted data.
6. Return structured data.
7. Store data using storage.py.

## Data Collection

Collect only data required for analysis.

Typical fields include:
- Title
- Price
- Year
- Mileage
- Transmission
- Location
- URL
- Listing date

Do not invent missing values.

## HTML Parsing

- Prefer CSS selectors.
- Avoid brittle selectors.
- Handle missing elements safely.
- Strip unnecessary whitespace.
- Normalize extracted text.

## Selector Strategy

Prefer selectors based on:

1. Stable element IDs
2. Semantic class names
3. HTML attributes
4. Text content only as a last resort

Avoid deeply nested CSS selectors unless absolutely necessary.

## HTTP Requests

- Set a descriptive User-Agent.
- Use reasonable request timeouts.
- Handle redirects.
- Retry only when appropriate.
- Handle HTTP errors gracefully.

## Data Validation

Validate:

- Price
- Year
- Mileage
- URL

Skip invalid listings instead of crashing.

## Error Handling

- Catch expected exceptions.
- Log useful error messages.
- Continue processing remaining listings whenever possible.

## Performance

- Minimize HTTP requests.
- Avoid duplicate downloads.
- Parse HTML only once per page.

## Ethics

Respect website Terms of Service.

Do not bypass protections.

Do not perform excessive requests.

## Project Rules

Never:

- scrape unnecessary information
- invent listing values
- hardcode HTML positions
- assume every page has identical structure

Always write maintainable and resilient scrapers.
