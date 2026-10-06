package com.capitalone.prep;

import java.time.Instant;
import java.util.UUID;

public class KafkaCdcIngestion {

    public interface Database {
        String insertTransaction(String accountId, double amount, String merchant);
    }

    public interface KafkaProducer {
        void send(String topic, String key, String jsonPayload);
    }

    private final Database db;
    private final KafkaProducer producer;

    public KafkaCdcIngestion(Database db, KafkaProducer producer) {
        this.db = db;
        this.producer = producer;
    }

    public String processEvent(String accountId, double amount, String merchant) {
        String txnId = db.insertTransaction(accountId, amount, merchant);
        long timestamp = Instant.now().getEpochSecond();
        
        String jsonPayload = String.format(
            "{\"transaction_id\":\"%s\",\"account_id\":\"%s\",\"amount\":%.2f,\"timestamp\":%d,\"source\":\"MAINFRAME_CDC\"}",
            txnId, accountId, amount, timestamp
        );

        producer.send("transaction-events", accountId, jsonPayload);
        return txnId;
    }
}
