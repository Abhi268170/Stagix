# API Design — Universal Principles

## REST Fundamentals
- Resources are nouns, not verbs: `/users`, not `/getUsers`
- HTTP methods: GET (read), POST (create), PUT (full update), PATCH (partial update), DELETE
- Status codes: 200 (OK), 201 (Created), 204 (No Content), 400 (Bad Request), 401 (Unauthorized), 403 (Forbidden), 404 (Not Found), 409 (Conflict), 422 (Unprocessable Entity), 429 (Too Many Requests), 500 (Internal Server Error)

## Error Response Format (RFC 7807)
```json
{
  "type": "https://api.example.com/errors/validation",
  "title": "Validation Error",
  "status": 422,
  "detail": "The 'email' field is not a valid email address",
  "instance": "/users",
  "errors": [{"field": "email", "message": "Invalid email format"}]
}
```

## Pagination
- Cursor-based for real-time data (preferred): `?cursor=abc&limit=20`
- Offset-based for static data: `?page=1&per_page=20`
- Always return: items, total count, next cursor/page link

## Versioning
- URL prefix preferred: `/api/v1/users`
- Never break existing clients — add fields, don't remove them
- Deprecation: announce, give migration window, then remove

## Rate Limiting
- Return headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`
- 429 response when exceeded
- Stricter limits on auth endpoints (login, register, password reset)
