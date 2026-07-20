# Code Review Guide

## Purpose

Review code for correctness, simplicity, maintainability, and adherence to project standards.

The goal is to improve existing code, not rewrite it unnecessarily.

## Review Process

For every review:

1. Verify correctness.
2. Check readability.
3. Check maintainability.
4. Check project consistency.
5. Suggest the smallest improvement possible.

## Correctness

Verify:

- Logic is correct.
- Edge cases are handled.
- Inputs are validated.
- Exceptions are handled appropriately.

## Python Standards

Check:

- PEP 8 compliance.
- Type hints.
- Function size.
- Naming consistency.
- Import order.
- Module organization.

## Simplicity

Prefer:

- Simple code.
- Small functions.
- Clear variable names.
- Reusable logic.

Avoid:

- Clever code.
- Premature optimization.
- Unnecessary abstractions.

## Performance

Check for:

- Duplicate work.
- Inefficient loops.
- Unnecessary object creation.
- Expensive operations inside loops.

Recommend optimization only when it improves clarity or performance significantly.

## Project Consistency

Verify that code follows:

- project.md
- python.md
- scraping.md
- forecasting.md
- reporting.md

## Documentation

Check:

- Module docstrings.
- Function docstrings.
- Meaningful comments.

Comments should explain why, not what.

## Testing

Ensure code is testable.

Avoid hidden dependencies and side effects.

## Review Output

Organize findings into:

### Strengths

### Issues

### Recommendations

Provide concise explanations.

Do not rewrite entire modules unless requested.

## Project Rules

Never:

- invent requirements
- redesign working code
- introduce new dependencies
- expand project scope

Recommend only improvements relevant to the current implementation.
