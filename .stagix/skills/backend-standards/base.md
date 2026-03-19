# Backend Standards — Universal Principles

These principles apply regardless of language or framework.

## SOLID Principles
- Single Responsibility: Each module/class has one reason to change
- Open/Closed: Open for extension, closed for modification
- Liskov Substitution: Subtypes must be substitutable for their base types
- Interface Segregation: Many specific interfaces over one general-purpose
- Dependency Inversion: Depend on abstractions, not concretions

## Error Handling
- Use typed errors/exceptions, not generic strings
- Errors should be catchable by type for different handling strategies
- Log errors with structured JSON (timestamp, level, message, context, stack trace)
- Never swallow errors silently — log or propagate
- Distinguish client errors (4xx) from server errors (5xx) in API responses

## Service Layer Patterns
- Repository pattern for data access (decouple business logic from DB)
- Service layer for business logic (not in controllers/handlers)
- Controllers/handlers only handle HTTP concerns (parsing, validation, response formatting)
- Dependency injection for testability

## API Contracts
- Validate all inputs at the boundary (controller/handler level)
- Use typed request/response models (not raw dicts/maps)
- Consistent error response format: `{error: {code, message, details}}`
- Pagination on all list endpoints (cursor or offset)
- Rate limiting on public endpoints

## Configuration Management
- All config from environment variables or config files, never hardcoded
- Separate config per environment (dev, staging, production)
- Secrets from environment variables or secret managers, never in code
- Fail fast on missing required config at startup

## Logging Standards
- Structured JSON logging (machine-parseable)
- Log levels: DEBUG, INFO, WARN, ERROR
- Include request ID / correlation ID in all log entries
- Never log sensitive data (passwords, tokens, PII)

## Graceful Shutdown
- Handle SIGTERM/SIGINT for clean shutdown
- Drain in-flight requests before stopping
- Close database connections cleanly
- Flush log buffers
