// Comprehensive System Design & Cloud Architecture Cheat Sheet Dataset
// Strictly Aligned with AWS Enterprise Architecture & Technical Interview Standards

export const cheatsheetData = {
  // Preserved for calculatorsModule.js compatibility
  sizingMath: [
    { label: "1 Million Requests / Day", value: "~12.5 Requests / Sec Avg (~25 QPS Peak)" },
    { label: "100 Million Requests / Day", value: "~1,160 Requests / Sec Avg (~2,300 QPS Peak)" },
    { label: "1 Billion Requests / Day", value: "~11,600 Requests / Sec Avg (~23,200 QPS Peak)" },
    { label: "1 KB Payload @ 1,000 QPS", value: "1 MB/sec Throughput (~86.4 GB / Day)" },
    { label: "Redis In-Memory Latency", value: "< 1ms (Sub-millisecond event loop)" },
    { label: "Postgres / MySQL SSD Latency", value: "2ms - 10ms (Indexed read)" }
  ],

  // System Design Comparative Trade-offs Matrix
  comparisons: [
    {
      id: "compute",
      category: "AWS Compute Strategy",
      title: "AWS Fargate vs AWS Lambda vs AWS EC2",
      badge: "Compute Layer",
      color: "cyan",
      items: [
        {
          name: "AWS Fargate (Containers)",
          bestFor: "Long-running microservices, persistent HikariCP DB connection pools, steady gRPC/HTTP traffic.",
          pros: ["Zero server maintenance", "Supports warm DB connection pooling", "Predictable pricing for steady QPS", "Full memory/CPU allocation (up to 16 vCPU)"],
          cons: ["Pay per running task hour", "Slower scaling than Lambda (1-2 mins to launch task)"],
          verdict: "Ideal for core payment services & stateful API gateways requiring persistent Aurora DB connections."
        },
        {
          name: "AWS Lambda (Serverless)",
          bestFor: "Event-driven workflows, SQS queue consumers, bursty APIs, cron jobs, payload < 6MB.",
          pros: ["Scales to zero cost", "Instant sub-second auto-scaling up to 10k executions", "Zero server administration"],
          cons: ["Cold-start latencies (100ms-500ms)", "15-minute max execution limit", "DB connection pool exhaustion without RDS Proxy"],
          verdict: "Ideal for async notifications, batch processors, and event-driven webhook ingestion."
        },
        {
          name: "AWS EC2 (Virtual Machines)",
          bestFor: "Custom OS kernels, extreme low-level performance tuning, legacy stateful monoliths, GPU training.",
          pros: ["Full root control", "Spot instances save up to 90%", "Highest raw networking throughput (100Gbps+)"],
          cons: ["Manual OS patching & security updates", "Complex auto-scaling group warm-up delay"],
          verdict: "Ideal for high-frequency trading engines or custom ML inference models needing dedicated GPU hardware."
        }
      ]
    },
    {
      id: "databases",
      category: "Database & Storage Strategy",
      title: "Aurora Postgres vs DynamoDB vs ElastiCache Redis vs ClickHouse",
      badge: "Storage Layer",
      color: "emerald",
      items: [
        {
          name: "Amazon Aurora Postgres (OLTP)",
          type: "Relational ACID DB",
          latency: "2ms - 10ms",
          bestFor: "Financial ledger balance accounting, multi-table ACID transactions, serializable isolation.",
          pros: [
            "Multi-table serializable ACID transactions & SQL joins",
            "Storage auto-scales up to 128TB per instance with 6-way AZ replication",
            "Up to 15 low-latency read replicas (< 20ms replication lag)"
          ],
          cons: [
            "Connection pool limits require PgBouncer / HikariCP management",
            "Write throughput bounded by primary writer instance scale"
          ],
          verdict: "Primary database for ledger accounting, user balances, and strict transaction compliance."
        },
        {
          name: "Amazon DynamoDB (NoSQL)",
          type: "Key-Value / Document Store",
          latency: "1ms - 5ms",
          bestFor: "High-throughput key lookups, credit card swipe balance checks, user session profiles.",
          pros: [
            "Single-digit millisecond latency at arbitrary Petabyte scale",
            "Global Tables for active-active multi-region replication",
            "Serverless connection handling (zero DB connection pool limits)"
          ],
          cons: [
            "Item size limit capped at 400KB per item",
            "Complex multi-table queries require single-table design modeling"
          ],
          verdict: "Primary datastore for POS swipe auth, session locks, and active-active multi-region user data."
        },
        {
          name: "ElastiCache Redis (In-Memory)",
          type: "Key-Value Data Structure Cache",
          latency: "< 1ms",
          bestFor: "Sub-millisecond rate limiters (ZSET sliding window), hot card balance caching, distributed locks (SETNX).",
          pros: [
            "Sub-millisecond in-memory read & write execution",
            "Rich data structures (Sorted Sets, Hashes, Bitmaps, HyperLogLog, Pub/Sub)",
            "Atomic Lua script execution (EVALSHA for race-free rate limits)"
          ],
          cons: [
            "Volatile memory requires persistent DB fallback (Aurora/DynamoDB)",
            "Single-threaded event loop can bottleneck on expensive O(N) operations"
          ],
          verdict: "Mandatory caching & distributed locking tier for rate limiters, session caches, and idempotency locks."
        },
        {
          name: "ClickHouse / Redshift (OLAP)",
          type: "Columnar Analytics Engine",
          latency: "10ms - 200ms",
          bestFor: "Real-time fraud detection analytics, aggregated queries over billions of transaction records.",
          pros: [
            "Columnar storage compression reduces disk I/O by 10x - 100x",
            "Vectorized query execution processes 100M+ rows per second",
            "Optimized for append-only log & analytical streaming ingestion"
          ],
          cons: [
            "High latency for single-row transactional point lookups",
            "Does not support multi-row transactional ACID updates"
          ],
          verdict: "Primary analytical warehouse for real-time fraud monitoring, transaction history reporting, and BI dashboards."
        }
      ]
    },
    {
      id: "networking",
      category: "Networking & Load Balancing",
      title: "Network Load Balancer (NLB) vs Application Load Balancer (ALB) vs API Gateway",
      badge: "Networking Layer",
      color: "indigo",
      items: [
        {
          name: "AWS Network Load Balancer (NLB - L4)",
          type: "Layer 4 (Transport)",
          latency: "Sub-1ms",
          bestFor: "High-throughput payment ingest APIs, gRPC internal service mesh, static IP whitelisting.",
          pros: [
            "Handles millions of QPS instantly without pre-warming",
            "Sub-1ms latency overhead at transport layer (TCP/UDP/TLS/gRPC)",
            "Provides static Elastic IP address per Availability Zone"
          ],
          cons: [
            "No HTTP path-based or header-based routing rules",
            "No integrated AWS WAF inspection at Layer 7"
          ],
          verdict: "Ideal for high-volume TCP payment gateways, internal gRPC microservice traffic, and IP whitelisting."
        },
        {
          name: "AWS Application Load Balancer (ALB - L7)",
          type: "Layer 7 (Application)",
          latency: "2ms - 5ms",
          bestFor: "RESTful web services, microservices requiring path-based routing (e.g. /v1/auth vs /v1/pay).",
          pros: [
            "HTTP / HTTPS / HTTP/2 path, host, and header-based routing",
            "Native integration with AWS WAF for layer 7 DDoS & SQLi protection",
            "TLS termination and sticky session routing"
          ],
          cons: [
            "Requires pre-warming for sudden massive traffic spikes (e.g. 10x flash sales)",
            "Slightly higher latency overhead than L4 NLB (2ms-5ms vs sub-ms)"
          ],
          verdict: "Standard load balancer for web APIs, containerized Fargate microservices, and public endpoints."
        },
        {
          name: "Amazon API Gateway (L7 Gateway)",
          type: "Layer 7 (API Management)",
          latency: "10ms - 30ms",
          bestFor: "Edge API facing public mobile apps, partner integration endpoints, serverless triggers to Lambda.",
          pros: [
            "Built-in rate limiting & throttling per client API key (Token Bucket)",
            "API usage plans, OAuth2 / JWT / Cognito authentication",
            "Native request payload validation & OpenAPI specification import"
          ],
          cons: [
            "10ms-30ms gateway latency overhead",
            "Managed account throttling limits requiring quota increases"
          ],
          verdict: "Primary public edge gateway for mobile apps, partner developers, and serverless API backends."
        }
      ]
    },
    {
      id: "streaming",
      category: "Messaging & Streaming Strategy",
      title: "Apache Kafka (AWS MSK) vs AWS Kinesis vs AWS SQS/SNS vs Debezium CDC",
      badge: "Messaging Overview",
      color: "purple",
      items: [
        {
          name: "Apache Kafka / AWS MSK",
          type: "Distributed Commit Log",
          latency: "5ms - 20ms",
          bestFor: "Enterprise event backbone, high-throughput log streams, multi-consumer event replay, Flink analytics.",
          pros: [
            "Log-based commit stream with retention up to months/years",
            "Partition key ordering guarantees across high-throughput clusters",
            "Rich ecosystem (Kafka Connect, Flink SQL, Schema Registry)",
            "Highest raw throughput (100k+ msg/sec per broker node)"
          ],
          cons: [
            "Cluster capacity management overhead (even with managed MSK)",
            "Partition count cannot be easily reduced after creation"
          ],
          verdict: "Standard enterprise event backbone for core microservice event streaming and real-time stateful stream processing."
        },
        {
          name: "AWS Kinesis Data Streams",
          type: "Serverless Stream Log",
          latency: "10ms - 200ms",
          bestFor: "AWS-native serverless stream processing with tight DynamoDB & Lambda triggers.",
          pros: [
            "Managed serverless stream operations with On-Demand auto-scaling",
            "Enhanced Fan-Out delivers dedicated 2 MB/sec throughput per consumer",
            "Native integration with AWS Lambda, EventBridge, and DynamoDB Streams"
          ],
          cons: [
            "1 MB/sec write limit per shard (requires resharding for large volume spikes)",
            "Poison pill record errors block shard partition until handled or expired"
          ],
          verdict: "Ideal for AWS-cloud-native event ingestion pipelines prioritizing zero server administration."
        },
        {
          name: "AWS SQS & SNS (Queue & Pub/Sub)",
          type: "Message Queue & Topic Fan-Out",
          latency: "10ms - 50ms",
          bestFor: "Asynchronous task queueing, worker decoupling, DLQ retries, pub/sub topic notifications.",
          pros: [
            "SNS fans out messages to multiple SQS queues automatically",
            "Built-in Dead-Letter Queue (DLQ) isolates unprocessable poison pills",
            "Pay-per-request pricing ($0.40 per 1M calls) with zero base cost"
          ],
          cons: [
            "Destructive consumption (messages deleted after processing, no stream replay)",
            "Single consumer per queue message (requires SNS topic for multi-service delivery)"
          ],
          verdict: "Ideal for background worker tasks, email/SMS notifications, and resilient microservice task queues."
        },
        {
          name: "Debezium CDC (Change Data Capture)",
          type: "DB Transaction Log Streamer",
          latency: "10ms - 100ms",
          bestFor: "Zero-code stream replication from OLTP DBs (Postgres WAL) to Kafka / analytical sinks.",
          pros: [
            "Eliminates application dual-write partial failure windows completely",
            "Zero database table locks (tails WAL / binlog asynchronously)",
            "Captures full row states (BEFORE/AFTER) with 100% eventual consistency"
          ],
          cons: [
            "Requires Write-Ahead Log (WAL) storage capacity on primary DB",
            "Schema migration changes require schema registry alignment"
          ],
          verdict: "Mandatory enterprise pattern for syncing Postgres OLTP to ClickHouse/Elasticsearch without app code dual-writes."
        }
      ]
    },
    {
      id: "kinesis-vs-sqs",
      category: "AWS Messaging Deep Dive",
      title: "AWS Kinesis Data Streams vs AWS SQS (Simple Queue Service)",
      badge: "Kinesis vs SQS Decision",
      color: "purple",
      items: [
        {
          name: "AWS Kinesis Data Streams",
          type: "Stream Log Model (Pull)",
          latency: "10ms - 200ms",
          bestFor: "Real-time continuous event streaming, multi-consumer event replay, partition-ordered log streams.",
          pros: [
            "Replayable stream log (retention from 24 hours up to 365 days)",
            "Multiple independent microservices read same stream at different offsets",
            "Strict FIFO ordering guaranteed per Shard Partition Key",
            "Enhanced Fan-Out (2 MB/sec dedicated HTTP/2 pipe per consumer)"
          ],
          cons: [
            "Requires shard capacity management (or On-Demand shard pricing)",
            "Poison pill errors block shard processing until handled or expired",
            "Higher baseline cost for low or idle traffic"
          ],
          verdict: "Ideal for real-time credit card transaction ingestion where Fraud ML, Accounting Ledgers, and Analytics pipelines all read the same stream."
        },
        {
          name: "AWS SQS (Simple Queue Service)",
          type: "Task Queue Model (Push/Poll)",
          latency: "10ms - 50ms",
          bestFor: "Asynchronous task queueing, worker decoupling, background job processing with DLQ isolation.",
          pros: [
            "Scales to zero cost ($0.40 per 1 million requests)",
            "Destructive pull model permanently deletes processed tasks",
            "Built-in Dead-Letter Queue (DLQ) isolates unprocessable poison pills",
            "Automatic unlimited horizontal scaling without provisioning shards"
          ],
          cons: [
            "Messages permanently deleted after processing (No stream replay)",
            "Standard SQS offers best-effort ordering (FIFO SQS capped at 3,000 RPS)",
            "Single consumer per message (requires SNS fan-out for multi-service delivery)"
          ],
          verdict: "Ideal for background worker tasks, email/SMS notification dispatch, async webhook processing, and retrying RPC operations."
        }
      ]
    }
  ],

  // ACID Guarantees in PostgreSQL & Financial Databases
  acidPostgres: {
    title: "ACID Guarantees in PostgreSQL & Enterprise Financial Systems",
    badge: "ACID & Transaction Guarantees",
    color: "emerald",
    overview: "ACID principles define the guarantees required for reliable transactional database processing. In financial ledger systems (like Capital One credit card processing), ACID guarantees that account balance debits, credits, and ledger transfers occur deterministically without corruption, race conditions, or partial data loss.",
    properties: [
      {
        letter: "A",
        name: "Atomicity",
        tagline: "All or Nothing Execution",
        concept: "A database transaction consists of one or more SQL statements. Either ALL operations succeed and commit together, or the entire transaction is rolled back with ZERO side effects.",
        postgresMechanism: "Powered by the Write-Ahead Log (WAL) and transaction logs (pg_xact / pg_clog). Uncommitted in-memory changes are discarded on error or ROLLBACK.",
        bankingUseCase: "When transferring $100 from Account A to Account B, DEBIT A and CREDIT B must commit atomically. If the system crashes midway, the transaction aborts and no money is lost."
      },
      {
        letter: "C",
        name: "Consistency",
        tagline: "Valid State Transitions & Schema Constraints",
        concept: "A transaction must transition the database from one valid state to another, strictly enforcing all schema invariants, foreign keys, unique keys, and check constraints.",
        postgresMechanism: "Postgres evaluates CHECK constraints (e.g. balance >= 0), FOREIGN KEY relations, NOT NULL rules, and UNIQUE indexes during execution. Any violation triggers immediate abort.",
        bankingUseCase: "Guarantees that an account balance can never drop below $0 or create orphaned transaction records without a valid customer ID."
      },
      {
        letter: "I",
        name: "Isolation",
        tagline: "Concurrent Transaction Safety (MVCC & Isolation Levels)",
        concept: "Concurrent transactions executing simultaneously must produce the exact same database state as if they were executed serially one after another.",
        postgresMechanism: "Powered by Multi-Version Concurrency Control (MVCC). Readers do not block writers, and writers do not block readers. Supports 4 Isolation Levels: Read Committed (default), Repeatable Read, and Serializable (SSI via SIREAD locks).",
        bankingUseCase: "Prevents race conditions where two simultaneous $500 card swipes double-spend a $600 balance (Write-Skew anomaly prevented by Serializable isolation)."
      },
      {
        letter: "D",
        name: "Durability",
        tagline: "Permanent Storage & Zero Data Loss (RPO = 0)",
        concept: "Once a transaction emits COMMIT and receives success acknowledgment, its changes are permanently recorded in non-volatile storage and survive any subsequent power outage or crash.",
        postgresMechanism: "Enforced via Write-Ahead Log (WAL) & fsync(). In Amazon Aurora Postgres, WAL records are synchronously replicated across 6 storage nodes in 3 Availability Zones (AZs) before acknowledging commit success.",
        bankingUseCase: "Guarantees that approved credit card authorizations are never lost or corrupted even if an entire AWS Availability Zone experiences total power failure."
      }
    ],
    isolationLevels: [
      { level: "Read Committed (Default)", dirtyRead: "Prevented", nonRepeatableRead: "Allowed", phantomRead: "Allowed", writeSkew: "Allowed", notes: "Default in Postgres. Each query sees data committed before query start." },
      { level: "Repeatable Read", dirtyRead: "Prevented", nonRepeatableRead: "Prevented", phantomRead: "Prevented (in PG)", writeSkew: "Allowed", notes: "Snapshot isolation. Transaction sees data committed before transaction start." },
      { level: "Serializable (SSI)", dirtyRead: "Prevented", nonRepeatableRead: "Prevented", phantomRead: "Prevented", writeSkew: "Prevented", notes: "Guarantees true serializability using SIREAD locks to detect write-skew dependencies." }
    ]
  },

  // System Design Architectural Patterns
  patterns: [
    {
      id: "acid-postgres-pattern",
      title: "ACID Transactions (Postgres/Aurora) vs Eventual Consistency (DynamoDB)",
      icon: "🛡️",
      color: "emerald",
      problem: "Using NoSQL eventual consistency databases for multi-table financial ledger accounting allows race conditions, phantom balances, and partial write failures.",
      solution: "Use PostgreSQL / Aurora Postgres for transactional ledgers. ACID guarantees atomicity via WAL logs, integrity via CHECK constraints, concurrent isolation via MVCC, and durability via 6-way AZ WAL replication."
    },
    {
      id: "kinesis-vs-sqs-pattern",
      title: "Stream Log (Kinesis/Kafka) vs Task Queue (SQS)",
      icon: "📡",
      color: "purple",
      problem: "Using SQS for multi-service event streaming requires creating separate queues for every service and managing SNS fan-out, while using Kinesis for simple background tasks wastes shard costs and risks blocking streams on unprocessable poison pill records.",
      solution: "Use Kinesis/Kafka when data represents an immutable append-only event stream (log) read by multiple independent microservices at different speeds. Use SQS when data represents discrete work units (tasks) that should be consumed once by worker threads and deleted upon completion with DLQ failure isolation."
    },
    {
      id: "cdc-vs-dual-write",
      title: "Dual-Write Problem vs Debezium Change Data Capture (CDC)",
      icon: "⚡",
      color: "cyan",
      problem: "Writing to both Postgres OLTP and ClickHouse/Kafka in application code creates partial failure windows (e.g., Postgres commit succeeds, but network timeout causes Kafka publish to fail).",
      solution: "Write exclusively to Postgres. Debezium CDC tails the Postgres Write-Ahead Log (WAL) asynchronously and publishes change events to Kafka with zero table locks and guaranteed eventual consistency."
    },
    {
      id: "saga-pattern",
      title: "Distributed Transactions: Saga Pattern (Orchestration vs Choreography)",
      icon: "🔄",
      color: "amber",
      problem: "2-Phase Commit (2PC) blocks database rows across microservices, causing extreme latency degradation and deadlocks.",
      solution: "Use Saga pattern. Execute local transactions sequentially. If step 3 fails (e.g. Card limit exceeded), publish compensating transactions in reverse order (Step 2 Rollback -> Step 1 Rollback) to restore eventual consistency."
    },
    {
      id: "cqrs-pattern",
      title: "CQRS (Command Query Responsibility Segregation)",
      icon: "📊",
      color: "emerald",
      problem: "Complex SQL aggregations and reporting queries lock rows on OLTP transactional databases, slowing down write throughput.",
      solution: "Separate write path (Commands -> Aurora Postgres) from read path (Queries -> ClickHouse / Redis read projections). Sync read projections via Kafka CDC streams."
    },
    {
      id: "idempotency-key",
      title: "Distributed Idempotency Keys (`SETNX`)",
      icon: "🔑",
      color: "indigo",
      problem: "Mobile app client retries network requests due to timeouts, resulting in double-charging credit cards.",
      solution: "Client attaches unique `Idempotency-Key` header (UUIDv4). API Gateway checks Redis using atomic `SET idempotency_key:UUID status=PROCESSING EX 86400 NX`. If key exists, return stored response or 409 Conflict."
    },
    {
      id: "rate-limiting",
      title: "Rate Limiting: Token Bucket vs Redis Sliding Window (`ZSET`)",
      icon: "⏱️",
      color: "purple",
      problem: "Fixed window counters allow double the allowed rate at window boundaries (e.g., 100 requests at 11:59:59 and 100 at 12:00:00).",
      solution: "Use Redis Sorted Sets (`ZSET`). Key stores client IP/User; score & value are timestamps. Execute `ZREMRANGEBYSCORE key 0 (now - window)` then `ZCARD key`. Atomic Lua execution guarantees sub-1ms sliding window precision."
    },
    {
      id: "consistent-hashing",
      title: "Consistent Hashing & Virtual Nodes",
      icon: "🌐",
      color: "blue",
      problem: "Standard mod-N hashing (`hash(key) % N`) causes 99% of keys to reshuffle when adding or removing cache nodes, destroying cache hit ratios.",
      solution: "Map keys and nodes onto a 2^32 hash ring. Use virtual nodes (e.g., 100 vnodes per physical server) to ensure uniform load distribution. Adding a node only reshuffles 1/N of keys."
    },
    {
      id: "pacelc-theorem",
      title: "PACELC Theorem & Consistent Systems",
      icon: "⚖️",
      color: "rose",
      problem: "CAP theorem only applies when a network Partition occurs, missing normal operation trade-offs.",
      solution: "PACELC states: IF Partitioned (P), choose Availability (A) vs Consistency (C); ELSE (E), choose Latency (L) vs Consistency (C). Examples: DynamoDB defaults to PA/EL; Aurora Postgres is PC/EC."
    }
  ],

  // Essential Latency & SLA Reference Numbers
  latencies: [
    { operation: "L1 Cache Reference", time: "0.5 ns", notes: "CPU Core speed" },
    { operation: "L2 Cache Reference", time: "7 ns", notes: "14x L1 cache" },
    { operation: "Main Memory (RAM) Reference", time: "100 ns", notes: "200x L1 cache" },
    { operation: "Redis In-Memory Key Lookup", time: "< 1 ms", notes: "Sub-millisecond memory speed" },
    { operation: "NVMe SSD Random Read", time: "100 µs", notes: "Fast local disk" },
    { operation: "Postgres Indexed Read (SSD)", time: "2 - 10 ms", notes: "B-Tree index lookup" },
    { operation: "Same AWS Region Network Hop", time: "0.5 - 1 ms", notes: "AZ to AZ VPC latency" },
    { operation: "Cross-Country US Network (NYC to SFO)", time: "60 - 80 ms", notes: "Speed of light in fiber" }
  ],

  slas: [
    { sla: "99.9% Availability (3 Nines)", downtimeYear: "8.76 Hours / Year", downtimeMonth: "43.8 Minutes / Month" },
    { sla: "99.99% Availability (4 Nines)", downtimeYear: "52.6 Minutes / Year", downtimeMonth: "4.38 Minutes / Month" },
    { sla: "99.999% Availability (5 Nines)", downtimeYear: "5.26 Minutes / Year", downtimeMonth: "26.3 Seconds / Month" }
  ]
};
