"""Markdown report generation for MiataTracker."""

from __future__ import annotations

from datetime import date
from pathlib import Path

import pandas as pd
import requests

from logger import get_logger

OLLAMA_URL = 'http://localhost:11434/api/generate'
OLLAMA_MODEL = 'qwen3.5:9b'
OLLAMA_TIMEOUT = 120

log = get_logger(__name__)


def generate_ai_analysis(stats: dict[str, float | int], prediction: pd.DataFrame | None) -> str:
    """Ask the local Ollama Qwen model for a short market commentary.

    Returns a fallback message when Ollama is unreachable so the report
    can still be generated.
    """
    prompt = (
        'You are analyzing the used Mazda MX-5 market. '
        'Write a short, objective commentary (max 150 words) covering market trend, '
        'price movement, and forecast outlook. Base it only on this data.\n'
        f'Market statistics: {stats}\n'
        f'Forecast (last rows): {_forecast_tail(prediction)}'
    )
    try:
        response = requests.post(
            OLLAMA_URL,
            json={'model': OLLAMA_MODEL, 'prompt': prompt, 'stream': False, 'think': False, 'options': {'num_predict': 180, 'temperature': 0.3}},
            timeout=OLLAMA_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()['response'].strip()
    except (requests.RequestException, KeyError, ValueError) as exc:
        log.warning('AI analysis unavailable: %s', exc)
        return '_AI analysis unavailable (Ollama not reachable)._'


def build_report(
    stats: dict[str, float | int],
    prediction: pd.DataFrame | None,
    ai_analysis: str,
    chart_path: str | None = None,
) -> str:
    """Assemble the Markdown report from statistics, forecast, and AI commentary."""
    lines = [
        '# Mazda MX-5 Market Report',
        '',
        f'Report date: {date.today().isoformat()}',
        '',
        '## Executive Summary',
        '',
        f'This report covers {stats["count"]} collected listings with a median price '
        f'of {stats["price_median"]:,.2f}. Statistics are calculated from stored data; '
        'forecast values are model estimates, not certainties.',
        '',
        '## Market Statistics',
        '',
        '| Metric | Value |',
        '|--------|-------|',
        f'| Listings | {stats["count"]} |',
        f'| Minimum price | {stats["price_min"]:,.2f} |',
        f'| Maximum price | {stats["price_max"]:,.2f} |',
        f'| Mean price | {stats["price_mean"]:,.2f} |',
        f'| Median price | {stats["price_median"]:,.2f} |',
        f'| Mean mileage | {stats["mileage_mean"]:,} |',
        f'| Mean year | {stats["year_mean"]} |',
        '',
        '## Forecast Summary',
        '',
    ]
    lines += _forecast_section(prediction, chart_path)
    lines += [
        '',
        '## AI Analysis',
        '',
        '_AI-generated commentary — verify against the statistics above._',
        '',
        ai_analysis,
        '',
        '## Conclusion',
        '',
        f'Statistics are historical facts from {stats["count"]} listings. '
        'Forecasts carry uncertainty and should be read together with their '
        'confidence interval.',
        '',
    ]
    return '\n'.join(lines)


def write_report(content: str, path: str | Path) -> None:
    """Write the report content to a Markdown file."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')


def _forecast_section(prediction: pd.DataFrame | None, chart_path: str | None) -> list[str]:
    """Build the forecast summary lines, handling the no-forecast case."""
    if prediction is None or prediction.empty:
        return ['Forecast unavailable: not enough dated listings to train a model.']
    last = prediction.iloc[-1]
    lines = [
        f'Forecast (estimate) for {last["ds"].date().isoformat()}: '
        f'{last["yhat"]:,.2f} '
        f'(confidence interval {last["yhat_lower"]:,.2f} – {last["yhat_upper"]:,.2f}).',
    ]
    if chart_path:
        lines += ['', f'Chart: `{chart_path}`']
    return lines


def _forecast_tail(prediction: pd.DataFrame | None) -> str:
    """Compact string of the last forecast rows for the AI prompt."""
    if prediction is None or prediction.empty:
        return 'no forecast available'
    tail = prediction.tail(5).copy()
    tail['ds'] = tail['ds'].dt.date
    return tail.round(2).to_string(index=False)
