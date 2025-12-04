# 🧱 System Design Interview — Complete Study Guide

This guide covers all essential concepts, patterns, components, and mental models needed for **system design interviews**.  
Use it as a reference, checklist, and study map.

---

# 1. 📌 How to Approach Any System Design Question

### **Step-by-Step Framework**
1. **Clarify requirements**
   - Functional (features)
   - Non-functional (scalability, latency, availability, durability)
   - Constraints (users, QPS, data size)
2. **Define the API / core operations**
3. **Create a high-level design**
   - Client → Load Balancer → Application Layer → Databases → Caches → Storage
4. **Identify bottlenecks & scale**
   - Horizontal scaling
   - Replication
   - Sharding
   - Caching
   - Queues
5. **Deep dive into components**
   - Data model
   - Consistency model
   - Indexes
   - Partitioning
6. **Discuss trade-offs**
   - Latency vs throughput
   - Consistency vs availability
   - Storage vs performance
7. **Address non-functional requirements**
   - Monitoring
   - Logging
   - Security
   - Rate-limiting
   - Failover
8. **Summarize and defend choices**

---

# 2. 🚦 Must-Know Concepts (Core of SD Interviews)

## **2.1 Scalability Basics**
- **Vertical scaling** → add CPU/RAM
- **Horizontal scaling** → add more servers (preferred)
- **Stateful vs Stateless services**
  - Stateless = easy to scale
  - Stateful = needs sticky sessions or externalizing state (Redis/DB)

---

# 3. 💾 Databases (SQL vs NoSQL)

## **3.1 SQL**
- Relational, strong consistency
- Good for: transactions, financial systems
- Supports JOINs, indexing, constraints

## **3.2 NoSQL**
- Schema-less, distributed
- Types:
  - **Key-Value:** Redis, DynamoDB
  - **Document:** MongoDB
  - **Columnar:** Cassandra
  - **Graph:** Neo4j

## **3.3 When to choose what**
- Need strong consistency → SQL  
- Need horizontal scale → NoSQL  
- Need fast reads → Cache + NoSQL  
- Need analytics → Column store  

---

# 4. ⚙️ Core System Components

## **4.1 Load Balancers**
- Distribute traffic across servers
- Algorithms:
  - Round-robin
  - Weighted
  - Least connections
  - IP hash (sticky sessions)

## **4.2 Caching**
- Reduces latency & DB load
- Types:
  - **Application-level** (in-memory, local)
  - **Redis / Memcached**
  - **CDN** (Cloudflare, Akamai)
- Cache patterns:
  - **Cache-Aside**
  - **Write-Through**
  - **Write-Behind**
  - **TTL expiration**

## **4.3 Message Queues**
- Asynchronous processing
- Smooth traffic spikes
- Technologies: Kafka, RabbitMQ, SQS
- Used for:
  - Sending emails
  - Processing payments
  - Logging pipelines

---

# 5. 🌍 Consistency, Availability & Partition Tolerance (CAP)

## **5.1 CAP Theorem**
- In distributed systems, you can pick **2 of 3**:
  - **Consistency**
  - **Availability**
  - **Partition Tolerance**

## **5.2 Strong vs Eventual Consistency**
- **Strong:** read = latest write (SQL, Spanner)
- **Eventual:** read catches up eventually (DynamoDB, Cassandra)

---

# 6. ⚡ High-Performance Techniques

### **6.1 Sharding/Partitioning**
- Split data across machines
- Strategies:
  - Hash-based
  - Range-based
  - Geo-based
- Challenges:
  - Hot partitions
  - Resharding

### **6.2 Replication**
- **Master–Slave** (read replicas)
- **Master–Master**
- **Quorum-based (majority writes)**

### **6.3 CDN**
- Push static content closer to users
- Use for:
  - Images
  - Videos
  - Scripts
  - Profile pictures

---

# 7. 🔐 Security (Interview-relevant)
- Rate limiting (prevent abuse)
- Throttling
- Authentication (OAuth 2.0, JWT)
- Authorization (RBAC)
- Encryption (HTTPS, TLS)
- Input validation
- WAF (Web Application Firewall)

