# Testing Standards — Universal Principles

## The Test Pyramid
- **Unit tests** (70%): Fast, isolated, test single functions/methods
- **Integration tests** (20%): Test module interactions, DB queries, API calls
- **E2E tests** (10%): Test critical user journeys through the full stack

## What to Test
- Business logic (calculations, transformations, decisions)
- Edge cases (empty inputs, boundary values, error conditions)
- Integration points (API calls, DB queries, external services)
- Auth/authz paths (who can access what)

## What NOT to Test
- Framework internals (React rendering, Express routing)
- Third-party library behaviour
- Trivial getters/setters
- Implementation details (test behaviour, not how it's done)

## Test Structure (AAA Pattern)
- **Arrange**: Set up test data and preconditions
- **Act**: Execute the code under test
- **Assert**: Verify the expected outcome

## Test Quality Rules
- Each test tests ONE thing (single assertion focus)
- Tests are independent (no shared mutable state, no execution order dependency)
- Tests are self-cleaning (create and destroy their own data)
- No hard waits (use polling/retry for async, not sleep)
- No flaky tests (if a test is flaky, fix it or delete it)
- Assertions in the test, not in helpers (explicit over implicit)

## Coverage Philosophy
- Coverage is a metric, not a goal
- 80% coverage threshold means: the remaining 20% should be trivial code
- Missing coverage on complex logic is a bug
- 100% coverage on trivial code is waste

## Mocking Strategy
- Mock external services (APIs, email, payment)
- Mock at the boundary (repository interface, HTTP client)
- Do NOT mock the database in integration tests (use test database)
- Do NOT mock the code under test
