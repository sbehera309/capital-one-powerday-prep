package com.capitalone.prep;

import java.util.Collections;
import java.util.List;

/**
 * Case 1: "Eeno" Real-Time Customer History Retrieval & Network Optimization
 * Java Solution
 */
public class CustomerDataStore {

    public interface StorageClient {
        List<String> retrieveRange(long customerId, long startTimestamp, long endTimestamp);
    }

    private final StorageClient store;

    public CustomerDataStore(StorageClient storageClient) {
        this.store = storageClient;
    }

    /**
     * Retrieves historical customer interactions within [currTime - timeWindowMinutes + 1, currTime].
     * Replaces O(T) sequential network calls with a single partition range query.
     */
    public List<String> retrieveRecent(long customerId, long currTime, long timeWindowMinutes) {
        if (timeWindowMinutes <= 0) {
            return Collections.emptyList();
        }
        long startTime = currTime - timeWindowMinutes + 1;
        return store.retrieveRange(customerId, startTime, currTime);
    }
}
