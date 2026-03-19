# Task: security-audit

## Purpose

Security Specialist's 8-point audit protocol. Systematic review of implemented code for vulnerabilities.

## Audit Checklist

Execute each check in order. For each finding, record: file, line range, severity, description, remediation.

### 1. Injection Vulnerabilities
- SQL injection: raw queries with string concatenation
- NoSQL injection: unsanitised query objects
- Command injection: user input in Bash/exec calls
- XSS: unescaped user content in templates
- LDAP injection (if applicable)

### 2. Authentication Flaws
- Password storage: must be bcrypt/argon2 (not MD5/SHA1/SHA256)
- JWT: check signing algorithm (must be RS256 or HS256 with strong secret), verify expiry
- Session: secure, httpOnly, SameSite cookie flags
- Password reset: token expiry, one-time use

### 3. Authorisation Gaps
- Every endpoint with user-specific data has ownership check
- Role-based access enforced at middleware level
- No IDOR: IDs in URLs validated against authenticated user
- Admin endpoints protected with appropriate role check

### 4. Secrets in Code
- Grep patterns: `password\s*=`, `api_key`, `secret`, `token`, `-----BEGIN`
- Check config files, .env.example, hardcoded URLs with credentials
- Verify all secrets come from environment variables

### 5. Input Validation
- All user inputs validated (type, length, format, range)
- File uploads restricted (type whitelist, size limit, no path traversal)
- Request body size limits configured
- Content-type validation on API endpoints

### 6. Error Handling
- Production error responses: no stack traces, no DB queries, no internal paths
- Error logging: structured, no sensitive data in logs
- Consistent error response format

### 7. Dependency Vulnerabilities
- Check lock files against known CVE databases
- Flag any dependency not in tech-stack.md
- Check for typosquatting on new packages

### 8. Rate Limiting & DoS Protection
- Auth endpoints (login, register, password reset) have rate limiting
- API endpoints have reasonable rate limits
- File upload endpoints have size limits

## Severity Calibration

- **CRITICAL**: Direct exploit path (SQL injection with user input, hardcoded admin password, auth bypass)
- **HIGH**: Exploitable with specific conditions (stored XSS, IDOR on sensitive data, weak JWT)
- **MEDIUM**: Should fix but not immediately exploitable (missing rate limiting, verbose errors in staging)
- **LOW**: Best practice (missing security headers, not using latest TLS)

## Output

Write findings to `.stagix/docs/security-report-{story-key}.md` per the agent's output format.
