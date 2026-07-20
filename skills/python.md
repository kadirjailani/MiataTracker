# Python Development Guide

## Purpose

Generate production-quality Python code that is simple, readable, maintainable, and suitable for long-term development.

## Python Version

Python 3.12

## Coding Style

- Follow PEP 8.
- Use descriptive variable and function names.
- Keep functions under 40 lines whenever practical.
- Prefer composition over inheritance.
- Prefer explicit code over clever code.
- Avoid unnecessary abstractions.
- Keep modules focused on a single responsibility.

## Type Hints

- Use type hints for all public functions.
- Use dataclasses for data models.
- Prefer built-in types (list, dict, tuple).
- Avoid Any unless absolutely necessary.

## Error Handling

- Raise meaningful exceptions.
- Never silently ignore errors.
- Validate inputs early.
- Keep exception handling specific.

## Documentation

- Every module starts with a short module docstring.
- Every public function has a concise docstring.
- Comments explain why, not what.

## Imports

Import order:

1. Standard library
2. Third-party libraries
3. Local project modules

Remove unused imports.

## File Organization

Recommended order:

- Module docstring
- Imports
- Constants
- Dataclasses
- Helper functions
- Main functions

## Logging

- Use the logging module.
- Do not use print() for application logging.
- Use print() only for CLI output when appropriate.

## Performance

- Write readable code first.
- Optimize only when profiling indicates a bottleneck.
- Avoid premature optimization.

## Testing

Write code that is easy to unit test.

Avoid hidden side effects.

## Project Rules

Never:
- invent requirements
- invent files
- invent APIs
- invent dependencies
- over-engineer the solution

Implement only the requested functionality.

If requirements are unclear, ask for clarification instead of guessing.
