package com.capitalone.prep;

import java.util.concurrent.atomic.AtomicInteger;

/**
 * System Design Q6: Enterprise Multi-Channel Notification Engine
 * Java Solution - Circuit Breaker & Exponential Backoff Retry
 */
public class NotificationRetryManager {

    public static int calculateVisibilityTimeout(int retryCount, int baseSeconds) {
        return (int) (Math.pow(2, retryCount) * baseSeconds);
    }

    public static class SimpleCircuitBreaker {
        private final int failureThreshold;
        private final long recoveryTimeoutMs;
        private final AtomicInteger failureCount = new AtomicInteger(0);
        private volatile String state = "CLOSED";
        private volatile long lastFailureTime = 0;

        public SimpleCircuitBreaker(int failureThreshold, long recoveryTimeoutMs) {
            this.failureThreshold = failureThreshold;
            this.recoveryTimeoutMs = recoveryTimeoutMs;
        }

        public synchronized boolean canExecute() {
            if ("OPEN".equals(state)) {
                if (System.currentTimeMillis() - lastFailureTime > recoveryTimeoutMs) {
                    state = "HALF_OPEN";
                    return true;
                }
                return false;
            }
            return true;
        }

        public synchronized void recordResult(boolean success) {
            if (success) {
                failureCount.set(0);
                state = "CLOSED";
            } else {
                int failures = failureCount.incrementAndGet();
                lastFailureTime = System.currentTimeMillis();
                if (failures >= failureThreshold) {
                    state = "OPEN";
                }
            }
        }
    }
}
