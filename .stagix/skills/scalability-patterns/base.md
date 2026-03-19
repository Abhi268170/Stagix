# Scalability Patterns — Universal Principles

## Caching Strategy
- **Browser cache**: Static assets with long TTL + content hash in filename
- **CDN cache**: Public pages, images, API responses where appropriate
- **Application cache**: Computed results, session data, frequently-read configs
- **Database cache**: Query result caching, materialised views
- Cache invalidation: TTL-based (simple) or event-based (precise)

## Async Patterns
- I/O-bound work: async/await (don't block threads on network/disk)
- CPU-bound work: background jobs/workers (don't block request threads)
- Long-running tasks: message queue (RabbitMQ, SQS, Redis Streams)
- Webhooks for event notification instead of polling

## Database Scaling
- Read replicas for read-heavy workloads
- Connection pooling (PgBouncer, ProxySQL)
- Query optimisation before hardware scaling
- Partitioning for time-series or very large tables

## Stateless Design
- No server-side session state (use JWT or external session store)
- Any server can handle any request (horizontal scaling ready)
- File uploads to object storage (S3, GCS), not local disk

## Circuit Breaker Pattern
- Wrap external service calls with circuit breaker
- States: Closed (normal) → Open (failing, fast-fail) → Half-Open (test recovery)
- Prevents cascading failures across services
