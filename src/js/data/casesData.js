// Structured Dataset for Technical Cases (Sorted by Recency: 2025–2026 First)
// Enhanced with Comprehensive Engineering Explanations & Interview Thought Process Frameworks

export const casesData = [
  {
    id: "case-1",
    num: "1",
    title: '"Eeno" Customer History',
    badge: "Late 2025",
    color: "blue",
    difficulty: "Late 2025 • High Frequency",
    category: "Network & Dynamic Windowing",
    prompt: `"Eeno" allows users to request arbitrary windows of transaction history. Legacy pagination relies on SQL OFFSET, causing slow DB queries, database connection pool exhaustion, and duplicate/dropped records when new transactions are inserted concurrently. Implement an efficient keyset pagination algorithm.`,
    legacyCode: {
      python: `# ❌ BUGGY LEGACY CODE: SQL OFFSET pagination causes DB locks and skipped rows
def fetch_history_offset(db_conn, account_id: str, offset: int, limit: int):
    # 🐛 BUG: O(N) DB scan with OFFSET skips records when concurrent writes occur!
    query = f"SELECT id, amount, created_at FROM transactions WHERE account_id='{account_id}' ORDER BY created_at DESC LIMIT {limit} OFFSET {offset}"
    return db_conn.execute(query).fetchall()`,

      go: `// ❌ BUGGY LEGACY CODE: SQL OFFSET pagination causes DB locks and skipped rows
func FetchHistoryOffset(db *sql.DB, accountID string, offset, limit int) ([]Transaction, error) {
	// 🐛 BUG: O(N) DB scan with OFFSET skips records when concurrent writes occur!
	query := fmt.Sprintf("SELECT id, amount, created_at FROM txs WHERE account_id='%s' ORDER BY created_at DESC LIMIT %d OFFSET %d", accountID, limit, offset)
	return db.Query(query)
}`,

      java: `// ❌ BUGGY LEGACY CODE: SQL OFFSET pagination causes DB locks and skipped rows
public List<Transaction> fetchHistoryOffset(String accountId, int offset, int limit) {
    // 🐛 BUG: O(N) DB scan with OFFSET skips records when concurrent writes occur!
    String sql = String.format("SELECT id, amount, created_at FROM transactions WHERE account_id='%s' ORDER BY created_at DESC LIMIT %d OFFSET %d", accountId, limit, offset);
    return jdbcTemplate.query(sql, new TransactionRowMapper());
}`
    },
    causes: [
      "SQL OFFSET requires the database engine to scan and discard offset N rows, degrading query performance to O(N).",
      "Concurrent inserts shift row positions, leading to duplicate items across pages or missed transaction records."
    ],
    solutions: [
      "Keyset (Cursor-Based) Pagination using tuple comparison `(created_at, id) < (last_date, last_id)`.",
      "Index-backed query execution `(account_id, created_at DESC, id DESC)` guarantees O(log N + Limit) lookup time."
    ],
    code: {
      python: `def fetch_customer_history(db_conn, account_id: str, last_date=None, last_id=None, limit=50):
    # ✅ Keyset (Cursor-Based) Pagination: O(log N + Limit) execution
    params = [account_id]
    where_clause = "account_id = %s"
    
    if last_date and last_id:
        # Tuple comparison guarantees deterministic page boundaries under concurrent writes
        where_clause += " AND (created_at, id) < (%s, %s)"
        params.extend([last_date, last_id])
    
    query = f"""
        SELECT id, amount, merchant, created_at
        FROM transactions
        WHERE {where_clause}
        ORDER BY created_at DESC, id DESC
        LIMIT %s
    """
    params.append(limit)
    return db_conn.execute(query, params).fetchall()`,

      go: `// ✅ Keyset (Cursor-Based) Pagination in Go with SQL Prepared Parameterization
func FetchCustomerHistory(ctx context.Context, db *sql.DB, accountID string, lastDate time.Time, lastID string, limit int) ([]Transaction, error) {
	var query string
	var args []interface{}

	if !lastDate.IsZero() && lastID != "" {
		query = \`SELECT id, amount, merchant, created_at FROM transactions 
				 WHERE account_id = $1 AND (created_at, id) < ($2, $3) 
				 ORDER BY created_at DESC, id DESC LIMIT $4\`
		args = []interface{}{accountID, lastDate, lastID, limit}
	} else {
		query = \`SELECT id, amount, merchant, created_at FROM transactions 
				 WHERE account_id = $1 
				 ORDER BY created_at DESC, id DESC LIMIT $2\`
		args = []interface{}{accountID, limit}
	}
	rows, err := db.QueryContext(ctx, query, args...)
	if err != nil { return nil, err }
	defer rows.Close()
	return parseRows(rows), nil
}`,

      java: `// ✅ Production Keyset Pagination in Java (Spring JDBC Template)
public List<Transaction> fetchCustomerHistory(String accountId, Instant lastDate, String lastId, int limit) {
    String sql = "SELECT id, amount, merchant, created_at FROM transactions WHERE account_id = ?";
    List<Object> params = new ArrayList<>(List.of(accountId));
    if (lastDate != null && lastId != null) {
        sql += " AND (created_at, id) < (?, ?)";
        params.add(lastDate);
        params.add(lastId);
    }
    sql += " ORDER BY created_at DESC, id DESC LIMIT ?";
    params.add(limit);
    return jdbcTemplate.query(sql, params.toArray(), new TransactionRowMapper());
}`
    },
    explanation: {
      clarifyingQuestions: [
        "What is the expected table size and write volume (QPS) for transaction history?",
        "Do transactions arrive in strict chronological order or can late-arriving events occur?",
        "Does the frontend UI require jumping to arbitrary page numbers (e.g. Page 450), or infinite scrolling?"
      ],
      hiddenTrap: "SQL OFFSET N degrades query execution time to O(N) because database storage engines (InnoDB/Postgres) must scan disk blocks and discard the first N rows sequentially. Furthermore, under high concurrent write throughput (e.g., real-time credit card authorizations), inserting a record while a user scrolls from Page 1 to Page 2 shifts all row indexes, causing duplicated records on Page 2 or permanently skipped transactions.",
      technicalRationale: "Keyset (cursor-based) pagination uses tuple filtering `(created_at, id) < (last_date, last_id)` backed by a composite index `(account_id, created_at DESC, id DESC)`. The database engine performs a logarithmic B-Tree seek directly to the last seen cursor position in O(log N) time, fetching exactly LIMIT records without scanning prior rows.",
      alternatives: [
        {
          name: "SQL OFFSET / LIMIT",
          status: "Rejected",
          reason: "Degrades to O(N) performance on deep pages and causes duplicate/missing records under concurrent inserts."
        },
        {
          name: "Elasticsearch Search-After",
          status: "Considered",
          reason: "Viable for complex text search, but rejected for primary transaction history due to 1-second indexing refresh lag and operational overhead."
        },
        {
          name: "Keyset Tuple Pagination (Selected)",
          status: "Selected",
          reason: "Sub-10ms performance at arbitrary table depth with guaranteed deterministic page boundaries under concurrent writes."
        }
      ]
    }
  },
  {
    id: "case-2",
    num: "2",
    title: "BNPL Cash Flow & MDR Yield",
    badge: "2025–2026",
    color: "cyan",
    difficulty: "2025–2026 • High Impact",
    category: "Installment Loss & Capital Yield",
    prompt: `"Buy-Now-Pay-Later (BNPL) splits a $400 order into 4 equal installments of $100. Merchants pay a 4.0% MDR fee up front ($16). However, installment defaults occur across installments 2, 3, and 4 at a 1.2% loss rate. Write a financial cash flow calculator to evaluate net bank yield."`,
    legacyCode: {
      python: `# ❌ LEGACY BUGGY CODE: Flawed yield model ignores installment default risk
def calculate_bnpl_profit(order_amount: float) -> float:
    mdr_revenue = order_amount * 0.04
    # 🐛 BUG: Assumes 100% of customers pay all 4 installments! Zero loss reserve factored!
    return mdr_revenue  # Overstates profit by $3.60 on a $400 purchase.`,

      go: `// ❌ LEGACY BUGGY CODE: Flawed yield model ignores installment default risk
func CalculateBnplProfit(orderAmount float64) float64 {
	mdrRevenue := orderAmount * 0.04
	// 🐛 BUG: Assumes 100% of customers pay all 4 installments! Zero loss reserve factored!
	return mdrRevenue // Overstates profit by $3.60 on a $400 purchase.
}`,

      java: `// ❌ LEGACY BUGGY CODE: Flawed yield model ignores installment default risk
public double calculateBnplProfit(double orderAmount) {
    double mdrRevenue = orderAmount * 0.04;
    // 🐛 BUG: Assumes 100% of customers pay all 4 installments! Zero loss reserve factored!
    return mdrRevenue; // Overstates profit by $3.60 on a $400 purchase.
}`
    },
    causes: [
      "Assumed zero installment defaults, overstating net profit margins on BNPL financing products."
    ],
    solutions: [
      "Factored 1.2% default loss rate across remaining 75% uncollected capital ($3.60 expected loss).",
      "Net bank profit = $16.00 MDR revenue - $3.60 expected loss = $12.40 net yield."
    ],
    code: {
      python: `def calculate_bnpl_yield(order_val: float, mdr_pct=0.04, default_rate=0.012) -> dict:
    # ✅ Risk-adjusted BNPL installment yield model
    upfront_mdr = order_val * mdr_pct
    merchant_payout = order_val - upfront_mdr
    expected_default_loss = (order_val * 0.75) * default_rate
    net_bank_profit = upfront_mdr - expected_default_loss
    return {
        "order_val": order_val,
        "upfront_mdr": upfront_mdr,
        "merchant_payout": merchant_payout,
        "expected_default_loss": expected_default_loss,
        "net_bank_profit": net_bank_profit
    }`,

      go: `func CalculateBnplYield(orderVal float64, mdrPct, defaultRate float64) BnplYield {
	mdr := orderVal * mdrPct
	payout := orderVal - mdr
	loss := (orderVal * 0.75) * defaultRate
	profit := mdr - loss
	return BnplYield{OrderVal: orderVal, UpfrontMDR: mdr, MerchantPayout: payout, NetProfit: profit}
}`,

      java: `public BnplYield calculateBnplYield(double orderVal, double mdrPct, double defaultRate) {
    double mdr = orderVal * mdrPct;
    double payout = orderVal - mdr;
    double loss = (orderVal * 0.75) * defaultRate;
    double profit = mdr - loss;
    return new BnplYield(orderVal, mdr, payout, loss, profit);
}`
    },
    explanation: {
      clarifyingQuestions: [
        "Is merchant payout settled immediately at checkout (T+0) or as installments are collected over time?",
        "Does the 1.2% default loss rate apply to total order value ($400) or to uncollected future installments ($300)?",
        "Are late payment penalty fees or debt collection recoveries included in net bank yield?"
      ],
      hiddenTrap: "FLAWED NAIVE ASSUMPTION:\nMany developers assume net profit is simply Gross MDR Fee ($400 × 4.0% = $16.00), treating the product as having a 4.0% profit margin.\n\nTHE FINANCIAL RISK REALITY:\nInstallment 1 ($100) is paid immediately at checkout by the customer, so there is ZERO credit risk on Installment 1. The bank extends credit ONLY on Installments 2, 3, and 4 ($300 total or 75% of order value) over 90 days. If 1.2% of customers default across installments 2–4, the expected credit loss (ECL) is 1.2% of $300 = $3.60. Ignoring default risk overstates net bank profit by $3.60 (a 29% overestimation of net profit!).",
      technicalRationale: "COMPLETE STEP-BY-STEP FINANCIAL MATH BREAKDOWN:\n\n1. Order Breakdown:\n   • Order Value = $400.00 split into 4 equal installments of $100.00.\n   • Installment 1 ($100.00): Paid up-front at checkout (0% default risk exposure).\n   • Installments 2, 3, 4 ($300.00): Outstanding uncollected credit exposure = $400.00 × 75%.\n\n2. Merchant Settlement:\n   • Merchant Discount Rate (MDR) = 4.0% up front.\n   • Gross MDR Revenue to Bank = $400.00 × 4.0% = $16.00.\n   • Net Merchant Payout = $400.00 - $16.00 = $384.00.\n\n3. Credit Loss Reserve (CECL / IFRS 9 Standard):\n   • Expected Default Loss = Uncollected Exposure × Default Rate\n   • Expected Default Loss = $300.00 × 1.2% = $3.60.\n\n4. Net Bank Profit & Portfolio Yield:\n   • Net Bank Profit = Gross MDR Revenue - Expected Default Loss\n   • Net Bank Profit = $16.00 - $3.60 = $12.40.\n   • Net Bank Yield % = $12.40 / $400.00 = 3.10% (vs naive 4.00% assumption).",
      alternatives: [
        {
          name: "Gross Revenue Model (Zero Loss Reserve)",
          status: "Rejected",
          reason: "Assumes 100% collection efficiency, overstating net bank profit by 29% ($16.00 vs $12.40) and violating CECL banking regulations."
        },
        {
          name: "Gross GMV Loss Reserve ($400 × 1.2%)",
          status: "Considered",
          reason: "Flawed because Installment 1 ($100) is collected immediately at checkout without credit default exposure."
        },
        {
          name: "Uncollected Capital ECL Reserve (Selected)",
          status: "Selected",
          reason: "Accurate credit risk modeling ($300 uncollected exposure × 1.2% default rate = $3.60 loss), yielding exact $12.40 net profit (3.10% net yield)."
        }
      ]
    }
  },
  {
    id: "case-3",
    num: "3",
    title: "Real-Time Cross-Border FX Settlement",
    badge: "2025–2026",
    color: "teal",
    difficulty: "2025–2026 • Distributed Systems",
    category: "Cross-Border FX & Liquidity",
    prompt: `"Cross-border payments require converting USD to EUR at fluctuating FX rates. The legacy service caches FX rates globally without locking or timestamp validation, causing stale rate arbitrage losses during market spikes. Write a thread-safe FX settlement rate engine with max 2-second rate validity."`,
    legacyCode: {
      python: `# ❌ LEGACY BUGGY CODE: Global static variable without cache TTL or locking
USD_TO_EUR_RATE = 0.85 # 🐛 BUG: Stale rate used indefinitely!

def get_fx_rate():
    return USD_TO_EUR_RATE`,

      go: `// ❌ LEGACY BUGGY CODE: Global unsynchronized variable without cache TTL
var usdToEurRate = 0.85 // 🐛 BUG: Stale rate used indefinitely!

func GetFxRate() float64 {
	return usdToEurRate
}`,

      java: `// ❌ LEGACY BUGGY CODE: Global static variable without synchronization or TTL
public class FxRateCache {
    private static double usdToEurRate = 0.85; // 🐛 BUG: Stale rate used indefinitely!
    public static double getRate() { return usdToEurRate; }
}`
    },
    causes: [
      "Global unsynchronized FX rate storage leads to race conditions and stale rate execution.",
      "Lack of TTL cache invalidation allows users to execute trades at expired, arbitrage-vulnerable prices."
    ],
    solutions: [
      "Atomic/Thread-safe rate cache with high-resolution epoch timestamp check.",
      "Strict 2-second TTL expiration window forcing fresh market rate fetches on stale cache hits."
    ],
    code: {
      python: `import time

class FxRateEngine:
    def __init__(self, ttl_seconds=2.0):
        self.ttl = ttl_seconds
        self.cached_rate = None
        self.last_update = 0.0

    def get_valid_rate(self, current_market_fetcher) -> float:
        now = time.time()
        if self.cached_rate is None or (now - self.last_update) > self.ttl:
            self.cached_rate = current_market_fetcher()
            self.last_update = now
        return self.cached_rate`,

      go: `type FxEngine struct {
	mu         sync.RWMutex
	cachedRate float64
	lastUpdate time.Time
	ttl        time.Duration
}

func (e *FxEngine) GetRate(fetcher func() float64) float64 {
	e.mu.RLock()
	if time.Since(e.lastUpdate) < e.ttl && e.cachedRate > 0 {
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

      java: `public class ThreadSafeFxEngine {
    private final ConcurrentHashMap<String, FxRateRecord> cache = new ConcurrentHashMap<>();
    private final Duration ttl = Duration.ofSeconds(2);

    public double getValidRate(String pair, Supplier<Double> marketFetcher) {
        FxRateRecord current = cache.get(pair);
        if (current == null || Instant.now().isAfter(current.timestamp().plus(ttl))) {
            double freshRate = marketFetcher.get();
            cache.put(pair, new FxRateRecord(freshRate, Instant.now()));
            return freshRate;
        }
        return current.rate();
    }
}`
    },
    explanation: {
      clarifyingQuestions: [
        "What is the upstream FX market provider update frequency and rate limit?",
        "What is the read QPS vs write update rate for currency pairs?",
        "How do we handle network outages when fetching fresh FX market rates?"
      ],
      hiddenTrap: "Global unsynchronized state causes data races across application threads. More critically, serving stale FX rates without a Time-To-Live (TTL) expiration window exposes the bank to latency arbitrage attacks—where algorithmic traders exploit expired FX rates during high volatility, causing substantial settlement loss.",
      technicalRationale: "Thread safety is achieved via read-write locks (`sync.RWMutex` in Go or `ConcurrentHashMap` in Java), allowing high-throughput concurrent reads. High-resolution epoch timestamp checks enforce a strict 2.0-second TTL validity window. If the cache expires, execution locks write access, fetches fresh rate ticks, and updates the timestamp atomically.",
      alternatives: [
        {
          name: "Direct Upstream Fetch per Transaction",
          status: "Rejected",
          reason: "Adds 150ms–300ms network latency per payment and breaches upstream rate limit quotas."
        },
        {
          name: "Unsynchronized Static Caching",
          status: "Rejected",
          reason: "Causes data race crashes and serves stale prices, exposing bank to FX arbitrage losses."
        },
        {
          name: "RWMutex + 2s Timestamp TTL (Selected)",
          status: "Selected",
          reason: "Provides sub-millisecond local memory lookup speed with strict 2-second rate freshness."
        }
      ]
    }
  },
  {
    id: "case-4",
    num: "4",
    title: "Virtual Card Generation",
    badge: "Mid 2025",
    color: "indigo",
    difficulty: "Mid 2025 • High Concurrency",
    category: "Idempotency & Distributed Locks",
    prompt: `"Users generating virtual cards under slow cellular connections tap the 'Create Card' button repeatedly. The legacy backend lacks idempotency keys, creating duplicate virtual cards and draining merchant credit limits. Write an idempotent card creation handler using Redis distributed locks."`,
    legacyCode: {
      python: `# ❌ LEGACY BUGGY CODE: No lock or deduplication key check
@app.route('/create-card', methods=['POST'])
def create_card():
    # 🐛 BUG: Duplicate HTTP POST creates 2 distinct virtual card numbers!
    card = card_service.generate_new_card(request.json['user_id'])
    return jsonify(card)`,

      go: `// ❌ LEGACY BUGGY CODE: No lock or deduplication key check
func CreateCardHandler(w http.ResponseWriter, r *http.Request) {
	// 🐛 BUG: Duplicate HTTP POST creates 2 distinct virtual card numbers!
	card := generateNewCard(r.FormValue("user_id"))
	json.NewEncoder(w).Encode(card)
}`,

      java: `// ❌ LEGACY BUGGY CODE: No lock or deduplication key check
@PostMapping("/create-card")
public ResponseEntity<VirtualCard> createCard(@RequestBody CardRequest req) {
    // 🐛 BUG: Duplicate HTTP POST creates 2 distinct virtual card numbers!
    VirtualCard card = cardService.generateNewCard(req.getUserId());
    return ResponseEntity.ok(card);
}`
    },
    causes: [
      "Absence of API idempotency key handling allowed parallel duplicate POST requests to execute.",
      "Race conditions in card generation database inserts caused duplicate card provisioning."
    ],
    solutions: [
      "Redis `SET key value NX PX 5000` atomic lock per `(user_id, idempotency_key)`.",
      "Cached idempotency response storage ensures duplicate requests receive the exact initial card response."
    ],
    code: {
      python: `import redis

r = redis.Redis()

def idempotent_create_card(user_id: str, idempotency_key: str, card_generator_func):
    lock_key = f"lock:card:{user_id}:{idempotency_key}"
    resp_key = f"resp:card:{user_id}:{idempotency_key}"
    
    # Check if request was already processed
    cached_resp = r.get(resp_key)
    if cached_resp:
        return cached_resp.decode('utf-8'), 200
        
    # Acquire atomic lock (5s TTL)
    if r.set(lock_key, "LOCKED", nx=True, px=5000):
        try:
            card_data = card_generator_func(user_id)
            r.set(resp_key, card_data, ex=86400) # Cache response 24h
            return card_data, 201
        finally:
            r.delete(lock_key)
    else:
        return {"error": "Concurrent request in progress"}, 409`,

      go: `func HandleIdempotentCardCreation(ctx context.Context, rdb *redis.Client, userID, idempKey string) (string, error) {
	lockKey := fmt.Sprintf("lock:card:%s:%s", userID, idempKey)
	respKey := fmt.Sprintf("resp:card:%s:%s", userID, idempKey)

	val, err := rdb.Get(ctx, respKey).Result()
	if err == nil { return val, nil }

	ok, err := rdb.SetNX(ctx, lockKey, "LOCKED", 5*time.Second).Result()
	if err != nil || !ok { return "", errors.New("concurrent request blocked") }
	defer rdb.Del(ctx, lockKey)

	newCard := generateCard(userID)
	rdb.Set(ctx, respKey, newCard, 24*time.Hour)
	return newCard, nil
}`,

      java: `public String createVirtualCardIdempotent(String userId, String idempKey) {
    String lockKey = "lock:card:" + userId + ":" + idempKey;
    String respKey = "resp:card:" + userId + ":" + idempKey;

    String existing = redis.get(respKey);
    if (existing != null) return existing;

    Boolean locked = redis.setIfAbsent(lockKey, "LOCKED", Duration.ofSeconds(5));
    if (Boolean.TRUE.equals(locked)) {
        try {
            String card = cardGenerator.apply(userId);
            redis.set(respKey, card, Duration.ofHours(24));
            return card;
        } finally {
            redis.del(lockKey);
        }
    }
    throw new ConcurrentRequestException("Duplicate request blocked");
}`
    },
    explanation: {
      clarifyingQuestions: [
        "How is the `Idempotency-Key` header generated by the mobile client (e.g. UUIDv4 per intent)?",
        "How long should the generated virtual card response be cached in Redis? (e.g. 24 hours)",
        "How do we handle cases where card creation fails mid-execution (e.g. DB connection timeout)?"
      ],
      hiddenTrap: "When mobile networks experience packet loss, mobile apps automatically retry HTTP POST requests. Without server-side idempotency, two identical requests hit separate application servers concurrently. Both pass validation checks and issue two separate virtual cards, exhausting user credit limits and causing account synchronization corruption.",
      technicalRationale: "An atomic Redis `SET lock_key LOCKED NX PX 5000` operation acquires a distributed lock in < 1ms across horizontal cluster nodes. If a request with the same `Idempotency-Key` arrives while processing, Redis rejects lock acquisition and returns HTTP 409 Conflict. Once complete, the response payload is cached in Redis for 24 hours (`EX 86400`), guaranteeing identical replay responses.",
      alternatives: [
        {
          name: "DB Unique Constraint Only",
          status: "Considered",
          reason: "Prevents duplicate rows, but throws raw database constraint violation errors instead of returning the generated card details."
        },
        {
          name: "In-Memory Process Lock",
          status: "Rejected",
          reason: "Fails in multi-node load-balanced server environments where requests hit different servers."
        },
        {
          name: "Redis Atomic Lock + 24h Response Cache (Selected)",
          status: "Selected",
          reason: "Distributed, multi-region capable, and adheres to enterprise API idempotency standards."
        }
      ]
    }
  },
  {
    id: "case-5",
    num: "5",
    title: "3-Boolean Security Alert Logic",
    badge: "Mid 2024",
    color: "rose",
    difficulty: "Mid 2024 • Logic & Testing",
    category: "Boolean Algebra & Short-Circuit Bugs",
    prompt: `"A security alert system uses 3 flags: is_new_device, is_foreign_ip, is_high_amount. The alert should trigger IF (is_new_device AND is_foreign_ip) OR (is_foreign_ip AND is_high_amount) OR (is_new_device AND is_high_amount). The legacy code used incorrect operator precedence, causing false negative security alerts."`,
    legacyCode: {
      python: `# ❌ LEGACY BUGGY CODE: Operator precedence flaw without grouping parentheses
def should_trigger_alert(is_new_device, is_foreign_ip, is_high_amount):
    # 🐛 BUG: Operator precedence evaluates AND before OR incorrectly!
    return is_new_device and is_foreign_ip or is_foreign_ip and is_high_amount or is_new_device and is_high_amount # Flawed precedence!`,

      go: `// ❌ LEGACY BUGGY CODE: Operator precedence flaw without grouping parentheses
func ShouldTriggerAlert(newDev, foreignIP, highAmt bool) bool {
	// 🐛 BUG: Operator precedence evaluates AND before OR incorrectly!
	return newDev && foreignIP || foreignIP && highAmt || newDev && highAmt
}`,

      java: `// ❌ LEGACY BUGGY CODE: Operator precedence flaw without grouping parentheses
public boolean shouldTriggerAlert(boolean newDev, boolean foreignIp, boolean highAmt) {
    // 🐛 BUG: Operator precedence evaluates AND before OR incorrectly!
    return newDev && foreignIp || foreignIp && highAmt || newDev && highAmt; // Flawed precedence!
}`
    },
    causes: [
      "Unparenthesized boolean expression relied on implicit operator precedence, resulting in missed alert triggers."
    ],
    solutions: [
      "Majority-voting logic: Alert triggers if sum of true flags >= 2.",
      "Clean parenthesized boolean evaluation: `(A && B) || (B && C) || (A && C)`."
    ],
    code: {
      python: `def should_trigger_alert(is_new_device: bool, is_foreign_ip: bool, is_high_amount: bool) -> bool:
    # ✅ Majority Voting: Trigger alert if 2 or more risk flags are active
    risk_score = sum([is_new_device, is_foreign_ip, is_high_amount])
    return risk_score >= 2`,

      go: `func ShouldTriggerAlert(newDev, foreignIP, highAmt bool) bool {
	count := 0
	if newDev { count++ }
	if foreignIP { count++ }
	if highAmt { count++ }
	return count >= 2
}`,

      java: `public boolean shouldTriggerAlert(boolean newDev, boolean foreignIp, boolean highAmt) {
    int riskCount = (newDev ? 1 : 0) + (foreignIp ? 1 : 0) + (highAmt ? 1 : 0);
    return riskCount >= 2;
}`
    },
    explanation: {
      clarifyingQuestions: [
        "Are all 3 security risk flags weighted equally in risk scoring?",
        "Should the logic support dynamic weights (e.g. `is_foreign_ip` = 2 points)?",
        "How is this evaluated under high-throughput authorization pipelines?"
      ],
      hiddenTrap: "Writing complex unparenthesized boolean expressions `A && B || B && C || A && C` relies on compiler-specific operator precedence rules. Subtle bugs emerge when developers misinterpret short-circuit evaluation order, leading to silent false negatives where critical fraud alerts fail to fire.",
      technicalRationale: "Refactoring to majority-voting arithmetic (`(A ? 1 : 0) + (B ? 1 : 0) + (C ? 1 : 0) >= 2`) converts fragile boolean logic into deterministic integer counting. It mathematically guarantees that any combination of 2 or 3 active risk flags triggers an alert, eliminating boolean operator precedence bugs entirely.",
      alternatives: [
        {
          name: "Unparenthesized Boolean Chain",
          status: "Rejected",
          reason: "High risk of operator precedence bugs and poor readability during code reviews."
        },
        {
          name: "Parenthesized Grouping `(A&&B)||(B&&C)||(A&&C)`",
          status: "Considered",
          reason: "Correct, but harder to extend when adding a 4th risk flag."
        },
        {
          name: "Majority Integer Risk Accumulator (Selected)",
          status: "Selected",
          reason: "Extensible, 100% testable against all 8 truth table permutations, and self-documenting."
        }
      ]
    }
  },
  {
    id: "case-6",
    num: "6",
    title: "Mainframe to Kafka Streaming",
    badge: "Early 2024",
    color: "purple",
    difficulty: "Early 2024 • Event Streaming",
    category: "EBCDIC Parsing & Kafka Ordering",
    prompt: `"Legacy mainframe EBCDIC copybook files are streamed to Kafka topics. The legacy parser used non-atomic batch writes, causing out-of-order transaction events and unparseable binary header corruption in downstream microservices. Write a partition-keyed Kafka producer guaranteeing strict per-account event ordering."`,
    legacyCode: {
      python: `# ❌ LEGACY BUGGY CODE: No partition key assigned to Kafka messages
def produce_mainframe_event(producer, event_data):
    # 🐛 BUG: Round-robin partitioning sends account events across multiple partitions!
    producer.send('mainframe-txs', value=event_data.encode('utf-8'))`,

      go: `// ❌ LEGACY BUGGY CODE: No partition key assigned to Kafka messages
func ProduceMainframeEvent(producer sarama.SyncProducer, event Event) error {
	// 🐛 BUG: Round-robin partitioning sends account events across multiple partitions!
	msg := &sarama.ProducerMessage{Topic: "mainframe-txs", Value: sarama.StringEncoder(event.Data)}
	_, _, err := producer.SendMessage(msg)
	return err
}`,

      java: `// ❌ LEGACY BUGGY CODE: No partition key assigned to Kafka messages
public void produceMainframeEvent(KafkaTemplate<String, String> kafka, String eventData) {
    // 🐛 BUG: Round-robin partitioning sends account events across multiple partitions!
    kafka.send("mainframe-txs", eventData);
}`
    },
    causes: [
      "Absence of message partition key caused Kafka to distribute transactions across partitions round-robin, breaking sequential ordering.",
      "Downstream consumers processed out-of-order events (e.g. account closure processed before deposit)."
    ],
    solutions: [
      "Set `account_id` as the explicit Kafka message partition key.",
      "Guarantees all transactions for a given account land in the exact same partition in strict sequential order."
    ],
    code: {
      python: `from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

def send_mainframe_event(account_id: str, event_payload: dict):
    # ✅ Explicit key parameter routes all events for account_id to the same partition
    producer.send(
        topic='mainframe-txs',
        key=account_id.encode('utf-8'),
        value=json.dumps(event_payload).encode('utf-8')
    )`,

      go: `func ProduceMainframeEventOrdered(producer sarama.SyncProducer, accountID string, payload []byte) error {
	msg := &sarama.ProducerMessage{
		Topic: "mainframe-txs",
		Key:   sarama.StringEncoder(accountID), // ✅ Guarantees partition-level ordering
		Value: sarama.ByteEncoder(payload),
	}
	_, _, err := producer.SendMessage(msg)
	return err
}`,

      java: `public void publishMainframeEvent(String accountId, MainframeEvent event) {
    ProducerRecord<String, String> record = new ProducerRecord<>(
        "mainframe-txs",
        accountId, // ✅ Partition Key guarantees strict sequence delivery
        objectMapper.writeValueAsString(event)
    );
    kafkaTemplate.send(record);
}`
    },
    explanation: {
      clarifyingQuestions: [
        "Are events for different bank accounts independent and able to process concurrently?",
        "What is the Kafka topic partition count and replication factor?",
        "How do downstream consumers handle event replay or failed offsets?"
      ],
      hiddenTrap: "When Kafka messages are published without a partition key (`key=null`), Kafka's default partitioner distributes messages using round-robin round robin across all topic partitions. Because consumers process different partitions independently in parallel, downstream microservices receive out-of-order events (e.g., an `ACCOUNT_CLOSED` event arrives before a `DEPOSIT` event), breaking financial ledger sequence integrity.",
      technicalRationale: "Setting `account_id` as the explicit Kafka message key routes all transactions for a specific bank account to the exact same Kafka partition via `murmur2(account_id) % num_partitions`. Kafka guarantees strict FIFO message ordering within a single partition, ensuring downstream consumer workers process account history sequentially.",
      alternatives: [
        {
          name: "Single Kafka Topic Partition",
          status: "Rejected",
          reason: "Guarantees global ordering but bottlenecking ingestion throughput to a single broker node."
        },
        {
          name: "Round-Robin Keyless Publishing",
          status: "Rejected",
          reason: "Causes out-of-order event consumption across consumer group threads."
        },
        {
          name: "Account-ID Partition Key Routing (Selected)",
          status: "Selected",
          reason: "Scales horizontally across hundreds of partitions while maintaining 100% per-account sequence ordering."
        }
      ]
    }
  },
  {
    id: "case-7",
    num: "7",
    title: "Mobile Payments Economics",
    badge: "2023–2024",
    color: "amber",
    difficulty: "2023–2024 • System Math",
    category: "Interchange & Interchange-Plus Models",
    prompt: `"Evaluate the interchange economics of mobile wallet payments (Apple Pay / Google Pay). Interchange fee is 1.75% + $0.10. Network assessment fee is 0.13%. Tokenization fee is $0.02. On a $50 mobile payment transaction, calculate merchant net payout and bank gross revenue."`,
    legacyCode: {
      python: `# ❌ LEGACY BUGGY CODE: Missing fixed network fees
def calc_interchange(amount):
    # 🐛 BUG: Ignores fixed $0.10 interchange fee and $0.02 tokenization fee!
    return amount * 0.0175`,

      go: `// ❌ LEGACY BUGGY CODE: Missing fixed network fees
func CalcInterchange(amount float64) float64 {
	// 🐛 BUG: Ignores fixed $0.10 interchange fee and $0.02 tokenization fee!
	return amount * 0.0175
}`,

      java: `// ❌ LEGACY BUGGY CODE: Missing fixed network fees
public double calcInterchange(double amount) {
    // 🐛 BUG: Ignores fixed $0.10 interchange fee and $0.02 tokenization fee!
    return amount * 0.0175;
}`
    },
    causes: [
      "Omitted fixed per-transaction fee components ($0.10 interchange + $0.02 tokenization).",
      "Failed to include 0.13% card network assessment fee."
    ],
    solutions: [
      "Total Fee = ($50 * 0.0175 + $0.10) + ($50 * 0.0013) + $0.02 = $0.875 + $0.10 + $0.065 + $0.02 = $1.06.",
      "Merchant Net Payout = $50.00 - $1.06 = $48.94."
    ],
    code: {
      python: `def calculate_mobile_payment_economics(amount: float) -> dict:
    interchange = (amount * 0.0175) + 0.10
    network_assessment = amount * 0.0013
    tokenization_fee = 0.02
    
    total_fee = interchange + network_assessment + tokenization_fee
    merchant_payout = amount - total_fee
    
    return {
        "gross_amount": amount,
        "interchange_fee": round(interchange, 4),
        "network_fee": round(network_assessment, 4),
        "tokenization_fee": tokenization_fee,
        "total_fee": round(total_fee, 2),
        "merchant_payout": round(merchant_payout, 2)
    }`,

      go: `func CalculateMobilePaymentEconomics(amount float64) PaymentEconomics {
	interchange := (amount * 0.0175) + 0.10
	network := amount * 0.0013
	token := 0.02
	total := interchange + network + token
	return PaymentEconomics{
		GrossAmount:    amount,
		InterchangeFee: interchange,
		NetworkFee:     network,
		TotalFee:       total,
		MerchantPayout: amount - total,
	}
}`,

      java: `public PaymentEconomics calculateMobileEconomics(double amount) {
    double interchange = (amount * 0.0175) + 0.10;
    double network = amount * 0.0013;
    double token = 0.02;
    double total = interchange + network + token;
    return new PaymentEconomics(amount, interchange, network, token, total, amount - total);
}`
    },
    explanation: {
      clarifyingQuestions: [
        "What pricing model is used (Interchange-Plus vs Tiered Flat Rate)?",
        "Does the issuer bank or acquiring merchant absorb the tokenization fee?",
        "Are card-not-present (CNP) vs card-present (CP) fee structures differentiated?"
      ],
      hiddenTrap: "Engineers often calculate card fees by multiplying the variable percentage ($1.75\%)$) while omitting fixed per-transaction cents ($\$0.10$ interchange fee and $\$0.02$ Apple/Google Pay tokenization fee). On micro-transactions ($<\$10$), fixed fees constitute over 50% of the total processing cost. Omitting fixed cents distorts revenue modeling by up to 15%.",
      technicalRationale: "Full fee breakdown on a $50 payment:\n1. Interchange Fee: ($50 * 0.0175) + $0.10 = $0.875 + $0.10 = $0.975\n2. Network Assessment Fee: ($50 * 0.0013) = $0.065\n3. Tokenization Fee: $0.02\nTotal Processing Fee = $0.975 + $0.065 + $0.02 = $1.06.\nMerchant Net Payout = $50.00 - $1.06 = $48.94.",
      alternatives: [
        {
          name: "Variable Percentage Only",
          status: "Rejected",
          reason: "Ignores fixed per-transaction cents, underestimating fees on micro-transactions."
        },
        {
          name: "Blended Flat-Rate (e.g. 2.9% + $0.30)",
          status: "Considered",
          reason: "Simplified Stripe-style model, but inaccurate for enterprise interchange-plus bank clearing."
        },
        {
          name: "Full Interchange-Plus Network Pricing (Selected)",
          status: "Selected",
          reason: "Matches Visa/Mastercard interchange schedule specifications with 100% financial accuracy."
        }
      ]
    }
  }
];
