package com.capitalone.prep;

import redis.clients.jedis.Jedis;

import java.util.HashMap;
import java.util.Map;

/**
 * System Design Q7: Distributed Banking Cache Architecture
 * Java Solution - Cache-Aside + SETNX Stampede Lock + Monotonic Version Check
 */
public class CacheAsideManager {

    public interface DBClient {
        AccountData queryAccount(String accountId);
    }

    public static class AccountData {
        public final double balance;
        public final long version;

        public AccountData(double balance, long version) {
            this.balance = balance;
            this.version = version;
        }
    }

    private final Jedis jedis;
    private final DBClient dbClient;

    public CacheAsideManager(Jedis jedis, DBClient dbClient) {
        this.jedis = jedis;
        this.dbClient = dbClient;
    }

    public AccountData getAccountBalance(String accountId, long clientMinVersion) throws InterruptedException {
        String cacheKey = "account:" + accountId + ":balance";
        String lockKey = "lock:account:" + accountId;

        Map<String, String> cached = jedis.hgetAll(cacheKey);
        if (cached != null && cached.containsKey("version")) {
            long ver = Long.parseLong(cached.get("version"));
            if (ver >= clientMinVersion) {
                double bal = Double.parseDouble(cached.get("balance"));
                return new AccountData(bal, ver);
            }
        }

        // Acquire lock to avoid cache stampede
        String setnxRes = jedis.set(lockKey, "LOCKED", redis.clients.jedis.params.SetParams.setParams().nx().ex(5));
        if (!"OK".equals(setnxRes)) {
            Thread.sleep(50);
            return getAccountBalance(accountId, clientMinVersion);
        }

        try {
            AccountData freshData = dbClient.queryAccount(accountId);
            Map<String, String> toCache = new HashMap<>();
            toCache.put("balance", String.valueOf(freshData.balance));
            toCache.put("version", String.valueOf(freshData.version));
            jedis.hset(cacheKey, toCache);
            jedis.expire(cacheKey, 300);
            return freshData;
        } finally {
            jedis.del(lockKey);
        }
    }
}
