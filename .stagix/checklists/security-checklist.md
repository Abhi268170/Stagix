# Security Audit Checklist

Security Specialist uses this. CRITICAL/HIGH block the story.

- [ ] Injection: SQL, NoSQL, command, XSS, LDAP
- [ ] Auth: password hashing, JWT, sessions, CSRF
- [ ] Authorisation: ownership checks, IDOR, role enforcement
- [ ] Secrets: no hardcoded credentials, env vars used
- [ ] Input validation: type, length, format, range
- [ ] File uploads: type whitelist, size limit, path traversal
- [ ] Error handling: no stack traces in production responses
- [ ] Dependencies: no known CVEs in new packages
- [ ] Rate limiting: on auth and abuse-prone endpoints
- [ ] Logging: security events logged, no sensitive data in logs