---

# 8. 🔍 Observability
- Logging (structured logs)
- Monitoring (Grafana, Prometheus)
- Metrics (latency, error rate, throughput)
- Alerting
- Distributed tracing (Jaeger, Zipkin)

---

# 9. 📊 Estimations (Very Important!)

### **Know how to estimate:**
- QPS (queries per second)
- Storage size
- Bandwidth
- Read/write ratios
- Latency budgets

### Example:
- 100M users  
- 10% daily active → 10M  
- 20 requests per user per day → 200M requests/day  
- ≈ 2,300 requests/sec  

---

# 10. 🧱 Common System Design Problems + Strategies

## **10.1 Design a URL Shortener**
Concepts:
- Hashing
- Write-heavy vs read-heavy
- Cache hot URLs

## **10.2 Design Twitter / News Feed**
Concepts:
- Fan-out on write vs fan-out on read
- Timeline service
- Caching hot timelines

## **10.3 Design Instagram**
Concepts:
- Object storage (S3)
- CDN
- Metadata in DB
- Sharding by user

## **10.4 Design Uber**
Concepts:
- Real-time location (Pub/Sub)
- Spatial databases (Quadtrees / Geohash)
- Matching engine

## **10.5 Design Chat System**
Concepts:
- WebSockets
- Delivery guarantees
- Presence service
- Message queues

---

# 11. 🏗️ Architecture Patterns

### **11.1 Microservices**
Pros:
- Independent deployment
- Scalability per service  
Cons:
- Operational complexity
- Network latency

### **11.2 Monolith**
Pros:
- Simpler, easy debugging  
Cons:
- Hard to scale teams, slower deployments

### **11.3 Event-Driven Architecture**
- Loose coupling  
- High scalability  
- Real-time systems  

---

# 12. 📚 Database Indexing (High ROI Topic)
- Improves read speed
- Types:
  - B-tree index
  - Hash index
  - Composite index
  - Full-text index
- Write performance decreases with more indexes

---

# 13. 🗂️ Data Storage Layers

| Data Type | Best Storage |
|----------|--------------|
| Raw media (images/videos) | S3, GCS |
| Logs | Kafka → S3 |
| Analytics | BigQuery, Snowflake |
| User profiles | SQL or NoSQL |
| Sessions | Redis |

---

# 14. 💡 Protocols to Know
- **HTTP/1.1** — text, sequential
- **HTTP/2** — binary, multiplexing
- **HTTP/3** — QUIC (UDP), even faster
- **REST** — resource-based API design
- **gRPC** — binary RPC over HTTP/2
- **WebSockets** — real-time async comms

---

# 15. 🧩 Trade-Offs Cheat Sheet

### Consistency vs Availability
- Banking → Consistency  
- Social media → Availability  

### SQL vs NoSQL
- Complex queries → SQL  
- Horizontal scaling → NoSQL  

### Caching vs DB
- Hot data → Cache  
- Source of truth → DB  

### Microservices vs Monolith
- Huge teams → Microservices  
- Small startups → Monolith  

---

# 16. 📝 What Interviewers Evaluate
- Clarity of thinking  
- Trade-off awareness  
- Understanding of scaling  
- Correct use of components  
- Ability to estimate  
- Realistic architecture  
- Communication skills  

---

# 17. 🧠 Final Study Checklist

### If you can explain these topics confidently, you're ready:
- Load balancing  
- Caching strategies  
- SQL vs NoSQL trade-offs  
- Sharding + replication  
- Messaging queues  
- Consistency models  
- CDN usage  
- Rate limiting  
- High-level architecture diagrams  
- Estimations (QPS, data size)  
- Common design patterns (fan-out, write-heavy, read-heavy, leader-election)  

---

# 🎉 You're Ready
Study this, build mental models, and practice designing systems like:
- Twitter  
- Instagram  
- WhatsApp  
- Uber  
- YouTube  
- Dropbox  
- Google Maps  

Master these patterns → you can solve any system design question.

