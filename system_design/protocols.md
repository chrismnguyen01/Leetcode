# HTTP, REST, and gRPC — Interview Notes

This document provides clear, detailed, interview-ready explanations of **HTTP**, **REST**, and **gRPC**.  
Use it as study notes or reference material.

---

## 📘 HTTP (HyperText Transfer Protocol)

HTTP is the foundational application-layer protocol used for communication on the web. It defines how clients and servers format and exchange messages.

### Key Concepts
- **Methods / Verbs**
  - `GET` – retrieve data  
  - `POST` – create data  
  - `PUT` – replace data  
  - `PATCH` – partial update  
  - `DELETE` – remove data  

- **Status Codes**
  - **2xx** – Success  
  - **3xx** – Redirect  
  - **4xx** – Client error  
  - **5xx** – Server error  

- **Message Structure**
  - Request: method, URL, headers, body  
  - Response: status code, headers, body  

- **Stateless**
  - Server does not store session state; each request contains all necessary context.

- **Transport**
  - Typically runs over TCP.
  - Important versions:
    - **HTTP/1.1** – text-based, no multiplexing  
    - **HTTP/2** – binary framing, multiplexing, header compression  

### Why HTTP Matters
HTTP is the universal transport for browsers, APIs, mobile apps, and backend services. A solid understanding of HTTP is essential for debugging, API design, caching, authentication, and performance optimization.

---

## 📗 REST (Representational State Transfer)

REST is an architectural style for designing networked APIs using HTTP.  
It is **not** a protocol; it is a set of constraints that promote simplicity, scalability, and statelessness.

### REST Constraints
1. **Client–Server**  
   - Separates user interface from data storage and logic.

2. **Stateless**  
   - Each request must contain all information needed.  
   - Server does not keep client sessions.

3. **Uniform Interface** *(core of REST)*  
   - Resource-based URLs (`/users/5`)  
   - Use HTTP verbs correctly  
   - JSON or other representations  
   - Self-descriptive messages  
   - Optional HATEOAS (links in responses)

4. **Cacheable**  
   - Responses define whether they can be cached.

5. **Layered System**  
   - Clients cannot tell if intermediaries (proxies, load balancers) exist.

6. **Code-on-Demand (Optional)**  
   - Server may send executable code (rare in APIs).

### What REST APIs Look Like
- **Endpoints:** `/users`, `/orders/123`  
- **Methods:** GET, POST, PUT, DELETE  
- **Formats:** JSON (common), XML, etc.

### Why REST Is Popular
- Human-readable  
- Easy to test and debug  
- Wide client compatibility (browsers, mobile apps, 3rd-party developers)  
- Ideal for public APIs  

---

## 📙 gRPC (Google Remote Procedure Call)

gRPC is a modern, high-performance RPC framework built on **HTTP/2**.  
It allows a client to call methods on a remote server as if it were a local function.

### How gRPC Works
- APIs are defined using **Protocol Buffers (.proto)**.
- gRPC generates client and server code automatically.
- Communication uses compact **binary Protobuf** messages.
- Uses **HTTP/2** features:
  - Multiplexing  
  - Header compression  
  - Bidirectional streaming  
  - Low latency

### RPC Model
Instead of resource URLs, gRPC exposes **methods**:
```proto
rpc GetUser(GetUserRequest) returns (GetUserResponse);