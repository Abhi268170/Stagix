# Generic Backend Standards

## Fallback Standards
When no specific framework overlay exists, follow these generic patterns:
- Layer your code: HTTP handling → Business logic → Data access
- Validate all inputs at the boundary
- Use parameterised queries (never string concatenation for SQL)
- Structured JSON logging
- Environment-based configuration
- Write tests that cover business logic and edge cases
