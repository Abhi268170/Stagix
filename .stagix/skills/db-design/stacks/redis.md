# Redis

## Specifics
- Data structure selection: String, Hash, List, Set, Sorted Set, Stream
- TTL on all cache keys (no unbounded growth)
- Key naming convention: {service}:{entity}:{id}
- Lua scripts for atomic operations
- Redis Streams for message queuing
- Sentinel or Cluster for HA
