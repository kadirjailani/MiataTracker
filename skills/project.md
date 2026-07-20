# MiataTracker Development Guide

## Mission
Build a local Python application that tracks the used Mazda MX-5 market by collecting listings, storing historical data, analyzing pricing trends, forecasting future prices, and generating AI-assisted reports.

## Technology Stack
- Python 3.12
- pandas
- requests
- BeautifulSoup4
- Prophet
- matplotlib
- Ollama (Qwen)
- CSV storage
- Git

## Coding Principles
- Keep the solution simple.
- Avoid unnecessary abstractions.
- Prefer readability over cleverness.
- Write modular code.
- Keep functions small and focused.
- Add type hints where appropriate.
- Follow PEP 8.

## Project Rules
- Never invent features.
- Never invent files.
- Never invent CLI commands.
- Never change project scope.
- Only implement what is requested.
- Preserve existing project structure.

## Development Workflow

Before implementing any task:

1. Understand the requested change.
2. Review existing project files.
3. Reuse existing code whenever possible.
4. Keep changes minimal.
5. Avoid introducing new dependencies unless requested.
6. Preserve backwards compatibility.
7. Verify that the implementation matches the project scope.

## Decision Priority

When making implementation decisions, follow this order:

1. Project requirements
2. Existing project architecture
3. Simplicity
4. Readability
5. Performance
6. Extensibility

Never sacrifice simplicity for premature optimization.

## Anti-Patterns

Never:

- Assume requirements.
- Add frameworks.
- Add databases.
- Add authentication.
- Add APIs.
- Add configuration files unless requested.
- Rename existing modules.
- Replace working code without reason.

## Documentation Rules
- README reflects only implemented functionality.
- Planned work belongs in roadmap documentation.
- Do not document unfinished features as complete.

## Response Rules
- Explain decisions briefly.
- Generate production-quality code.
- Avoid placeholder implementations.
- If information is missing, ask instead of guessing.
