package com.capitalone.prep;

import redis.clients.jedis.Jedis;
import java.util.Arrays;
import java.util.Collections;

/**
 * System Design Q3: Distributed In-Memory Rate Limiter for Banking APIs
 * Java Solution
 */
public class DistributedRateLimiter {

    private static final String LUA_SCRIPT = 
        "local key = KEYS[1] " +
        "local now = tonumber(ARGV[1]) " +
        "local window = tonumber(ARGV[2]) " +
        "local limit = tonumber(ARGV[3]) " +
        "local clearBefore = now - window " +
        "redis.call('ZREMRANGEBYSCORE', key, 0, clearBefore) " +
        "local currentRequests = redis.call('ZCARD', key) " +
        "if currentRequests < limit then " +
        "    redis.call('ZADD', key, now, now) " +
        "    redis.call('EXPIRE', key, math.ceil(window / 1000)) " +
        "    return 1 " +
        "else " +
        "    return 0 " +
        "end";

    private final Jedis jedis;
    private final long limit;
    private final long windowMs;

    public DistributedRateLimiter(Jedis jedis, long limit, long windowMs) {
        this.jedis = jedis;
        this.limit = limit;
        this.windowMs = windowMs;
    }

    public boolean allowRequest(String identifier) {
        String key = "ratelimit:" + identifier;
        long nowMs = System.currentTimeMillis();
        Object res = jedis.eval(LUA_SCRIPT, 
            Collections.singletonList(key), 
            Arrays.asList(String.valueOf(nowMs), String.valueOf(windowMs), String.valueOf(limit))
        );
        return Long.valueOf(1).equals(res);
    }
}
