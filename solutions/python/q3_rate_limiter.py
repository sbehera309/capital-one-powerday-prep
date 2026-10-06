"""
Capital One PowerDay System Design Q3:
Distributed In-Memory Rate Limiter for Banking APIs (ZSET Sliding Window)
Language: Python
"""
import time
import redis

RATE_LIMIT_LUA = """
local key = KEYS[1]
local now = tonumber(ARGV[1])
local window = tonumber(ARGV[2])
local limit = tonumber(ARGV[3])
local clearBefore = now - window

-- Purge requests older than sliding window threshold
redis.call('ZREMRANGEBYSCORE', key, 0, clearBefore)
-- Count requests remaining in sliding window
local currentRequests = redis.call('ZCARD', key)
if currentRequests < limit then
    redis.call('ZADD', key, now, now)
    redis.call('EXPIRE', key, math.ceil(window / 1000))
    return 1 -- ALLOWED (HTTP 200)
else
    return 0 -- RATE LIMITED (HTTP 429)
end
"""

class DistributedRateLimiter:
    def __init__(self, r: redis.Redis, limit: int = 100, window_ms: int = 60000):
        self.r = r
        self.limit = limit
        self.window_ms = window_ms
        self._script = self.r.register_script(RATE_LIMIT_LUA)

    def allow_request(self, identifier: str) -> bool:
        key = f"ratelimit:{identifier}"
        now_ms = int(time.time() * 1000)
        res = self._script(keys=[key], args=[now_ms, self.window_ms, self.limit])
        return res == 1
