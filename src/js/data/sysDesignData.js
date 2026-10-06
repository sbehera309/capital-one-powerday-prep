// Structured Dataset for System Design Questions (Sorted by Recency: 2025–2026 First)

export const sysDesignQuestions = [
  {
    id: "sys-q1",
    num: "1",
    title: "Real-Time Credit Card Transaction Processing & Instant Fraud Check",
    recency: "2025–2026 • High Frequency",
    color: "blue",
    archBadge: "Distributed Saga & Async Microservices",
    requirements: [
      "Sub-100ms P99 latency for credit card transaction approval.",
      "Dual-write consistency between Aurora Postgres OLTP & ClickHouse OLAP analytics.",
      "Zero lost transactions during total AWS Availability Zone failure."
    ],
    components: [
      { name: "API Gateway (Kong/Envoy)", desc: "TLS termination, OAuth2 token validation, Redis distributed locking for duplicate auth requests." },
      { name: "Auth Microservice", desc: "Stateless Go service validating credit limit, account status, and CVV payload." },
      { name: "Kafka Event Bus", desc: "Multi-AZ partitioned topic (`cc-tx-events`) with partition key = `account_id`." },
      { name: "Debezium CDC + Flink", desc: "Low-latency Change Data Capture streaming Postgres WAL events directly into ClickHouse without DB locks." }
    ]
  },
  {
    id: "sys-q2",
    num: "2",
    title: "High-Throughput POS Card Swipe Authorization & Balance Deduction",
    recency: "2025–2026 • Low Latency",
    color: "cyan",
    archBadge: "In-Memory Redis Lua & ISO 8583",
    requirements: [
      "Process 50,000 POS swipes/sec with sub-20ms P99 response time.",
      "Atomic remaining balance verification to prevent double-spending.",
      "Asynchronous audit log publishing to DynamoDB without blocking POS approval."
    ],
    components: [
      { name: "ISO 8583 Gateway", desc: "Converts legacy terminal ISO messages to gRPC payloads." },
      { name: "Redis Cluster (Lua Script)", desc: "Executes single-threaded atomic balance check & deduction (`EVALSHA`)." },
      { name: "DynamoDB Audit Trail", desc: "Appends immutable transaction logs asynchronously via Kafka." }
    ]
  },
  {
    id: "sys-q3",
    num: "3",
    title: "Multi-Region Active-Active Consensus & Failover",
    recency: "2025–2026 • High Availability",
    color: "emerald",
    archBadge: "CockroachDB Raft Quorum & Route 53 Anycast",
    requirements: [
      "RPO = 0 (Zero transaction data loss) & RTO < 3 seconds during total region failure.",
      "Active-Active write capability in US-East-1 and US-West-2.",
      "Strong serializable isolation across multi-region transactions."
    ],
    components: [
      { name: "Route 53 Anycast DNS", desc: "Routes user requests to nearest healthy region using health probes." },
      { name: "CockroachDB Cluster", desc: "Distributed SQL database using Raft consensus across 5 regional replicas." },
      { name: "Envoy Regional Mesh", desc: "Cross-region TLS mTLS gRPC proxy routing." }
    ]
  },
  {
    id: "sys-q4",
    num: "4",
    title: "Distributed API Gateway Rate Limiter & Sliding Window",
    recency: "2025 • Core Infrastructure",
    color: "teal",
    archBadge: "Redis ZSET Sliding Window",
    requirements: [
      "Enforce 100 requests/minute per partner API key across 200 gateway nodes.",
      "Sub-2ms rate limit check overhead per incoming HTTP request.",
      "Smooth burst handling without sticky thread starvation."
    ],
    components: [
      { name: "Envoy Rate Limit Filter", desc: "Interprets HTTP headers and queries centralized rate limit service." },
      { name: "Redis ZSET Cluster", desc: "Sliding window log storing timestamps as ZSET scores." }
    ]
  },
  {
    id: "sys-q5",
    num: "5",
    title: "Real-Time Fraud Evaluation Engine (Sub-50ms)",
    recency: "Mid 2025 • ML Engineering",
    color: "indigo",
    archBadge: "ONNX Runtime & Redis Feature Store",
    requirements: [
      "Evaluate 120 ML fraud features in sub-50ms window before issuing HTTP authorization response.",
      "Real-time velocity counter aggregation over 1-minute sliding windows.",
      "Fallback to rule engine if ML model inference times out."
    ],
    components: [
      { name: "Feast / Redis Feature Store", desc: "Provides sub-2ms retrieval for 120 pre-computed user fraud features." },
      { name: "ONNX ML Inference Engine", desc: "Lightweight C++ model server running XGBoost fraud models." }
    ]
  },
  {
    id: "sys-q6",
    num: "6",
    title: "Event-Driven Rewards & Loyalty Engine",
    recency: "2024–2025 • Event Driven",
    color: "purple",
    archBadge: "Apache Flink & Stateful Event Streaming",
    requirements: [
      "Process 100,000 reward point calculations/second from card transactions.",
      "Exact-once processing semantics to prevent duplicate point credit allocations.",
      "Real-time tier upgrade notifications (Gold/Platinum) within 500ms of transaction."
    ],
    components: [
      { name: "Apache Flink Stateful Stream", desc: "Computes rolling spend totals using RocksDB state backend." },
      { name: "Kafka Transaction Topic", desc: "Ingests credit card settlement events with idempotency keys." }
    ]
  },
  {
    id: "sys-q7",
    num: "7",
    title: "Mainframe CDC Ingestion Pipeline to AWS S3 & Snowflake",
    recency: "2024 • Data Engineering",
    color: "amber",
    archBadge: "Debezium CDC + Kafka Connect",
    requirements: [
      "Stream DB2 mainframe database changes to AWS S3 data lake with sub-10 second latency.",
      "Zero read lock overhead on mainframe production DB2 database.",
      "Automatic schema evolution handling for mainframe copybook alterations."
    ],
    components: [
      { name: "Debezium CDC Engine", desc: "Reads DB2 transaction logs directly without locking database tables." },
      { name: "Kafka Connect S3 Sink", desc: "Batches CDC records into Parquet format on AWS S3." }
    ]
  },
  {
    id: "sys-q8",
    num: "8",
    title: "High-Availability BNPL Ledger System",
    recency: "2024 • Ledger Systems",
    color: "rose",
    archBadge: "Event Sourcing & Double-Entry Accounting",
    requirements: [
      "Immutable double-entry ledger ensuring Total Assets = Total Liabilities + Equity at all times.",
      "Audit capability to replay ledger state to any historic microsecond timestamp.",
      "High throughput write pipeline supporting 10,000 ledger entries/sec."
    ],
    components: [
      { name: "Immutable Event Store", desc: "Append-only database storing financial journal entries." },
      { name: "CQRS Read Projection Engine", desc: "Builds real-time balance views for fast API reads." }
    ]
  },
  {
    id: "sys-q9",
    num: "9",
    title: "Real-Time Cross-Border FX Settlement System",
    recency: "2024 • Financial Architecture",
    color: "violet",
    archBadge: "ISO 20022 & SWIFT gpi Network",
    requirements: [
      "Settle cross-border payments across 15 currencies with instant rate locking.",
      "Automated liquidity rebalancing between Nostro/Vostro accounts.",
      "Compliance screening against OFAC sanctions lists in sub-30ms."
    ],
    components: [
      { name: "ISO 20022 Payment Gateway", desc: "Formats and validates XML payment messages (pacs.008)." },
      { name: "OFAC Sanctions Screener", desc: "High-speed trie matching for fast AML compliance checks." }
    ]
  }
];

