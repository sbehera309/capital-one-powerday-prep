// Cheat Sheet & Sizing Formulas Dataset

export const cheatsheetData = {
  sizingMath: [
    { label: "1 Million Requests / Day", value: "~12.5 Requests / Sec Average (~25 QPS Peak)" },
    { label: "100 Million Requests / Day", value: "~1,160 Requests / Sec Average (~2,300 QPS Peak)" },
    { label: "1 Billion Requests / Day", value: "~11,600 Requests / Sec Average (~23,200 QPS Peak)" },
    { label: "1 KB Payload @ 1,000 QPS", value: "1 MB/sec Network Throughput (~86.4 GB / Day)" },
    { label: "Redis Latency", value: "Sub-1ms to 2ms (In-memory, single-threaded event loop)" },
    { label: "Postgres / MySQL SSD Latency", value: "5ms - 15ms (Indexed read)" }
  ],
  systemDesignPatterns: [
    { title: "Saga Pattern (Choreography vs Orchestration)", desc: "Manages distributed transactions across microservices using compensating transactions if a step fails." },
    { title: "CQRS (Command Query Responsibility Segregation)", desc: "Separates read and write data models to optimize high-throughput analytics independently from OLTP writes." },
    { title: "Event Sourcing", desc: "Stores state as an immutable sequence of events rather than current state snapshots, allowing full historical replay." },
    { title: "Circuit Breaker", desc: "Prevents cascading microservice failures by failing fast when downstream services become unresponsive." }
  ]
};
