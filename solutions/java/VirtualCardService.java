package com.capitalone.prep;

import java.util.Optional;

/**
 * Case 2: Virtual Card Generation
 * Java Solution
 */
public class VirtualCardService {

    public interface CardDB {
        String createNewCard(String userId, Integer ttlHours);
        Optional<String> findActiveReusableCard(String userId);
    }

    private final CardDB db;

    public VirtualCardService(CardDB db) {
        this.db = db;
    }

    public String generateVirtualCard(String userId, int expiryHours, boolean isOneTime) {
        if (isOneTime) {
            return db.createNewCard(userId, expiryHours);
        }

        Optional<String> existingCard = db.findActiveReusableCard(userId);
        if (existingCard.isPresent()) {
            return existingCard.get();
        }

        return db.createNewCard(userId, null);
    }
}
