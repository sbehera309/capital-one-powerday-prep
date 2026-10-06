// Structured Dataset for System Design Questions (Sorted by Recency: 2025–2026 First)
// Strictly Aligned to AWS Cloud-Native Architecture & Enterprise Industry Standards

export const sysDesignQuestions = [
  {
    id: "sys-q1",
    num: "1",
    title: "Real-Time Credit Card Transaction Processing & Instant Fraud Check",
    recency: "2025–2026 • High Frequency",
    color: "blue",
    archBadge: "AWS 5-Tier Distributed Saga & Async Microservices",
    prompt: "Design a real-time credit card transaction processing platform for Capital One. It must approve payments in sub-100ms P99 latency, support high-volume ACH statement settlements, and maintain dual-write consistency between transactional OLTP storage and OLAP analytical warehouses without database locks.",
    requirements: [
      "Sub-100ms P99 latency for credit card transaction approval.",
      "Dual-write consistency between Amazon Aurora Postgres OLTP & ClickHouse / Redshift OLAP analytics.",
      "Zero lost transactions during total AWS Availability Zone failure."
    ],
    tradeoffs: [
      {
        topic: "AWS Fargate (Containers) vs AWS Lambda (Serverless)",
        decision: "AWS Fargate ECS Containers Selected",
        rationale: "Payment authorization requires warm database connection pools (HikariCP / PgBouncer) to Amazon Aurora Postgres. AWS Lambda cold starts (100ms–500ms) would violate sub-100ms P99 SLAs. Fargate containers maintain persistent gRPC / TCP connections, eliminating connection setup overhead per payment request."
      },
      {
        topic: "Debezium CDC + Amazon MSK vs Application Dual-Writing",
        decision: "Debezium Change Data Capture Selected",
        rationale: "Dual-writing directly to Postgres and ClickHouse from the microservice layer creates partial failure windows (e.g. Postgres succeeds, ClickHouse times out) and doubles network hop latency. Debezium CDC reads the Postgres Write-Ahead Log (WAL) asynchronously without locking database tables, guaranteeing 100% eventual consistency without impacting payment approval latency."
      },
      {
        topic: "Amazon Aurora Postgres (OLTP) vs Amazon DynamoDB",
        decision: "Amazon Aurora PostgreSQL Selected for OLTP",
        rationale: "ACH statement settlements and core ledger accounting require ACID transactions and relational constraints (SERIALIZABLE isolation, multi-table Foreign Keys). DynamoDB is single-row ACID or eventual-consistent, making multi-account ledger balancing harder to audit."
      }
    ],
    components: [
      { name: "Amazon API Gateway", desc: "TLS 1.3 termination, WAF rules, OAuth2 validation, and Amazon ElastiCache distributed locking." },
      { name: "AWS Fargate (Payments Microservice)", desc: "Stateless ECS Go container executing business validation, fraud check orchestration, and SQL statements." },
      { name: "Amazon Aurora PostgreSQL (OLTP)", desc: "Multi-AZ primary database writing payment records with SERIALIZABLE isolation and WAL generation." },
      { name: "Debezium CDC + Amazon MSK + ClickHouse", desc: "Change Data Capture streaming Postgres WAL change events directly into ClickHouse without OLTP table locks." }
    ]
  },
  {
    id: "sys-q2",
    num: "2",
    title: "High-Throughput POS Card Swipe Authorization & Balance Deduction",
    recency: "2025–2026 • Low Latency",
    color: "cyan",
    archBadge: "AWS In-Memory ElastiCache Redis & ISO 8583",
    prompt: "Design a high-throughput POS card swipe authorization system capable of handling 50,000 swipes/sec with sub-20ms P99 response time. Prevent double-spending on remaining balances using atomic in-memory scripts and publish asynchronous audit events.",
    requirements: [
      "Process 50,000 POS swipes/sec with sub-20ms P99 response time.",
      "Atomic remaining balance verification to prevent double-spending.",
      "Asynchronous audit log publishing to Amazon DynamoDB without blocking POS approval."
    ],
    tradeoffs: [
      {
        topic: "Amazon ElastiCache Redis Lua Scripts vs Relational DB Lock",
        decision: "Redis Single-Threaded Lua Script (EVALSHA) Selected",
        rationale: "Relational database row locks (`SELECT ... FOR UPDATE`) at 50,000 QPS cause severe lock contention and DB thread pool exhaustion. Redis executes Lua scripts single-threadedly in memory, performing atomic remaining balance checks and deductions in <1ms without locks."
      },
      {
        topic: "AWS Network Load Balancer (NLB) vs Application Load Balancer (ALB)",
        decision: "AWS NLB Selected for POS Ingress",
        rationale: "POS terminals communicate via low-level ISO 8583 TCP socket connections. AWS NLB operates at Layer 4, handling tens of millions of concurrent TCP/gRPC connections with ultra-low sub-millisecond latency compared to Layer 7 ALB HTTP parsing overhead."
      },
      {
        topic: "Amazon DynamoDB Async Audit Stream vs Synchronous Write",
        decision: "Amazon MSK + DynamoDB Async Audit Selected",
        rationale: "Writing audit logs synchronously during the POS authorization path adds 10-15ms of disk I/O latency. Publishing authorization decision events to Amazon MSK streams logs asynchronously into DynamoDB without delaying the ISO 8583 merchant response."
      }
    ],
    components: [
      { name: "AWS Network Load Balancer (NLB)", desc: "High-throughput TCP ingress balancing 50,000 ISO 8583 requests/sec." },
      { name: "AWS Fargate (POS Auth Microservice)", desc: "High-concurrency Go container managing ISO parsing and Redis cluster queries." },
      { name: "Amazon ElastiCache Redis Cluster", desc: "Executes single-threaded atomic balance check & deduction using Lua scripts (`EVALSHA`)." },
      { name: "Amazon DynamoDB + Amazon MSK", desc: "Appends immutable audit logs asynchronously via Kafka streams." }
    ]
  },
  {
    id: "sys-q3",
    num: "3",
    title: "Multi-Region Active-Active Consensus & Failover",
    recency: "2025–2026 • High Availability",
    color: "emerald",
    archBadge: "AWS Route 53 Anycast & Multi-Region Compute",
    prompt: "Design a multi-region active-active core banking database architecture spanning AWS us-east-1 and us-west-2. Achieve zero transaction data loss (RPO = 0) and automated failover in under 3 seconds (RTO < 3s) during total regional blackout.",
    requirements: [
      "RPO = 0 (Zero transaction data loss) & RTO < 3 seconds during total AWS region failure.",
      "Active-Active write capability in AWS us-east-1 and us-west-2.",
      "Strong serializable isolation across multi-region transactions."
    ],
    tradeoffs: [
      {
        topic: "Raft Consensus Multi-Region DB vs Asynchronous Primary-Replica",
        decision: "Multi-Region Raft Quorum Database Selected",
        rationale: "Asynchronous DB replication across regions introduces data loss windows during unannounced regional outages (RPO > 0). Raft consensus requires a majority quorum (3/5 replicas across 3 availability zones / 2 regions) to acknowledge writes before committing, guaranteeing RPO = 0."
      },
      {
        topic: "AWS Route 53 Anycast Latency Routing vs Static DNS",
        decision: "AWS Route 53 Latency Routing with Health Probes Selected",
        rationale: "Route 53 latency routing directs users to the geographically nearest AWS region under normal conditions. When health probes detect 2 consecutive failures in us-east-1, Route 53 shifts 100% traffic to us-west-2 in <3 seconds without human intervention."
      }
    ],
    components: [
      { name: "AWS Route 53 Anycast DNS", desc: "Latency-based routing with automated health check probes to nearest active region." },
      { name: "AWS Fargate Regional Gateway", desc: "Active-Active compute clusters running containerized microservices in us-east-1 and us-west-2." },
      { name: "CockroachDB / Aurora Global Database", desc: "Multi-region Raft consensus / storage engine with zero data loss replication." },
      { name: "AWS App Mesh / Envoy", desc: "Cross-region mTLS gRPC service mesh proxy." }
    ]
  },
  {
    id: "sys-q4",
    num: "4",
    title: "Distributed API Gateway Rate Limiter & Sliding Window",
    recency: "2025 • Core Infrastructure",
    color: "teal",
    archBadge: "Amazon ElastiCache Redis ZSET Sliding Window",
    prompt: "Design a distributed API Gateway rate limiter enforcing 100 requests/minute per partner API key across 200 stateless gateway nodes with sub-2ms overhead per check and smooth burst handling.",
    requirements: [
      "Enforce 100 requests/minute per partner API key across 200 gateway nodes.",
      "Sub-2ms rate limit check overhead per incoming HTTP request.",
      "Smooth burst handling without sticky thread starvation."
    ],
    tradeoffs: [
      {
        topic: "Redis ZSET Sliding Window vs Fixed Window Counter",
        decision: "ElastiCache Redis Sorted Set (ZSET) Selected",
        rationale: "Fixed-window rate limiters suffer from edge-of-window traffic spikes (e.g. 100 requests at 00:59 and 100 requests at 01:01 allows 200 requests in 2 seconds). The Redis ZSET sliding window logs timestamp scores and purges elements older than now - 60s, enforcing strict rolling 60-second limit compliance."
      },
      {
        topic: "Centralized Redis Cluster vs Local In-Memory Gateway Caching",
        decision: "Centralized ElastiCache Redis Cluster Selected",
        rationale: "Local in-memory counters across 200 gateway nodes allow clients to bypass rate limits by hitting different gateway instances behind round-robin load balancers. A centralized ElastiCache Redis cluster provides a single global source of truth."
      }
    ],
    components: [
      { name: "Amazon API Gateway / Envoy", desc: "Interprets HTTP headers and queries centralized rate limit service." },
      { name: "AWS Fargate (Rate Limiter Microservice)", desc: "High-performance rate limit evaluation container." },
      { name: "Amazon ElastiCache Redis ZSET", desc: "Sliding window log storing request timestamps as ZSET scores." }
    ]
  },
  {
    id: "sys-q5",
    num: "5",
    title: "Real-Time Fraud Evaluation Engine (Sub-50ms)",
    recency: "Mid 2025 • ML Engineering",
    color: "indigo",
    archBadge: "AWS SageMaker / ONNX & ElastiCache Feature Store",
    prompt: "Design a real-time fraud scoring engine evaluating 120 ML features in sub-50ms window before issuing HTTP authorization. Integrate low-latency feature stores and ONNX C++ XGBoost inference with fallback rule processing.",
    requirements: [
      "Evaluate 120 ML fraud features in sub-50ms window before issuing HTTP authorization response.",
      "Real-time velocity counter aggregation over 1-minute sliding windows.",
      "Fallback to rule engine if ML model inference times out."
    ],
    tradeoffs: [
      {
        topic: "Amazon ElastiCache (Feast Feature Store) vs Relational Database Joins",
        decision: "Amazon ElastiCache Redis Feature Store Selected",
        rationale: "Executing 120 SQL joins across user transaction history tables takes 30ms–100ms, consuming the entire SLA budget. Feast backed by ElastiCache Redis stores pre-computed features in memory, returning 120 data points via a single `MGET` call in sub-2ms."
      },
      {
        topic: "ONNX Runtime C++ Server vs Python Flask ML Inference",
        decision: "ONNX C++ Model Execution Engine Selected",
        rationale: "Python ML servers suffer from Global Interpreter Lock (GIL) overhead and memory garbage collection pauses (45ms+ latency). Compiling XGBoost models to ONNX format executed via C++ containers achieves predictable 4.2ms model evaluation."
      }
    ],
    components: [
      { name: "AWS Fargate (Fraud Orchestrator)", desc: "Coordinates sub-50ms parallel feature fetching and ML inference." },
      { name: "Feast / Amazon ElastiCache Redis", desc: "Provides sub-2ms retrieval for 120 pre-computed user fraud features." },
      { name: "ONNX C++ ML Inference Server", desc: "Lightweight container running XGBoost fraud evaluation models." }
    ]
  },
  {
    id: "sys-q6",
    num: "6",
    title: "Event-Driven Rewards & Loyalty Engine",
    recency: "2024–2025 • Event Driven",
    color: "purple",
    archBadge: "Amazon MSK & AWS EKS Apache Flink Stream",
    prompt: "Design an event-driven rewards and loyalty platform processing 100,000 credit card transaction settlements/sec. Ensure exactly-once processing semantics to prevent duplicate points and trigger instant mobile push alerts upon tier promotion.",
    requirements: [
      "Process 100,000 reward point calculations/second from card transactions.",
      "Exact-once processing semantics to prevent duplicate point credit allocations.",
      "Real-time tier upgrade notifications (Gold/Platinum) within 500ms of transaction."
    ],
    tradeoffs: [
      {
        topic: "Apache Flink Stateful Streaming vs Traditional Nightly Cron Jobs",
        decision: "AWS EKS Apache Flink Stateful Stream Selected",
        rationale: "Nightly batch cron jobs leave users waiting 24 hours to see point balances or tier promotions. Apache Flink maintains in-memory state in RocksDB, computing rolling spend totals per transaction in real-time with sub-second tier promotion push alerts."
      },
      {
        topic: "Amazon MSK Partition Key = account_id vs Round-Robin Partitioning",
        decision: "Explicit account_id Partition Key Selected",
        rationale: "Round-robin partitioning sends transactions for the same account to different Flink workers, causing race conditions in point balances. Partitioning by `account_id` guarantees all events for a given account land on the exact same Flink task worker in sequential order."
      }
    ],
    components: [
      { name: "Amazon MSK (Managed Kafka)", desc: "Ingests credit card settlement events with partition key = `account_id`." },
      { name: "AWS EKS / Fargate (Apache Flink)", desc: "Stateful stream processing computing rolling 30-day spend with RocksDB state." },
      { name: "Amazon SNS / APNS / FCM", desc: "Delivers real-time push notifications to smartphone clients." }
    ]
  },
  {
    id: "sys-q7",
    num: "7",
    title: "Mainframe CDC Ingestion Pipeline to AWS S3 & Snowflake",
    recency: "2024 • Data Engineering",
    color: "amber",
    archBadge: "Debezium CDC + Amazon MSK + AWS S3",
    prompt: "Design an automated Change Data Capture (CDC) streaming pipeline from DB2 mainframe legacy databases to AWS S3 and Snowflake analytical data lakehouses with sub-10 second latency and zero read-locking overhead on mainframe DB2 production tables.",
    requirements: [
      "Stream DB2 mainframe database changes to AWS S3 data lake with sub-10 second latency.",
      "Zero read lock overhead on mainframe production DB2 database.",
      "Automatic schema evolution handling for mainframe copybook alterations."
    ],
    tradeoffs: [
      {
        topic: "Debezium CDC + AWS Direct Connect vs Batch SQL Queries",
        decision: "Debezium Change Data Capture Selected",
        rationale: "Executing `SELECT * FROM DB2_TABLE` batch queries on production mainframes incurs heavy CPU MIPS costs and table locks. Debezium streams Write-Ahead Logs (WAL) over AWS Direct Connect without impacting production mainframe queries."
      },
      {
        topic: "Apache Parquet Columnar Storage vs JSON/CSV Format",
        decision: "Snappy Parquet Format on Amazon S3 Selected",
        rationale: "JSON and CSV formats require scanning full files line-by-line during analytics queries. Snappy Parquet is a compressed columnar format, reducing S3 storage costs by 80% and enabling Snowflake/Athena to execute column-filtered queries 10x faster."
      }
    ],
    components: [
      { name: "AWS Direct Connect + Debezium CDC", desc: "Reads DB2 transaction logs directly without locking database tables." },
      { name: "Amazon MSK + Kafka Connect S3 Sink", desc: "Batches CDC records into Snappy-compressed Parquet format on AWS S3." },
      { name: "Amazon S3 Data Lake + Snowflake", desc: "Immutable storage on S3 (`s3://c1-lake-raw`) auto-ingested into Snowflake via Snowpipe." }
    ]
  },
  {
    id: "sys-q8",
    num: "8",
    title: "High-Availability BNPL Ledger System",
    recency: "2024 • Ledger Systems",
    color: "rose",
    archBadge: "AWS CQRS Event Sourcing Ledger",
    prompt: "Design an immutable double-entry accounting ledger system for Buy-Now-Pay-Later (BNPL) loans supporting 10,000 writes/sec, cryptographic event stream auditing, and CQRS read projections for instant merchant balance queries.",
    requirements: [
      "Immutable double-entry ledger ensuring Total Assets = Total Liabilities + Equity at all times.",
      "Audit capability to replay ledger state to any historic microsecond timestamp.",
      "High throughput write pipeline supporting 10,000 ledger entries/sec."
    ],
    tradeoffs: [
      {
        topic: "Event Sourcing + CQRS Pattern vs Standard Database CRUD",
        decision: "Event Sourcing with CQRS Projections Selected",
        rationale: "CRUD update operations (`UPDATE account SET balance = balance - 100`) destroy historic audit trails and create lock contention. Event sourcing stores an immutable append-only journal of financial events, allowing full ledger replay. CQRS projects balances into Amazon OpenSearch for instant read queries."
      },
      {
        topic: "Double-Entry Accounting Constraint Validation",
        decision: "Synchronous Double-Entry Validation Selected",
        rationale: "Every transaction must balance (`Debits == Credits`) before being sealed into the immutable ledger, guaranteeing zero accounting discrepancy."
      }
    ],
    components: [
      { name: "AWS Fargate (Ledger Command API)", desc: "Spring Boot microservice verifying double-entry constraints." },
      { name: "Amazon Aurora PostgreSQL (Event Store)", desc: "Append-only database storing journal entries with cryptographic hashes." },
      { name: "Amazon OpenSearch / DynamoDB", desc: "CQRS read projection building queryable balance views." }
    ]
  },
  {
    id: "sys-q9",
    num: "9",
    title: "Real-Time Cross-Border FX Settlement System",
    recency: "2024 • Financial Architecture",
    color: "violet",
    archBadge: "AWS ISO 20022 & SWIFT gpi Pipeline",
    prompt: "Design an international cross-border FX payment settlement platform supporting ISO 20022 XML standards, sub-30ms OFAC sanctions screening, automated 10-second exchange rate locking, and SWIFT gpi Nostro/Vostro settlement.",
    requirements: [
      "Settle cross-border payments across 15 currencies with instant rate locking.",
      "Automated liquidity rebalancing between Nostro/Vostro accounts.",
      "Compliance screening against OFAC sanctions lists in sub-30ms."
    ],
    tradeoffs: [
      {
        topic: "Aho-Corasick Trie Matcher vs Relational Database LIKE Queries",
        decision: "Aho-Corasick In-Memory Trie Screener Selected",
        rationale: "Fuzzy SQL `LIKE` queries against millions of sanctioned names in OFAC database take 200ms+. The Aho-Corasick trie data structure evaluates all SDN list names in a single sub-30ms pass in memory."
      },
      {
        topic: "10-Second Rate Lock in ElastiCache Redis vs Dynamic Execution",
        decision: "ElastiCache Redis TTL Rate Lock Selected",
        rationale: "Executing cross-border transfers without locking exchange rates exposes the bank to foreign exchange rate market volatility during SWIFT settlement processing."
      }
    ],
    components: [
      { name: "Amazon API Gateway (ISO Ingress)", desc: "Validates pacs.008 XML payment messages." },
      { name: "AWS Fargate (Compliance Screener)", desc: "Executes sub-30ms AML and OFAC sanctions trie matching." },
      { name: "Amazon ElastiCache Redis (FX Rate Engine)", desc: "Locks USD/EUR exchange rate for 10 seconds." },
      { name: "Amazon MSK + SWIFT gpi Network", desc: "Executes Nostro account settlement and updates SWIFT tracker." }
    ]
  }
];

