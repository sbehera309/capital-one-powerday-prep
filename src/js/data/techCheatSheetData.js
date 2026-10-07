// Structured Dataset for Technical Case Studies Cheat Sheet
// Strictly Aligned with Capital One Technical Case Interview Questions & Coding Fixes

export const techCheatSheetData = {
  // Case-by-Case Breakdown
  caseBreakdowns: [
    {
      id: "cs-case-1",
      caseNum: "1",
      title: '"Eeno" Customer History (Keyset Pagination)',
      badge: "DB & Performance",
      color: "blue",
      category: "db-pagination",
      bugDescription: "SQL OFFSET N forces database engines to scan and discard N rows sequentially (O(N) latency). Concurrent writes shift row indexes, causing skipped or duplicated records on page navigation.",
      fixPattern: "Keyset (Cursor-Based) Pagination using tuple filtering backed by a composite B-Tree index.",
      codeSnippet: `-- ✅ Production Keyset Query (O(log N + LIMIT) execution)
SELECT id, amount, merchant, created_at
FROM transactions
WHERE account_id = $1 
  AND (created_at, id) < ($2, $3) -- Tuple comparison cursor
ORDER BY created_at DESC, id DESC
LIMIT $4;`,
      keyFormulas: [
        "OFFSET Scan Complexity: O(N) disk I/O scan",
        "Keyset Cursor Complexity: O(log N + LIMIT) B-Tree seek",
        "Index Required: (account_id, created_at DESC, id DESC)"
      ],
      interviewerProTip: "Highlight that keyset pagination provides 100% deterministic page boundaries even when 10,000 new transactions are inserted per second."
    },
    {
      id: "cs-case-2",
      caseNum: "2",
      title: "BNPL Cash Flow & MDR Net Yield",
      badge: "Financial Math",
      color: "cyan",
      category: "financial-math",
      bugDescription: "Flawed naive assumption: Net profit is assumed to be Gross MDR Fee ($400 × 4% = $16.00). Reality: Installment 1 ($100) is paid up-front at checkout with 0% risk. Credit default risk applies to the remaining 3 uncollected installments ($300 exposure = 75%). Ignoring default risk overstates profit by $3.60 (a 29% overestimation!).",
      fixPattern: "Calculate Net Bank Profit = Upfront MDR Revenue ($16.00) - Expected Credit Loss Reserve ($300 × 1.2% = $3.60) = $12.40 Net Profit (3.10% Net Bank Yield).",
      codeSnippet: `# ✅ Step-by-Step Risk-Adjusted BNPL Yield Model
upfront_mdr = order_val * 0.04                  # $400 * 4.0% = $16.00 Gross Revenue
merchant_payout = order_val - upfront_mdr        # $400 - $16.00 = $384.00 Payout
uncollected_capital = order_val * 0.75           # Installments 2, 3, 4 = $300.00
expected_default_loss = uncollected_capital * 0.012  # $300 * 1.2% = $3.60 Loss Reserve
net_bank_profit = upfront_mdr - expected_default_loss  # $16.00 - $3.60 = $12.40 Profit
net_bank_yield_pct = net_bank_profit / order_val       # $12.40 / $400 = 3.10% Yield`,
      keyFormulas: [
        "Gross MDR Revenue = Order Value ($400) × 4.0% = $16.00",
        "Uncollected Exposure = Order Value ($400) × 75% = $300.00",
        "Expected Credit Loss (ECL) = $300.00 × 1.2% = $3.60",
        "Net Profit = $16.00 - $3.60 = $12.40 (3.10% Net Yield on $400 GMV vs naive 4.00%)"
      ],
      interviewerProTip: "State clearly to the interviewer: 'Because Installment 1 is paid up-front at checkout, credit exposure exists ONLY on Installments 2, 3, and 4 ($300). Under CECL / IFRS 9 banking rules, loss reserves must be applied against uncollected capital exposure ($300 × 1.2% = $3.60), resulting in a net profit of $12.40.'"
    },
    {
      id: "cs-case-3",
      caseNum: "3",
      title: "Cross-Border FX Settlement (Thread-Safe Cache)",
      badge: "Concurrency & Memory",
      color: "teal",
      category: "concurrency",
      bugDescription: "Global unsynchronized FX variables cause data races in multi-threaded application servers. Lacking cache TTL expiration serves stale rates indefinitely, exposing the bank to FX arbitrage losses.",
      fixPattern: "Use read-write thread locks (sync.RWMutex / ConcurrentHashMap) combined with high-resolution epoch timestamp checks and a strict 2.0-second TTL.",
      codeSnippet: `// ✅ Go RWMutex Thread-Safe FX Engine with 2s TTL
func (e *FxEngine) GetRate(fetcher func() float64) float64 {
    e.mu.RLock()
    if time.Since(e.lastUpdate) < 2*time.Second && e.cachedRate > 0 {
        defer e.mu.RUnlock()
        return e.cachedRate
    }
    e.mu.RUnlock()

    e.mu.Lock()
    defer e.mu.Unlock()
    e.cachedRate = fetcher()
    e.lastUpdate = time.Now()
    return e.cachedRate
}`,
      keyFormulas: [
        "Cache Readiness: time.Since(lastUpdate) < TTL_DURATION",
        "Locking Strategy: RWMutex (Concurrent Reads, Exclusive Writes)",
        "Fresh Rate Fetch: Triggered automatically on TTL expiry"
      ],
      interviewerProTip: "Explain that RWMutex allows thousands of concurrent payment threads to read the cached rate simultaneously without lock contention."
    },
    {
      id: "cs-case-4",
      caseNum: "4",
      title: "Virtual Card Generation (Idempotency Locks)",
      badge: "API & Concurrency",
      color: "indigo",
      category: "concurrency",
      bugDescription: "Cellular network packet loss causes mobile app retry loops to submit duplicate HTTP POST requests, provisioning multiple virtual cards and double-charging client credit limits.",
      fixPattern: "Enforce API idempotency using atomic Redis distributed locks (SETNX) per (user_id, idempotency_key) and cache HTTP response payloads for 24 hours.",
      codeSnippet: `# ✅ Redis Atomic Idempotency Lock & Response Cache
lock_acquired = redis.set(f"lock:card:{user_id}:{idemp_key}", "LOCKED", nx=True, px=5000)
if not lock_acquired:
    return {"error": "Concurrent request in progress"}, 409

card = generate_virtual_card(user_id)
redis.set(f"resp:card:{user_id}:{idemp_key}", card, ex=86400) # Cache 24h
return card, 201`,
      keyFormulas: [
        "Lock Key: lock:card:{user_id}:{idempotency_key}",
        "Atomic Command: SET key value NX PX 5000 (5s TTL)",
        "Response Cache TTL: EX 86400 (24 Hours)"
      ],
      interviewerProTip: "Highlight that returning HTTP 409 Conflict during processing and cached HTTP 200 on replay adheres to Stripe / IETF API Idempotency Standards."
    },
    {
      id: "cs-case-5",
      caseNum: "5",
      title: "Security Alert Logic (Majority Voting)",
      badge: "Logic & Testing",
      color: "rose",
      category: "boolean-logic",
      bugDescription: "Unparenthesized boolean expressions (A && B || B && C || A && C) rely on compiler-specific operator precedence rules, causing unexpected evaluation short-circuits and silent false negatives.",
      fixPattern: "Refactor to integer majority voting (risk_score >= 2) or explicit parenthesized clauses.",
      codeSnippet: `// ✅ Majority Integer Risk Accumulator
public boolean shouldTriggerAlert(boolean newDev, boolean foreignIp, boolean highAmt) {
    int riskScore = (newDev ? 1 : 0) + (foreignIp ? 1 : 0) + (highAmt ? 1 : 0);
    return riskScore >= 2; // Trigger alert if 2 or 3 risk flags are active
}`,
      keyFormulas: [
        "Truth Table Permutations: 2^3 = 8 total state combinations",
        "Threshold Criteria: riskScore >= 2",
        "Evaluation Complexity: O(1) arithmetic integer addition"
      ],
      interviewerProTip: "Demonstrate how integer counting eliminates short-circuit precedence traps and easily scales when adding new risk flags."
    },
    {
      id: "cs-case-6",
      caseNum: "6",
      title: "Mainframe to Kafka Streaming (Partition Keys)",
      badge: "Event Streaming",
      color: "purple",
      category: "streaming",
      bugDescription: "Publishing Kafka events without partition keys (key=null) causes Kafka to distribute messages round-robin across partitions, breaking sequential event ordering for downstream consumers.",
      fixPattern: "Set account_id as explicit Kafka message partition key so murmur2(account_id) % partitions routes all events for a given account to the exact same partition.",
      codeSnippet: `// ✅ Partition-Keyed Kafka Producer (Strict Per-Account Ordering)
ProducerRecord<String, String> record = new ProducerRecord<>(
    "mainframe-txs",
    account.getId(), // ✅ Partition Key guarantees strict sequence delivery
    eventJsonPayload
);
kafkaTemplate.send(record);`,
      keyFormulas: [
        "Partition Hashing: murmur2(PartitionKey) % TotalPartitions",
        "Ordering Scope: Guaranteed FIFO within single partition only",
        "Throughput Benefit: Parallel processing across accounts without race conditions"
      ],
      interviewerProTip: "Emphasize that Kafka guarantees ordering ONLY within a single partition—not across the entire topic."
    },
    {
      id: "cs-case-7",
      caseNum: "7",
      title: "Mobile Payments Economics (Interchange-Plus)",
      badge: "Financial Math",
      color: "amber",
      category: "financial-math",
      bugDescription: "Omitting fixed per-transaction cents ($0.10 interchange + $0.02 tokenization) severely undercalculates fees on small transactions (< $10), distorting unit economics.",
      fixPattern: "Calculate complete Interchange-Plus pricing including variable %, fixed cents, network assessment %, and tokenization fees.",
      codeSnippet: `# ✅ Full Mobile Payment Interchange-Plus Model
interchange = (amount * 0.0175) + 0.10
network_assessment = amount * 0.0013
tokenization_fee = 0.02
total_processing_fee = interchange + network_assessment + tokenization_fee
merchant_net_payout = amount - total_processing_fee # $50 - $1.06 = $48.94`,
      keyFormulas: [
        "Interchange Fee = (Amount × 1.75%) + $0.10",
        "Network Assessment = Amount × 0.13%",
        "Tokenization Fee = $0.02",
        "Total Processing Fee = $0.875 + $0.10 + $0.065 + $0.02 = $1.06",
        "Merchant Payout = $50.00 - $1.06 = $48.94"
      ],
      interviewerProTip: "Point out that on a $5.00 transaction, fixed fees ($0.12) represent more than 50% of total fees, making fixed-cent modeling critical."
    }
  ],

  // Diagnostic Matrix for Common Anti-Patterns
  antiPatterns: [
    {
      category: "Database Pagination",
      buggyPattern: "SELECT ... OFFSET 5000 LIMIT 50",
      flaw: "Scans & discards 5000 rows (O(N) CPU/disk). Row indexes shift under concurrent inserts.",
      fixPattern: "WHERE (created_at, id) < (?, ?) LIMIT 50",
      ruleOfThumb: "Use Keyset Seek pagination for transactional feeds."
    },
    {
      category: "Credit Loss Reserve",
      buggyPattern: "Profit = GMV × MDR%",
      flaw: "Ignores expected credit loss (ECL) on uncollected future installments.",
      fixPattern: "Profit = MDR - (GMV × 75% × Default%)",
      ruleOfThumb: "Apply default loss reserves against uncollected capital exposure."
    },
    {
      category: "Cache Concurrency",
      buggyPattern: "var rate float64 = 0.85",
      flaw: "Data race across threads; serves expired rates indefinitely (arbitrage risk).",
      fixPattern: "RWMutex + Timestamp TTL check",
      ruleOfThumb: "Pair cache reads with high-resolution epoch TTL checks."
    },
    {
      category: "API Idempotency",
      buggyPattern: "POST /create-card (No Deduplication)",
      flaw: "Network retries execute POST logic multiple times, creating duplicate cards.",
      fixPattern: "Redis SETNX lock + 24h response cache",
      ruleOfThumb: "Require client Idempotency-Key headers on state-mutating POST APIs."
    },
    {
      category: "Boolean Algebra",
      buggyPattern: "A && B || B && C || A && C",
      flaw: "Implicit operator precedence creates unintended evaluation paths & false negatives.",
      fixPattern: "(A?1:0)+(B?1:0)+(C?1:0) >= 2",
      ruleOfThumb: "Convert complex boolean logic to integer threshold scoring."
    },
    {
      category: "Event Streaming",
      buggyPattern: "producer.send('topic', payload) [key=null]",
      flaw: "Round-robin distribution sends account events to random partitions out of order.",
      fixPattern: "producer.send('topic', accountId, payload)",
      ruleOfThumb: "Always pass entity ID as Kafka partition key for sequence integrity."
    },
    {
      category: "Payment Economics",
      buggyPattern: "Fee = Amount × 1.75%",
      flaw: "Omits fixed per-transaction cents ($0.10 + $0.02), distorting micro-transaction margins.",
      fixPattern: "Fee = (Amount × 1.75% + $0.10) + Assessment + Token",
      ruleOfThumb: "Never omit fixed-cent components in interchange-plus calculations."
    }
  ]
};
