# Security Review — Universal Principles

## OWASP Top 10 (2021)
1. **Broken Access Control** — Verify every endpoint checks ownership/permissions
2. **Cryptographic Failures** — Check for weak algorithms, hardcoded keys, plaintext secrets
3. **Injection** — SQL, NoSQL, OS command, LDAP — verify parameterised queries everywhere
4. **Insecure Design** — Check for missing rate limiting, no account lockout, predictable tokens
5. **Security Misconfiguration** — Default credentials, unnecessary features, verbose errors
6. **Vulnerable Components** — Check dependencies against known CVE databases
7. **Auth Failures** — Weak passwords, missing MFA, session fixation, JWT issues
8. **Data Integrity Failures** — Unsigned updates, deserialisation of untrusted data
9. **Logging Failures** — Insufficient logging of security events, log injection
10. **SSRF** — Server-side requests to user-controlled URLs

## Secrets Detection Patterns
- `password\s*=\s*['"]` — hardcoded passwords
- `api[_-]?key\s*=\s*['"]` — API keys
- `secret\s*=\s*['"]` — generic secrets
- `-----BEGIN .* PRIVATE KEY-----` — private keys
- `token\s*=\s*['"]` — tokens
- Connection strings with embedded credentials

## Auth Patterns to Verify
- Password hashing: bcrypt or argon2 (never MD5, SHA1, SHA256 alone)
- JWT: RS256 or HS256 with strong secret, verify expiry enforced
- Session cookies: Secure, HttpOnly, SameSite=Lax or Strict
- CSRF protection on state-changing endpoints
- Account lockout after failed attempts

## Input Validation Rules
- Validate type, length, format, range on ALL user inputs
- Whitelist validation preferred over blacklist
- File uploads: type whitelist, size limit, no path traversal
- URLs: validate scheme (no javascript:, data:), prevent SSRF
