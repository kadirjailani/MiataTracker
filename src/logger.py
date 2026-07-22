"""Logging utilities for MiataTracker."""

from __future__ import annotations

import logging


def get_logger(name: str = "MiataTracker", level_name: str = "INFO") -> logging.Logger:
    """Return a console logger, configuring its handler only once."""
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level_name.upper(), logging.INFO))

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("%(asctime)s [%(levelname)-8s] %(name)s: %(message)s")
        )
        logger.addHandler(handler)

    return logger
