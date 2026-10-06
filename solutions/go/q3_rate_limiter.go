package main

import (
	"context"
	"time"

	"github.com/redis/go-redis/v9"
)

const rateLimitLua = `
local key = KEYS[1]
local now = tonumber(ARGV[1])
local window = tonumber(ARGV[2])
local limit = tonumber(ARGV[3])
local clearBefore = now - window

redis.call('ZREMRANGEBYSCORE', key, 0, clearBefore)
local currentRequests = redis.call('ZCARD', key)
if currentRequests < limit then
    redis.call('ZADD', key, now, now)
    redis.call('EXPIRE', key, math.ceil(window / 1000))
    return 1
else
    return 0
end
`

// DistributedRateLimiter implements Redis ZSET sliding window counter in Go
type DistributedRateLimiter struct {
	rdb      *redis.Client
	limit    int64
	windowMs int64
}

func NewRateLimiter(rdb *redis.Client, limit, windowMs int64) *DistributedRateLimiter {
	return &DistributedRateLimiter{rdb: rdb, limit: limit, windowMs: windowMs}
}

func (rl *DistributedRateLimiter) AllowRequest(ctx context.Context, identifier string) (bool, error) {
	key := "ratelimit:" + identifier
	nowMs := time.Now().UnixNano() / int64(time.Millisecond)
	res, err := rl.rdb.Eval(ctx, rateLimitLua, []string{key}, nowMs, rl.windowMs, rl.limit).Result()
	if err != nil {
		return false, err
	}
	return res.(int64) == 1, nil
}
