// Flashcards & Interview Review Dataset

export const flashcardsData = [
  {
    id: 1,
    category: "Databases & Consistency",
    front: "What is the key difference between PostgreSQL OFFSET vs Keyset Pagination?",
    back: "OFFSET scans and discards N rows (O(N) CPU/disk overhead) and skips/duplicates rows during concurrent writes. Keyset (Cursor) pagination uses indexed tuple comparisons `(created_at, id) < (last_date, last_id)` for deterministic O(log N) lookup time."
  },
  {
    id: 2,
    category: "Distributed Locks",
    front: "How do you correctly implement an Idempotent API lock in Redis?",
    back: "Use `SET lock_key lock_id NX PX 5000` to atomically acquire an exclusive 5-second lock. Check an existing response key `resp_key` first, execute card generation inside a try block, cache response for 24h, and release lock via Lua script comparing `lock_id`."
  },
  {
    id: 3,
    category: "Financial Systems",
    front: "What is Merchant Discount Rate (MDR) yield calculation?",
    back: "MDR Fee = Order Amount * MDR %. Net Bank Profit = Upfront MDR Fee - Expected Default Losses across remaining uncollected installments. For BNPL 4-pay: Default Loss = (Order Amount * 0.75) * Default Rate."
  },
  {
    id: 4,
    category: "Streaming & Messaging",
    front: "How does Kafka guarantee partition-level transaction ordering?",
    back: "By setting an explicit partition key (e.g. `account_id`) on every message. All events with the same key hash to the exact same Kafka partition and are consumed sequentially by a single thread in consumer groups."
  }
];
