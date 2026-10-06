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
          keyPoints: ["Supports complex SQL joins & secondary indexes", "Storage auto-scales up to 128TB per instance", "Up to 15 read replicas with < 20ms replication lag"]
        },
        {
          name: "Amazon DynamoDB (NoSQL)",
          type: "Key-Value / Document Store",
          latency: "1ms - 5ms",
          bestFor: "High-throughput key lookups, credit card swipe balance checks, user session profiles.",
          keyPoints: ["Single-digit millisecond latency at arbitrary PB scale", "Global Tables for active-active multi-region replication", "Zero connection pool limits"]
        },
        {
          name: "ElastiCache Redis (In-Memory)",
          type: "Key-Value Data Structure Cache",
          latency: "< 1ms",
          bestFor: "Sub-millisecond rate limiters (ZSET sliding window), hot card balance caching, distributed locks (SETNX).",
          keyPoints: ["In-memory single-threaded execution", "Supports Sorted Sets, Hashes, Bitmaps, Pub/Sub", "Volatile storage requiring fallback to persistent DB"]
        },
        {
          name: "ClickHouse / Redshift (OLAP)",
          type: "Columnar Analytics Engine",
          latency: "10ms - 200ms",
          bestFor: "Real-time fraud detection analytics, aggregated queries over billions of transaction records.",
          keyPoints: ["Column-oriented compression reduces disk IO by 10x-100x", "Optimized for append-heavy analytical queries", "Not suitable for single-row transactional writes"]
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
          layer: "Layer 4 (Transport)",
          features: "TCP / UDP / TLS / gRPC forwarding. Operates at transport layer with static IP per AZ.",
          latency: "Sub-1ms latency overhead",
          throughput: "Millions of QPS without pre-warming",
          whenToUse: "High-throughput payment ingest APIs, gRPC internal service mesh, static IP whitelisting."
        },
        {
          name: "AWS Application Load Balancer (ALB - L7)",
          layer: "Layer 7 (Application)",
          features: "HTTP / HTTPS / HTTP/2 path & host routing, TLS termination, AWS WAF integration, sticky sessions.",
          latency: "2ms - 5ms routing overhead",
          throughput: "Auto-scales with pre-warming for major spikes",
          whenToUse: "RESTful web services, microservices requiring path-based routing (e.g. /v1/auth vs /v1/pay)."
        },
        {
          name: "Amazon API Gateway (L7 Gateway)",
          layer: "Layer 7 (API Management)",
          features: "Rate limiting / throttling (Token Bucket), API key usage plans, JWT/Cognito auth, request validation, OpenAPI spec support.",
          latency: "10ms - 30ms latency overhead",
          throughput: "Managed throttling limits (e.g. 10k RPS soft limit)",
          whenToUse: "Edge API facing public mobile apps, partner integration endpoints, serverless triggers to Lambda."
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

  // System Design Architectural Patterns
  patterns: [
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
