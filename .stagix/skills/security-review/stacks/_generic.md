# Generic Security

## Fallback
- Validate all inputs (type, length, format, range)
- Parameterised queries for all database access
- Output encoding for all user-generated content
- HTTPS everywhere, HSTS headers
- Secrets in environment variables, never in code
- Dependencies: lock versions, scan for known CVEs
