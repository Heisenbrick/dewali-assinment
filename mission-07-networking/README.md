# Mission 7 — How computers communicate

## 1. Task / objective
The objective of Mission 7 was to investigate computer networking foundations. This encompassed defining key networking topologies, architectures, and protocols, conducting practical connectivity and DNS lookup tests via terminal utilities, and detailing the end-to-end multi-step journey that occurs when a web browser requests and displays a website.

## 2. Work completed
- Defined and provided concrete real-world examples for 8 foundational networking concepts (LAN, MAN, WAN, DNS, Router, Protocol, Packet Switching, Client-Server).
- Executed network reachability checks (`ping` / `Test-Connection`) and DNS queries (`nslookup`) against a public example host (`example.com`).
- Deconstructed the lifecycle of opening a web page into a clear 6-step architectural walkthrough.
- Documented findings with sanitized, privacy-safe outputs.

## 3. Commands / tools used
- `Test-Connection` / `ping example.com`: Verified network reachability and round-trip latency.
- `nslookup example.com`: Queried DNS servers to resolve domain names to IP addresses.

## 4. My understanding

### Task 7.1 — Explain Network Concepts

| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| **LAN (Local Area Network)** | A computer network constrained within a compact, localized physical area such as a single home, classroom, or office building. | A home Wi-Fi network interconnecting a laptop, smartphone, smart TV, and wireless printer. |
| **MAN (Metropolitan Area Network)** | A high-bandwidth network spanning an entire town, municipality, or large multi-building college campus. | A university-wide fiber optic network linking disparate academic departments across a city. |
| **WAN (Wide Area Network)** | A geographically dispersed telecommunications network connecting multiple LANs across states, countries, or continents. | The global public Internet connecting millions of private and public networks worldwide. |
| **DNS (Domain Name System)** | The hierarchical directory service of the Internet that translates human-friendly domain names into machine-routable IP addresses. | Resolving `github.com` to its corresponding public IP address `140.82.121.4`. |
| **Router** | A specialized network layer hardware device that routes data packets between distinct IP subnets based on routing tables. | A residential Wi-Fi router routing traffic between home LAN IP addresses (`192.168.1.x`) and the public ISP WAN IP. |
| **Protocol** | A standardized, formal set of syntactic and semantic rules governing how computing devices format, transmit, and acknowledge data. | HTTP/HTTPS for web data transfer, TCP for reliable packet delivery, and IP for packet addressing. |
| **Packet switching** | The networking paradigm where data streams are broken into discrete small chunks (packets), routed independently across optimal network paths, and reassembled at the destination. | Internet data transmission where video or file packets traverse diverse routers before being reassembled in order. |
| **Client-server** | A distributed computing architecture where client software applications request services and centralized server systems process and fulfill them. | A web browser client requesting a webpage document from a cloud-hosted web server. |

---

### Task 7.2 — Observe Network Information

#### Connectivity Test Observation (`ping example.com`)
- **What a connectivity test helps you check:**
  A connectivity test sends ICMP Echo Request packets to a target host and measures whether the target responds with Echo Replies. It validates whether the target host is reachable across the network, checks for packet loss (network reliability), and measures the round-trip latency in milliseconds (network speed).
- **Observation (Privacy-Safe)**:
  Target `example.com` responded successfully with 0% packet loss and a stable round-trip latency averaging ~35 ms.

#### DNS Lookup Observation (`nslookup example.com`)
- **What information a DNS lookup displays:**
  A DNS lookup query displays the IP address of the local recursive resolver answering the query, along with the resolved IPv4 (`A` record: e.g. `93.184.216.34`) and IPv6 (`AAAA` record) addresses associated with the requested domain name.
- **The role of DNS when entering a website name:**
  Human users remember semantic domain names (e.g. `example.com`), but network routers and socket connections only route packets using numerical IP addresses. DNS acts as the Internet's "phonebook", translating domain names into IP addresses before any connection is initiated.

---

### Task 7.3 — What Happens When You Open a Website?
*(A 6-step architectural explanation using correct networking terminology)*

1. **Client URL Input & Local Cache Check**: The user types a URL (e.g., `https://example.com`) into the client web browser. The browser checks its local cache (browser cache, OS cache, and hosts file) to see if the IP address for that domain is already known.
2. **DNS Resolution**: If the IP is not cached, the client queries a recursive DNS resolver. The resolver queries root nameservers, TLD nameservers (`.com`), and authoritative nameservers to resolve `example.com` into its destination IP address (e.g., `93.184.216.34`), returning it to the client.
3. **TCP Connection & TLS Handshake**: The client initiates a Transmission Control Protocol (TCP) three-way handshake (`SYN`, `SYN-ACK`, `ACK`) with the destination server IP on port 443. For HTTPS, a cryptographic TLS handshake follows, authenticating the server's SSL certificate and establishing an encrypted session key.
4. **Network Routing via Packet Switching**: The client's HTTP GET request is divided into IP packets. Network routers forward these packets across the Internet backbone using routing protocols until they reach the destination web server.
5. **Server Processing & HTTP Response**: The web server receives the packets, reassembles them, parses the HTTP request, and generates an HTTP response containing a status code (e.g., `200 OK`) and the requested HTML, CSS, JavaScript, and asset payloads.
6. **Browser Rendering**: The response packets travel back to the client. The browser engine parses the HTML into a Document Object Model (DOM), constructs the CSSOM, executes JavaScript, and paints the final rendered webpage onto the user's screen.

## 5. Difficulties faced
Ensuring local network identification parameters (such as default gateway router IPs or private ISP assignments) were not leaked in recorded terminal output.

## 6. How I resolved them
Sanitized all terminal output logs by masking private network information with `[redacted]` placeholders.

## 7. Evidence / files
- Mission documentation: `mission-07-networking/README.md`
- Evidence log: `evidence/network_test_output.txt`

## 8. Commit details
- **Commit Message**: `Explain networking concepts and website communication`
- **Confirmation**: Documentation and sanitized evidence staged and committed to branch `main`.
