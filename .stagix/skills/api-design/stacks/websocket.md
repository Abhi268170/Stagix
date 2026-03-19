# WebSocket

## Conventions
- JSON message format with type field for routing
- Heartbeat/ping-pong for connection health
- Reconnection with exponential backoff on client
- Auth via initial HTTP upgrade headers or first message
- Rate limiting on message frequency