// Interactive SVG Topology Data for All 9 Questions
export const sysSimData = {
  q1: {
    scenarios: [
      {
        name: "Scenario 1: Happy Path - ACH Statement Payment",
        nodes: [
          { title: "Mobile App", sub: "HTTP POST /payments" },
          { title: "API Gateway", sub: "Redis SETNX Lock" },
          { title: "Aurora Postgres", sub: "SCHEDULED_ACH Write" },
          { title: "ClickHouse OLAP", sub: "Debezium CDC Stream" }
        ],
        steps: [
          { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: Mobile Client Payment Submission", protocol: "HTTP/2 POST (TLS 1.3)", headers: "Idempotency-Key: idemp_9921-a482\nAuthorization: Bearer eyJhbGciOi...", body: "{\n  \"account_id\": \"acc_48210\",\n  \"amount\": 450.00,\n  \"method\": \"ACH_CHECKING\"\n}", action: "User clicks 'Pay Balance' on mobile app. Request signed with TLS 1.3 & Idempotency Key.", response: "HTTP 202 Accepted (Processing)", badge: "CLIENT SUBMIT" },
          { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: API Gateway Distributed Lock", protocol: "Redis EVALSHA (Lua)", headers: "SET lock:acc_48210:idemp_9921 EX 10 NX", body: "{\n  \"lock_acquired\": true,\n  \"ttl_ms\": 10000\n}", action: "Gateway checks Redis distributed lock to prevent duplicate payment submissions.", response: "Lock Granted (OK)", badge: "IDEMPOTENT LOCK" },
          { nodeIdx: 2, lineId: "line-1-2", title: "Step 3: Primary Aurora Postgres DB Write", protocol: "gRPC / PostgreSQL Driver", headers: "Txn Isolation: SERIALIZABLE", body: "INSERT INTO payments (id, account_id, amount, status)\nVALUES ('pay_9981', 'acc_48210', 450.00, 'SCHEDULED');", action: "Payment record persisted synchronously to Primary Aurora DB instance.", response: "1 Row Inserted (0.8ms)", badge: "PERSISTED" },
          { nodeIdx: 3, lineId: "line-1-2", title: "Step 4: Asynchronous Debezium CDC Stream to ClickHouse", protocol: "Debezium WAL CDC -> Kafka", headers: "Topic: cc-payments-wal\nPartition: 4", body: "{\n  \"before\": null,\n  \"after\": { \"id\": \"pay_9981\", \"amount\": 450.00 },\n  \"op\": \"c\"\n}", action: "Debezium streams Postgres WAL change event without table locks into ClickHouse.", response: "202 Accepted { txn_id: 'tx_9981' }", badge: "COMPLETED" }
        ]
      }
    ]
  },
  q2: {
    scenarios: [
      {
        name: "Scenario 1: POS Card Swipe Approval (Lua Atomic Check)",
        nodes: [
          { title: "POS Terminal", sub: "ISO 8583 Swipe" },
          { title: "Auth Gateway", sub: "Decrypt PAN" },
          { title: "Redis Primary", sub: "Lua Atomic Script" },
          { title: "DynamoDB Audit", sub: "Async Log" }
        ],
        steps: [
          { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: Merchant Swipes Card for $150", protocol: "ISO 8583 Message", headers: "Merchant-ID: merch_99", body: "{\n  \"amount\": 150.00\n}", action: "POS terminal transmits authorization request for $150 transaction.", response: "Pending Auth", badge: "SWIPED" },
          { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Auth Gateway Decrypts PAN & Routes to Redis", protocol: "gRPC Auth Service", headers: "X-Correlation-ID: auth_77192a", body: "{\n  \"card_id\": \"c_48210\"\n}", action: "Gateway checks cache cluster for card's real-time remaining balance.", response: "Routing to Redis", badge: "ROUTED" },
          { nodeIdx: 2, lineId: "line-1-2", title: "Step 3: Single-Threaded Redis Lua Script Execution", protocol: "Redis EVALSHA (Atomic)", headers: "Script: check_and_decr.lua", body: "{\n  \"approved\": true\n}", action: "Redis executes Lua script: 400 + 150 <= 1000 -> Updates spend to $550 atomically.", response: "APPROVED (00)", badge: "APPROVED" },
          { nodeIdx: 3, lineId: "line-1-2", title: "Step 4: Async Audit Event Published to DynamoDB", protocol: "AWS SDK DynamoDB", headers: "Table: auth_events", body: "{\n  \"decision\": \"APPROVED\"\n}", action: "Approval log written asynchronously to DynamoDB without blocking ISO response.", response: "200 OK (ISO Resp: 00)", badge: "AUDITED" }
        ]
      }
    ]
  },
  q3: {
    scenarios: [
      {
        name: "Scenario 1: Multi-Region Active-Active Consensus & Failover",
        nodes: [
          { title: "Route 53 Anycast", sub: "Traffic to us-east-1" },
          { title: "us-east-1 Cluster", sub: "Primary Deposit" },
          { title: "CockroachDB Raft", sub: "Cross-Region Sync" },
          { title: "Region Blackout", sub: "DNS Failover to us-west-2" }
        ],
        steps: [
          { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: User Deposited $500 in US-East-1", protocol: "HTTP POST /v1/transactions", headers: "Geo: US-East", body: "{\n  \"amount\": 500.00\n}", action: "Route 53 routes request to nearest US-East data center.", response: "Processing...", badge: "US-EAST-1" },
          { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Raft Consensus Synchronizes Across Regions", protocol: "Raft Consensus", headers: "Quorum: 3/5 Replicas Ack", body: "{\n  \"us_east_ack\": true\n}", action: "Raft consensus writes transaction synchronously to US-East & US-West nodes.", response: "Raft Committed", badge: "RAFT SYNC" },
          { nodeIdx: 2, lineId: "line-1-2", title: "Step 3: Total AWS US-East-1 Regional Outage Occurs!", protocol: "Route 53 Health Check", headers: "us-east-1: UNHEALTHY", body: "{\n  \"outage\": true\n}", action: "AWS US-East-1 loses total power. Health check fails after 2 consecutive probes.", response: "Health Check Failed", badge: "OUTAGE ALERT" },
          { nodeIdx: 3, lineId: "line-1-2", title: "Step 4: Route 53 DNS Failover to US-West-2 in 2.8s", protocol: "DNS Anycast Failover", headers: "Active: us-west-2", body: "{\n  \"recovered\": true\n}", action: "Route 53 shifts 100% traffic to US-West-2. Zero transaction data lost!", response: "100% Recovered (2.8s)", badge: "ZERO RPO" }
        ]
      }
    ]
  },
  q4: {
    scenarios: [
      {
        name: "Scenario 1: Under Quota Request (200 OK)",
        nodes: [
          { title: "Partner App", sub: "HTTP Request" },
          { title: "Envoy Gateway", sub: "Extract API Key" },
          { title: "Redis ZSET", sub: "Sliding Window" },
          { title: "Core Banking", sub: "Process Request" }
        ],
        steps: [
          { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: Partner API Request", protocol: "HTTP/1.1 GET /v1/accounts", headers: "X-API-Key: key_partner_99", body: "{}", action: "Partner app sends GET request to core banking API.", response: "Pending...", badge: "REQUEST" },
          { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Envoy Gateway Key Check", protocol: "Envoy Filter Engine", headers: "Key: key_partner_99", body: "{\n  \"client_id\": \"client_fintech_99\",\n  \"limit_per_min\": 100\n}", action: "Envoy extracts client ID and fetches rate limit quota profile.", response: "Routing to Redis Limiter", badge: "PROFILE OK" },
          { nodeIdx: 2, lineId: "line-1-2", title: "Step 3: Redis ZSET Sliding Window Counter", protocol: "Redis Pipeline", headers: "ZSET-Key: rate:client_fintech_99", body: "{\n  \"active_count_in_window\": 42,\n  \"limit\": 100,\n  \"allowed\": true\n}", action: "Redis purges timestamps older than now - 60s. Count = 42 < 100 limit.", response: "Allowed (42/100)", badge: "ZSET PASS" },
          { nodeIdx: 3, lineId: "line-1-2", title: "Step 4: Core Banking Service Responds with 200 OK", protocol: "gRPC Core Banking", headers: "X-RateLimit-Remaining: 57", body: "{\n  \"status\": \"SUCCESS\"\n}", action: "Core banking service returns account data with remaining quota headers.", response: "200 OK (Remaining: 57)", badge: "200 OK" }
        ]
      }
    ]
  },
  q5: {
    scenarios: [
      {
        name: "Scenario 1: Real-Time Fraud Evaluation (Sub-50ms)",
        nodes: [
          { title: "Auth Pipeline", sub: "Transaction Event" },
          { title: "Feast Feature Store", sub: "Fetch 120 Features" },
          { title: "ONNX ML Engine", sub: "XGBoost Fraud Score" },
          { title: "Decision Service", sub: "Approve / Decline" }
        ],
        steps: [
          { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: Auth Request Arrives", protocol: "gRPC Auth Event", headers: "User-ID: u_8819", body: "{\n  \"amount\": 1200.00\n}", action: "Auth pipeline sends user ID and transaction amount for evaluation.", response: "Evaluating...", badge: "EVALUATE" },
          { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Redis Feature Store Lookup", protocol: "Redis MGET (sub-2ms)", headers: "Features: 120 Data Points", body: "{\n  \"velocity_1m\": 4,\n  \"device_risk\": 0.91\n}", action: "Fetches user's 1-minute transaction velocity and device trust score.", response: "Features Retrived", badge: "FEATURES LOADED" },
          { nodeIdx: 2, lineId: "line-1-2", title: "Step 3: ONNX C++ Model Inference Engine", protocol: "ONNX Runtime C++ API", headers: "Model: fraud_xgboost_v4.onnx", body: "{\n  \"fraud_score\": 0.88\n}", action: "Runs XGBoost tree evaluation in 4.2ms. Output fraud score = 0.88.", response: "Score Calculated", badge: "ML SCORED" },
          { nodeIdx: 3, lineId: "line-1-2", title: "Step 4: Decision Service Triggers Step-Up Auth", protocol: "Rule Engine", headers: "Threshold: 0.75", body: "{\n  \"decision\": \"CHALLENGE_MFA\"\n}", action: "Fraud score > 0.75 threshold. Triggers SMS MFA prompt to cardholder.", response: "200 OK (MFA Sent)", badge: "DECISION ISSUED" }
        ]
      }
    ]
  },
  q6: {
    scenarios: [
      {
        name: "Scenario 1: Apache Flink Stateful Rewards Aggregation",
        nodes: [
          { title: "Card Settlement", sub: "Kafka Producer" },
          { title: "Flink Job", sub: "RocksDB State Window" },
          { title: "Tier Engine", sub: "Check Gold Status" },
          { title: "Push Notification", sub: "APNS / FCM Alert" }
        ],
        steps: [
          { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: Settlement Event Published to Kafka", protocol: "Kafka Event", headers: "Topic: card-settlements", body: "{\n  \"amount\": 350.00\n}", action: "Settlement engine posts completed $350 transaction event.", response: "Event Queued", badge: "EVENT PUBLISHED" },
          { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Flink Computes Rolling Monthly Spend", protocol: "Apache Flink Operator", headers: "State: RocksDB", body: "{\n  \"prev_spend\": 9700.00,\n  \"new_spend\": 10050.00\n}", action: "Flink updates user's rolling 30-day spend total to $10,050.", response: "Window Updated", badge: "STATE UPDATED" },
          { nodeIdx: 2, lineId: "line-1-2", title: "Step 3: Tier Upgrade Triggered ($10,000 Threshold)", protocol: "Rule Evaluator", headers: "Tier: Gold ($10k+)", body: "{\n  \"unlocked_tier\": \"GOLD\"\n}", action: "User crosses $10,000 threshold. Tier engine grants Gold status.", response: "Tier Upgraded", badge: "GOLD UNLOCKED" },
          { nodeIdx: 3, lineId: "line-1-2", title: "Step 4: Real-Time Mobile Push Notification", protocol: "Apple APNS / Google FCM", headers: "DeviceToken: tok_99a", body: "{\n  \"title\": \"Congratulations! You unlocked Gold Status 🎉\"\n}", action: "Push notification delivered to user's smartphone within 380ms.", response: "Delivered (200)", badge: "NOTIFICATION SENT" }
        ]
      }
    ]
  },
  q7: {
    scenarios: [
      {
        name: "Scenario 1: Debezium CDC Mainframe Ingestion",
        nodes: [
          { title: "Mainframe DB2", sub: "WAL Change Log" },
          { title: "Debezium Connect", sub: "Non-Blocking CDC" },
          { title: "Kafka Cluster", sub: "Parquet Converter" },
          { title: "AWS S3 / Snowflake", sub: "Analytic Query" }
        ],
        steps: [
          { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: Customer Account Balance Updated on DB2", protocol: "Mainframe DB2 Commit", headers: "Table: ACCT_BAL", body: "{\n  \"acct_id\": \"99182\",\n  \"bal\": 5400.00\n}", action: "Mainframe transaction updates DB2 record. Write-Ahead Log entry emitted.", response: "DB2 Committed", badge: "WAL EMITTED" },
          { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Debezium Captures WAL Delta without Locks", protocol: "Debezium Connector", headers: "Source: db2_cdc_connector", body: "{\n  \"op\": \"u\",\n  \"before\": 4900.00,\n  \"after\": 5400.00\n}", action: "Debezium reads DB2 transaction log without locking active database tables.", response: "CDC Captured", badge: "CDC READ" },
          { nodeIdx: 2, lineId: "line-1-2", title: "Step 3: Kafka Connect Batches Records to Parquet", protocol: "Kafka Connect S3 Sink", headers: "Format: Apache Parquet", body: "{\n  \"batch_size_mb\": 64,\n  \"compression\": \"SNAPPY\"\n}", action: "Kafka Connect aggregates CDC records into 64MB Parquet files.", response: "Parquet Generated", badge: "BATCH CREATED" },
          { nodeIdx: 4, lineId: "line-1-2", title: "Step 4: AWS S3 Auto-Ingest into Snowflake Lake", protocol: "Snowpipe Auto-Ingest", headers: "Target: SNOWFLAKE_RAW", body: "{\n  \"rows_inserted\": 10000\n}", action: "Snowpipe detects new S3 file and loads account delta into Snowflake analytical warehouse.", response: "Snowflake Ingested", badge: "LAKE LOADED" }
        ]
      }
    ]
  },
  q8: {
    scenarios: [
      {
        name: "Scenario 1: CQRS Event Sourcing Ledger Write",
        nodes: [
          { title: "BNPL Checkout", sub: "Create Order" },
          { title: "Ledger Command API", sub: "Validate Assets = Liab" },
          { title: "Immutable Event Store", sub: "Append Entry" },
          { title: "CQRS Read Projection", sub: "Update Balance View" }
        ],
        steps: [
          { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: Order Created for $200 BNPL Loan", protocol: "HTTP POST /v1/ledger", headers: "Product: BNPL_4_PAY", body: "{\n  \"order_id\": \"ord_5521\",\n  \"amount\": 200.00\n}", action: "User initiates 4-installment BNPL loan for $200 online purchase.", response: "Processing...", badge: "LOAN REQUEST" },
          { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Double-Entry Balance Verification", protocol: "Ledger Validation Engine", headers: "Check: Debit == Credit", body: "{\n  \"debit_loans_receivable\": 200.00,\n  \"credit_merchant_payable\": 200.00\n}", action: "Command service validates balanced double-entry transaction record.", response: "Balanced (0.00 Diff)", badge: "ACCOUNTING VERIFIED" },
          { nodeIdx: 2, lineId: "line-1-2", title: "Step 3: Immutable Entry Appended to Event Store", protocol: "Append-Only Postgres", headers: "Sequence_Num: 994812", body: "{\n  \"entry_id\": \"ent_8829\",\n  \"hash\": \"a8f9c41e...\"\n}", action: "Ledger entry appended to immutable event log with cryptographic chain hash.", response: "Event Persisted", badge: "LEDGER SEALED" },
          { nodeIdx: 3, lineId: "line-1-2", title: "Step 4: CQRS Read Projection Asynchronously Updated", protocol: "Kafka -> Read DB View", headers: "View: Merchant_Balance_Summary", body: "{\n  \"merchant_id\": \"m_9921\",\n  \"pending_payout\": 200.00\n}", action: "Read projection updates merchant's queryable balance view within 45ms.", response: "Read Model Synced", badge: "VIEW PROJECTED" }
        ]
      }
    ]
  },
  q9: {
    scenarios: [
      {
        name: "Scenario 1: Cross-Border FX Settlement Pipeline",
        nodes: [
          { title: "ISO Gateway", sub: "pacs.008 Payment" },
          { title: "OFAC Screener", sub: "Trie Sanction Match" },
          { title: "FX Rate Engine", sub: "Lock USD/EUR Rate" },
          { title: "SWIFT gpi", sub: "Nostro Settlement" }
        ],
        steps: [
          { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: Cross-Border Payment Instruction Received", protocol: "ISO 20022 XML Message", headers: "Message: pacs.008.001.08", body: "{\n  \"instructed_amount\": 10000.00,\n  \"currency\": \"USD\",\n  \"target_curr\": \"EUR\"\n}", action: "Originating bank submits cross-border transfer instruction.", response: "pacs.008 Received", badge: "ISO PARSED" },
          { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Sub-30ms OFAC Sanctions Screening", protocol: "Aho-Corasick Trie Matcher", headers: "List: OFAC_SDN_2026", body: "{\n  \"sanction_match\": false,\n  \"confidence\": 0.00\n}", action: "High-speed screener checks sender and receiver names against sanctions database.", response: "CLEARED (No Match)", badge: "AML CLEARED" },
          { nodeIdx: 2, lineId: "line-1-2", title: "Step 3: FX Rate Lock (USD -> EUR @ 0.9215)", protocol: "FX Rate Service", headers: "Lock_ID: fx_lock_8871", body: "{\n  \"locked_rate\": 0.9215,\n  \"eur_amount\": 9215.00,\n  \"ttl_sec\": 10\n}", action: "Rate engine locks 0.9215 exchange rate for 10 seconds to execute conversion.", response: "Rate Locked", badge: "FX LOCKED" },
          { nodeIdx: 3, lineId: "line-1-2", title: "Step 4: Settlement Execution via SWIFT gpi Network", protocol: "SWIFT gpi Tracker API", headers: "UETR: e94812a-33f1", body: "{\n  \"status\": \"SETTLED\",\n  \"vostro_debited\": 9215.00\n}", action: "Nostro account debited and funds credited to beneficiary bank in Frankfurt.", response: "200 OK (Settled)", badge: "SWIFT SETTLED" }
        ]
      }
    ]
  }
};
