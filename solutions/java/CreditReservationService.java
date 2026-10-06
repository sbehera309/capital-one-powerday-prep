package com.capitalone.prep;

import redis.clients.jedis.Jedis;
import java.util.Collections;

/**
 * System Design Q2: Credit Limit Concurrent Throttler & Atomic Balance Reservation
 * Java Solution
 */
public class CreditReservationService {

    private static final String LUA_SCRIPT = 
        "local available = tonumber(redis.call('GET', KEYS[1])) " +
        "local amount = tonumber(ARGV[1]) " +
        "if available and available >= amount then " +
        "    redis.call('DECRBY', KEYS[1], amount) " +
        "    return 1 " +
        "else " +
        "    return 0 " +
        "end";

    private final Jedis jedis;

    public CreditReservationService(Jedis jedis) {
        this.jedis = jedis;
    }

    public boolean reserveCredit(String accountId, long amount) {
        String key = "account:" + accountId + ":available_credit";
        Object result = jedis.eval(LUA_SCRIPT, Collections.singletonList(key), Collections.singletonList(String.valueOf(amount)));
        return Long.valueOf(1).equals(result);
    }
}
