# Python Security

## Stack-Specific Risks
- pickle deserialization: never unpickle untrusted data
- SSRF via requests library: validate URLs, block internal IPs
- eval()/exec(): never with user input
- Template injection (Jinja2): use autoescape=True
- Django: verify CSRF middleware, check DEBUG=False in prod
- FastAPI: validate Pydantic models, check CORS origins