// Interactive SVG Topology Data for All 9 Questions (AWS 5-Tier Architectural Pipeline)
export const sysSimData = {
  q1: {
    scenarios: [
      {
        name: "Scenario 1: Happy Path - ACH Statement Payment",
        nodes: [
          { title: "1. Mobile App Client", sub: "HTTP POST /payments (TLS 1.3)" },
          { title: "2. Amazon API Gateway", sub: "TLS 1.3 WAF & ElastiCache Distributed Lock" },
          { title: "3. AWS Fargate (Payments API Service)", sub: "Stateless Microservice Business Logic & Auth" },
          { title: "4. Amazon Aurora PostgreSQL (OLTP DB)", sub: "Multi-AZ Primary DB Write & WAL Emission" },
          { title: "5. ClickHouse OLAP (Debezium CDC + MSK)", sub: "Asynchronous Lockless CDC Analytics Stream" }
        ],
        steps: [
          { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: Mobile Client Payment Submission", protocol: "HTTP/2 POST (TLS 1.3)", headers: "Idempotency-Key: idemp_9921-a482\nAuthorization: Bearer eyJhbGciOi...", body: "{\n  \"account_id\": \"acc_48210\",\n  \"amount\": 450.00,\n  \"method\": \"ACH_CHECKING\"\n}", action: "User clicks 'Pay Balance' on mobile app. Request signed with TLS 1.3 & Idempotency Key.", response: "HTTP 202 Accepted (Processing)", badge: "CLIENT SUBMIT" },
          { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Amazon API Gateway Lock Check", protocol: "Amazon ElastiCache EVALSHA (Lua)", headers: "SET lock:acc_48210:idemp_9921 EX 10 NX", body: "{\n  \"lock_acquired\": true,\n  \"ttl_ms\": 10000\n}", action: "API Gateway verifies ElastiCache Redis distributed lock to block duplicate payments.", response: "Lock Granted (OK)", badge: "IDEMPOTENT LOCK" },
          { nodeIdx: 2, lineId: "line-2-3", title: "Step 3: AWS Fargate Payments Service Processing", protocol: "AWS ECS Fargate (Go Container)", headers: "X-Correlation-ID: tx_9981-proc", body: "{\n  \"account_status\": \"ACTIVE\",\n  \"validated\": true\n}", action: "AWS Fargate microservice container evaluates business logic and prepares SQL transaction.", response: "Validated (0.4ms)", badge: "SERVICE VALIDATED" },
          { nodeIdx: 3, lineId: "line-3-4", title: "Step 4: Primary Amazon Aurora Postgres DB Write", protocol: "gRPC / PostgreSQL Driver", headers: "Txn Isolation: SERIALIZABLE", body: "INSERT INTO payments (id, account_id, amount, status)\nVALUES ('pay_9981', 'acc_48210', 450.00, 'SCHEDULED');", action: "Payment record persisted synchronously to Primary Amazon Aurora Postgres instance.", response: "1 Row Inserted (0.8ms)", badge: "PERSISTED" },
          { nodeIdx: 4, lineId: "line-3-4", title: "Step 5: Debezium CDC Stream to ClickHouse via Amazon MSK", protocol: "Debezium WAL CDC -> Amazon MSK", headers: "Topic: cc-payments-wal\nPartition: 4", body: "{\n  \"before\": null,\n  \"after\": { \"id\": \"pay_9981\", \"amount\": 450.00 },\n  \"op\": \"c\"\n}", action: "Debezium streams Postgres WAL change event without table locks into ClickHouse OLAP.", response: "202 Accepted { txn_id: 'tx_9981' }", badge: "COMPLETED" }
        ]
      }
    ]
  },
  q2: {
    scenarios: [
      {
        name: "Scenario 1: POS Card Swipe Approval (Lua Atomic Check)",
        nodes: [
          { title: "1. Merchant POS Terminal", sub: "ISO 8583 Card Swipe Signal" },
          { title: "2. AWS Network Load Balancer (NLB)", sub: "High-Throughput TCP/gRPC Ingress (50k QPS)" },
          { title: "3. AWS Fargate (POS Auth Service)", sub: "Go Microservice ISO Parser & gRPC Router" },
          { title: "4. Amazon ElastiCache Redis Cluster", sub: "Lua Single-Threaded Atomic Balance Check" },
          { title: "5. Amazon DynamoDB Audit Log", sub: "Async Amazon MSK Audit Stream" }
        ],
        steps: [
          { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: Merchant Swipes Card for $150", protocol: "ISO 8583 Message", headers: "Merchant-ID: merch_99", body: "{\n  \"amount\": 150.00\n}", action: "POS terminal transmits authorization request for $150 transaction.", response: "Pending Auth", badge: "SWIPED" },
          { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: AWS NLB Routes to Fargate Container", protocol: "AWS NLB TCP Proxy", headers: "X-Correlation-ID: auth_77192a", body: "{\n  \"card_id\": \"c_48210\"\n}", action: "NLB balances traffic across AWS Fargate POS authorization containers.", response: "Routing to Service", badge: "NLB ROUTED" },
          { nodeIdx: 2, lineId: "line-2-3", title: "Step 3: AWS Fargate Service Executes Redis Lua Script", protocol: "Amazon ElastiCache EVALSHA", headers: "Script: check_and_decr.lua", body: "{\n  \"approved\": true\n}", action: "Fargate container executes Lua script: 400 + 150 <= 1000 -> Updates spend atomically.", response: "APPROVED (00)", badge: "APPROVED" },
          { nodeIdx: 3, lineId: "line-3-4", title: "Step 4: Balance Deducted in ElastiCache Primary", protocol: "ElastiCache In-Memory Write", headers: "Key: card:c_48210:balance", body: "{\n  \"new_balance\": 550.00\n}", action: "In-memory remaining balance updated with sub-2ms latency.", response: "Balance Updated", badge: "BALANCE UPDATED" },
          { nodeIdx: 4, lineId: "line-3-4", title: "Step 5: Async Audit Event Published to DynamoDB", protocol: "AWS SDK DynamoDB", headers: "Table: auth_events", body: "{\n  \"decision\": \"APPROVED\"\n}", action: "Approval log written asynchronously to DynamoDB via Amazon MSK without blocking ISO response.", response: "200 OK (ISO Resp: 00)", badge: "AUDITED" }
        ]
      }
    ]
  },
  q3: {
    scenarios: [
      {
        name: "Scenario 1: Multi-Region Active-Active Consensus & Failover",
        nodes: [
          { title: "1. User Mobile / Web Client", sub: "HTTP POST /transactions" },
          { title: "2. AWS Route 53 Anycast DNS", sub: "Latency Routing (us-east-1 Active)" },
          { title: "3. AWS Fargate Regional Compute", sub: "us-east-1 Active Container Gateway" },
          { title: "4. CockroachDB / Aurora Global Engine", sub: "3/5 Multi-Region Quorum Sync" },
          { title: "5. AWS Route 53 Failover (us-west-2)", sub: "Automated Failover Cluster (<3s RTO)" }
        ],
        steps: [
          { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: User Deposited $500 in US-East-1", protocol: "HTTP POST /v1/transactions", headers: "Geo: US-East", body: "{\n  \"amount\": 500.00\n}", action: "AWS Route 53 routes request to nearest US-East data center.", response: "Processing...", badge: "US-EAST-1" },
          { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: AWS Fargate Service Receives Deposit", protocol: "AWS ECS Fargate gRPC", headers: "Cluster: us-east-1a", body: "{\n  \"status\": \"VALIDATED\"\n}", action: "Fargate container verifies deposit account parameters.", response: "Validated", badge: "FARGATE OK" },
          { nodeIdx: 2, lineId: "line-2-3", title: "Step 3: Quorum Consensus Synchronizes Across Regions", protocol: "Multi-Region Quorum Sync", headers: "Quorum: 3/5 Replicas Ack", body: "{\n  \"us_east_ack\": true\n}", action: "Raft consensus writes transaction synchronously to US-East & US-West database nodes.", response: "Quorum Committed", badge: "QUORUM SYNC" },
          { nodeIdx: 3, lineId: "line-3-4", title: "Step 4: Total AWS US-East-1 Regional Outage Occurs!", protocol: "AWS Route 53 Health Probe", headers: "us-east-1: UNHEALTHY", body: "{\n  \"outage\": true\n}", action: "AWS US-East-1 loses total power. Health probe fails after 2 consecutive checks.", response: "Health Check Failed", badge: "OUTAGE ALERT" },
          { nodeIdx: 4, lineId: "line-3-4", title: "Step 5: Route 53 DNS Failover to US-West-2 in 2.8s", protocol: "AWS Route 53 Failover", headers: "Active: us-west-2", body: "{\n  \"recovered\": true\n}", action: "Route 53 shifts 100% traffic to US-West-2. Zero transaction data lost (RPO = 0)!", response: "100% Recovered (2.8s)", badge: "ZERO RPO" }
        ]
      }
    ]
  },
  q4: {
    scenarios: [
      {
        name: "Scenario 1: Under Quota Request (200 OK)",
        nodes: [
          { title: "1. Partner App Client", sub: "HTTP GET Request" },
          { title: "2. Amazon API Gateway / Envoy", sub: "Extract API Key & Quota Profile" },
          { title: "3. AWS Fargate (Rate Limiter Service)", sub: "Evaluates Sliding Window Quota" },
          { title: "4. Amazon ElastiCache Redis ZSET", sub: "Sliding Window Counter Log" },
          { title: "5. Core Banking Microservice", sub: "Process & Return Account Payload" }
        ],
        steps: [
          { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: Partner API Request", protocol: "HTTP/1.1 GET /v1/accounts", headers: "X-API-Key: key_partner_99", body: "{}", action: "Partner app sends GET request to core banking API.", response: "Pending...", badge: "REQUEST" },
          { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Amazon API Gateway Key Check", protocol: "Amazon API Gateway Filter", headers: "Key: key_partner_99", body: "{\n  \"client_id\": \"client_fintech_99\",\n  \"limit_per_min\": 100\n}", action: "API Gateway extracts client ID and fetches rate limit quota profile.", response: "Routing to Service", badge: "PROFILE OK" },
          { nodeIdx: 2, lineId: "line-2-3", title: "Step 3: AWS Fargate Service Queries ElastiCache", protocol: "AWS ECS Fargate gRPC", headers: "ZSET-Key: rate:client_fintech_99", body: "{\n  \"active_count\": 42\n}", action: "Rate limiter service executes sliding window Redis query.", response: "Querying Redis", badge: "LIMITER QUERY" },
          { nodeIdx: 3, lineId: "line-3-4", title: "Step 4: ElastiCache Redis ZSET Evaluation", protocol: "Amazon ElastiCache Pipeline", headers: "Status: ALLOWED", body: "{\n  \"allowed\": true\n}", action: "Redis purges timestamps older than now - 60s. Count = 42 < 100 limit.", response: "Allowed (42/100)", badge: "ZSET PASS" },
          { nodeIdx: 4, lineId: "line-3-4", title: "Step 5: Core Banking Service Responds with 200 OK", protocol: "AWS Fargate Core Banking", headers: "X-RateLimit-Remaining: 57", body: "{\n  \"status\": \"SUCCESS\"\n}", action: "Core banking service returns account data with remaining quota headers.", response: "200 OK (Remaining: 57)", badge: "200 OK" }
        ]
      }
    ]
  },
  q5: {
    scenarios: [
      {
        name: "Scenario 1: Real-Time Fraud Evaluation (Sub-50ms)",
        nodes: [
          { title: "1. Payment Auth Pipeline Client", sub: "Incoming Transaction Authorization" },
          { title: "2. Amazon API Gateway", sub: "Route gRPC Request to Fraud Orchestrator" },
          { title: "3. AWS Fargate (Fraud Orchestrator)", sub: "Coordinates Feature Fetching & Inference" },
          { title: "4. Amazon ElastiCache Feature Store & ONNX Runtime", sub: "Fetch 120 Features & Run XGBoost Model" },
          { title: "5. AWS Lambda (Decision Rule Service)", sub: "Approve / Challenge SMS MFA Response" }
        ],
        steps: [
          { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: Auth Request Arrives", protocol: "gRPC Auth Event", headers: "User-ID: u_8819", body: "{\n  \"amount\": 1200.00\n}", action: "Auth pipeline sends user ID and transaction amount for evaluation.", response: "Evaluating...", badge: "EVALUATE" },
          { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Amazon API Gateway Routes to Fargate", protocol: "HTTP/2 gRPC", headers: "Service: fraud-orchestrator", body: "{\n  \"user_id\": \"u_8819\"\n}", action: "Gateway forwards request to AWS Fargate microservice.", response: "Routed", badge: "GATEWAY ROUTE" },
          { nodeIdx: 2, lineId: "line-2-3", title: "Step 3: AWS Fargate Service Fetches ElastiCache Features", protocol: "ElastiCache MGET (sub-2ms)", headers: "Features: 120 Data Points", body: "{\n  \"velocity_1m\": 4,\n  \"device_risk\": 0.91\n}", action: "Fetches user's 1-minute transaction velocity and device trust score.", response: "Features Retrived", badge: "FEATURES LOADED" },
          { nodeIdx: 3, lineId: "line-3-4", title: "Step 4: ONNX C++ Model Inference Engine", protocol: "ONNX Runtime C++ API", headers: "Model: fraud_xgboost_v4.onnx", body: "{\n  \"fraud_score\": 0.88\n}", action: "Runs XGBoost tree evaluation in 4.2ms. Output fraud score = 0.88.", response: "Score Calculated", badge: "ML SCORED" },
          { nodeIdx: 4, lineId: "line-3-4", title: "Step 5: AWS Lambda Decision Service Triggers Step-Up Auth", protocol: "AWS Lambda Function", headers: "Threshold: 0.75", body: "{\n  \"decision\": \"CHALLENGE_MFA\"\n}", action: "Fraud score > 0.75 threshold. Triggers SMS MFA prompt to cardholder via Amazon SNS.", response: "200 OK (MFA Sent)", badge: "DECISION ISSUED" }
        ]
      }
    ]
  },
  q6: {
    scenarios: [
      {
        name: "Scenario 1: Apache Flink Stateful Rewards Aggregation",
        nodes: [
          { title: "1. Card Settlement Producer", sub: "Publish Completed Purchase Event" },
          { title: "2. Amazon MSK (Managed Kafka)", sub: "Partition Key = account_id" },
          { title: "3. AWS EKS / Fargate (Apache Flink)", sub: "RocksDB Stateful 30-Day Window" },
          { title: "4. AWS Fargate (Rewards API Service)", sub: "DynamoDB Tier Status Update" },
          { title: "5. Amazon SNS / APNS / FCM", sub: "Instant Gold Tier Unlock Alert" }
        ],
        steps: [
          { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: Settlement Event Published to Amazon MSK", protocol: "Amazon MSK Event", headers: "Topic: card-settlements", body: "{\n  \"amount\": 350.00\n}", action: "Settlement engine posts completed $350 transaction event.", response: "Event Queued", badge: "EVENT PUBLISHED" },
          { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Amazon MSK Ingests Partitioned Message", protocol: "Kafka Consumer", headers: "Partition: 3", body: "{\n  \"account_id\": \"acc_99182\"\n}", action: "Amazon MSK streams event to Flink consumer task manager.", response: "Stream Ingested", badge: "STREAM INGESTED" },
          { nodeIdx: 2, lineId: "line-2-3", title: "Step 3: Flink Computes Rolling Monthly Spend", protocol: "Apache Flink Operator", headers: "State: RocksDB", body: "{\n  \"prev_spend\": 9700.00,\n  \"new_spend\": 10050.00\n}", action: "Flink updates user's rolling 30-day spend total to $10,050.", response: "Window Updated", badge: "STATE UPDATED" },
          { nodeIdx: 3, lineId: "line-3-4", title: "Step 4: Rewards API Updates User Tier Status", protocol: "AWS Fargate Microservice", headers: "Tier: Gold ($10k+)", body: "{\n  \"unlocked_tier\": \"GOLD\"\n}", action: "User crosses $10,000 threshold. Rewards API grants Gold status.", response: "Tier Upgraded", badge: "GOLD UNLOCKED" },
          { nodeIdx: 4, lineId: "line-3-4", title: "Step 5: Real-Time Mobile Push Notification", protocol: "Amazon SNS -> APNS / FCM", headers: "DeviceToken: tok_99a", body: "{\n  \"title\": \"Congratulations! You unlocked Gold Status 🎉\"\n}", action: "Push notification delivered to user's smartphone within 380ms.", response: "Delivered (200)", badge: "NOTIFICATION SENT" }
        ]
      }
    ]
  },
  q7: {
    scenarios: [
      {
        name: "Scenario 1: Debezium CDC Mainframe Ingestion",
        nodes: [
          { title: "1. Mainframe DB2 Database", sub: "WAL Write-Ahead Log Emission" },
          { title: "2. AWS Direct Connect + Debezium CDC", sub: "Non-Blocking Delta Extraction" },
          { title: "3. Amazon MSK + Kafka Connect (AWS Fargate)", sub: "Snappy Parquet Batch Conversion" },
          { title: "4. Amazon S3 Data Lake", sub: "s3://c1-lake-raw Parquet Storage" },
          { title: "5. Snowflake Analytics Warehouse", sub: "Snowpipe Auto-Ingestion" }
        ],
        steps: [
          { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: Customer Account Balance Updated on DB2", protocol: "Mainframe DB2 Commit", headers: "Table: ACCT_BAL", body: "{\n  \"acct_id\": \"99182\",\n  \"bal\": 5400.00\n}", action: "Mainframe transaction updates DB2 record. Write-Ahead Log entry emitted.", response: "DB2 Committed", badge: "WAL EMITTED" },
          { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Debezium Captures WAL Delta via AWS Direct Connect", protocol: "Debezium Connector", headers: "Source: db2_cdc_connector", body: "{\n  \"op\": \"u\",\n  \"before\": 4900.00,\n  \"after\": 5400.00\n}", action: "Debezium reads DB2 transaction log without locking active database tables.", response: "CDC Captured", badge: "CDC READ" },
          { nodeIdx: 2, lineId: "line-2-3", title: "Step 3: Kafka Connect Batches Records to Parquet", protocol: "Amazon MSK S3 Sink", headers: "Format: Apache Parquet", body: "{\n  \"batch_size_mb\": 64,\n  \"compression\": \"SNAPPY\"\n}", action: "Kafka Connect on AWS Fargate aggregates CDC records into 64MB Parquet files.", response: "Parquet Generated", badge: "BATCH CREATED" },
          { nodeIdx: 3, lineId: "line-3-4", title: "Step 4: Files Persisted to Amazon S3 Data Lake", protocol: "AWS S3 API", headers: "Bucket: s3://c1-lake-raw", body: "{\n  \"key\": \"2026/10/06/batch_992.parquet\"\n}", action: "Parquet batch uploaded to S3 data lake.", response: "S3 Written", badge: "S3 PERSISTED" },
          { nodeIdx: 4, lineId: "line-3-4", title: "Step 5: Amazon S3 Auto-Ingest into Snowflake Lake", protocol: "Snowpipe Auto-Ingest", headers: "Target: SNOWFLAKE_RAW", body: "{\n  \"rows_inserted\": 10000\n}", action: "Snowpipe detects new S3 file and loads account delta into Snowflake analytical warehouse.", response: "Snowflake Ingested", badge: "LAKE LOADED" }
        ]
      }
    ]
  },
  q8: {
    scenarios: [
      {
        name: "Scenario 1: CQRS Event Sourcing Ledger Write",
        nodes: [
          { title: "1. BNPL Checkout Gateway", sub: "Create $200 Order Request" },
          { title: "2. Amazon API Gateway", sub: "HTTPS Ingress & Idempotency Key Validation" },
          { title: "3. AWS Fargate (Ledger Command API)", sub: "Spring Boot Double-Entry Accounting Validator" },
          { title: "4. Amazon Aurora PostgreSQL (Event Store)", sub: "Append Entry with Cryptographic Hash" },
          { title: "5. Amazon OpenSearch / DynamoDB (CQRS)", sub: "Asynchronous Merchant Balance View" }
        ],
        steps: [
          { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: Order Created for $200 BNPL Loan", protocol: "HTTP POST /v1/ledger", headers: "Product: BNPL_4_PAY", body: "{\n  \"order_id\": \"ord_5521\",\n  \"amount\": 200.00\n}", action: "User initiates 4-installment BNPL loan for $200 online purchase.", response: "Processing...", badge: "LOAN REQUEST" },
          { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Amazon API Gateway Validates Request", protocol: "Amazon API Gateway", headers: "Idempotency-Key: idemp_7719", body: "{\n  \"status\": \"VALIDATED\"\n}", action: "API Gateway verifies HTTPS request parameters and routes to Fargate.", response: "Gateway Validated", badge: "GATEWAY OK" },
          { nodeIdx: 2, lineId: "line-2-3", title: "Step 3: Double-Entry Balance Verification", protocol: "AWS Fargate Ledger API", headers: "Check: Debit == Credit", body: "{\n  \"debit_loans_receivable\": 200.00,\n  \"credit_merchant_payable\": 200.00\n}", action: "Fargate Spring Boot microservice validates balanced double-entry transaction record.", response: "Balanced (0.00 Diff)", badge: "ACCOUNTING VERIFIED" },
          { nodeIdx: 3, lineId: "line-3-4", title: "Step 4: Immutable Entry Appended to Event Store", protocol: "Amazon Aurora Postgres", headers: "Sequence_Num: 994812", body: "{\n  \"entry_id\": \"ent_8829\",\n  \"hash\": \"a8f9c41e...\"\n}", action: "Ledger entry appended to immutable Aurora event log with cryptographic chain hash.", response: "Event Persisted", badge: "LEDGER SEALED" },
          { nodeIdx: 4, lineId: "line-3-4", title: "Step 5: CQRS Read Projection Asynchronously Updated", protocol: "Amazon MSK -> OpenSearch", headers: "View: Merchant_Balance_Summary", body: "{\n  \"merchant_id\": \"m_9921\",\n  \"pending_payout\": 200.00\n}", action: "Read projection updates merchant's queryable balance view within 45ms.", response: "Read Model Synced", badge: "VIEW PROJECTED" }
        ]
      }
    ]
  },
  q9: {
    scenarios: [
      {
        name: "Scenario 1: Cross-Border FX Settlement Pipeline",
        nodes: [
          { title: "1. ISO 20022 Gateway", sub: "pacs.008 XML Transfer Request" },
          { title: "2. Amazon API Gateway", sub: "Edge Ingress & Validation" },
          { title: "3. AWS Fargate (Compliance Screener)", sub: "Sub-30ms OFAC Sanctions Trie Matcher" },
          { title: "4. Amazon ElastiCache Redis (FX Rate Engine)", sub: "Lock USD/EUR Rate (0.9215)" },
          { title: "5. Amazon MSK + SWIFT gpi Network", sub: "Nostro Account Settlement" }
        ],
        steps: [
          { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: Cross-Border Payment Instruction Received", protocol: "ISO 20022 XML Message", headers: "Message: pacs.008.001.08", body: "{\n  \"instructed_amount\": 10000.00,\n  \"currency\": \"USD\",\n  \"target_curr\": \"EUR\"\n}", action: "Originating bank submits cross-border transfer instruction.", response: "pacs.008 Received", badge: "ISO PARSED" },
          { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Amazon API Gateway Validates Payload", protocol: "Amazon API Gateway", headers: "Pipeline: aml-screening", body: "{\n  \"status\": \"ROUTING\"\n}", action: "API Gateway forwards instruction payload to Fargate compliance microservice.", response: "Routing", badge: "GATEWAY ROUTED" },
          { nodeIdx: 2, lineId: "line-2-3", title: "Step 3: Sub-30ms OFAC Sanctions Screening", protocol: "AWS Fargate Aho-Corasick Trie", headers: "List: OFAC_SDN_2026", body: "{\n  \"sanction_match\": false,\n  \"confidence\": 0.00\n}", action: "High-speed Fargate screener checks sender and receiver names against sanctions database.", response: "CLEARED (No Match)", badge: "AML CLEARED" },
          { nodeIdx: 3, lineId: "line-3-4", title: "Step 4: FX Rate Lock (USD -> EUR @ 0.9215)", protocol: "Amazon ElastiCache Redis", headers: "Lock_ID: fx_lock_8871", body: "{\n  \"locked_rate\": 0.9215,\n  \"eur_amount\": 9215.00,\n  \"ttl_sec\": 10\n}", action: "Rate engine locks 0.9215 exchange rate in ElastiCache Redis for 10 seconds.", response: "Rate Locked", badge: "FX LOCKED" },
          { nodeIdx: 4, lineId: "line-3-4", title: "Step 5: Settlement Execution via SWIFT gpi Network", protocol: "Amazon MSK -> SWIFT gpi", headers: "UETR: e94812a-33f1", body: "{\n  \"status\": \"SETTLED\",\n  \"vostro_debited\": 9215.00\n}", action: "Nostro account debited and funds credited to beneficiary bank in Frankfurt via SWIFT.", response: "200 OK (Settled)", badge: "SWIFT SETTLED" }
        ]
      }
    ]
  }
};
