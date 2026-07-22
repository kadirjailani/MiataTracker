"""Configuration for MiataTracker."""

from __future__ import annotations

import os

DEFAULTS: dict[str, str] = {
    "SCRAPER_URLS": "",
    "LOG_LEVEL": "INFO",
    "DATA_DIR": "data",
}


def get_config() -> dict[str, str]:
    """Return configuration defaults, overridden by environment variables when set."""
    return {key: os.getenv(key, default) for key, default in DEFAULTS.items()}
