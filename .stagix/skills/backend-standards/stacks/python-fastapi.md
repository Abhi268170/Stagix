# Python FastAPI Standards

## Project Structure
```
app/
├── main.py            # FastAPI app + lifespan
├── api/routes/        # Route handlers (thin — delegate to services)
├── services/          # Business logic
├── repositories/      # Database access (SQLAlchemy)
├── models/            # SQLAlchemy ORM models
├── schemas/           # Pydantic request/response models
├── core/config.py     # Settings via pydantic-settings
├── core/security.py   # Auth utilities
└── core/exceptions.py # Custom exception classes
```

## Conventions
- Type hints on ALL function signatures (mypy strict)
- Pydantic models for ALL request/response validation
- Async def for all route handlers and DB operations
- Dependency injection via FastAPI Depends()
- Alembic for migrations (never raw SQL in application code)
- Structured logging via structlog
- pytest + httpx for testing (AsyncClient for async endpoints)
