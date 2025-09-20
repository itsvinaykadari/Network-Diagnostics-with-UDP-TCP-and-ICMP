# Network Diagnostics with UDP, TCP, and ICMP

This project focuses on implementing and analyzing network diagnostic tools using **UDP, TCP, and ICMP** protocols through Python socket programming. The objective is to measure **RTT (Round Trip Time)**, detect **timeouts**, analyze **packet loss**, and study the effects of **network impairments** such as simulated packet loss and ICMP errors.

---

## 📌 Features

### 1. UDP Pinger
- Implemented UDP Pinger Client and Server.
- Measured **RTT** using timestamping before/after sending packets.
- Handled **timeouts** using exceptions and simulated **packet loss** via Python `random` module.
- Emulated real packet loss at NIC using **Linux tc-netem** tool.
- Added ICMP error simulation (Destination Unreachable, Port Unreachable).

### 2. TCP Pinger
- Implemented **TCP Pinger Client and Server** with socket programming.
- Reliable connection-oriented communication.
- Measured **min, max, average RTT** and packet loss rate.
- **Multithreaded TCP Server**: supports concurrent clients using Python `threading`.
- Simulated TCP packet loss using **Linux tc-netem**.

### 3. ICMP Pinger
- Implemented ICMP client using raw sockets to send ICMP packets.
- Tested connectivity to hosts (e.g., google.com).
- Handled ICMP errors and packet losses gracefully.

---

## ⚙️ Tools & Technologies
- **Python 3**
- **Socket Programming**
- **Multithreading**
- **Linux tc-netem & iptables** (to emulate packet loss)
- **Raw Sockets** (for ICMP simulation)

---

## 🚀 Use Cases
- **Network Performance Testing** → Measure RTT, latency, and packet loss across networks.
- **Troubleshooting Connectivity** → Detect host availability & differentiate TCP vs UDP issues.
- **Load Testing & Scalability** → Multithreaded TCP server to simulate multiple concurrent clients.
- **Realistic Network Simulation** → Emulate real-world conditions (loss, delay, errors).
- **Educational Tool** → Hands-on learning of **UDP, TCP, ICMP** and error handling in networking.

---

## 📂 Project Structure
```
├── UDP_Pinger_Client.py
├── UDP_Pinger_Server.py
├── TCP_Pinger_Client.py
├── TCP_Pinger_Server.py
├── ICMP_Pinger.py
├── TCP_ICMP_Server.py
├── TCP_ICMP_Client.py
└── README.md
```

---

## 🧑‍🤝‍🧑 Contributors
- **Vinaykumar Kadari (CS24MTECH14008)** → TCP Pinger, ICMP Pinger, Error Handling
- **P. Rushi Keswar Reddy (CS24MTECH11018)** → ICMP_Pinger, TCPPingerThreading, UDP ICMP Client/Server
- **Kishor Kumar Patro (SM24MTECH14001)** → UDP Pinger, UDP ICMP Server

---

## 📝 Acknowledgements
- [Python Socket Programming Docs](https://docs.python.org/3/howto/sockets.html)
- [GeeksforGeeks: ICMP Pinger](https://www.geeksforgeeks.org/internet-control-message-protocol-icmp/)
- [Traffic Control with tc-netem](https://www.pico.net/kb/how-can-i-simulate-delayed-and-dropped-packets-in-linux/)
