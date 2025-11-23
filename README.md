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
.
├── README.md                                 # Main project documentation
├── udp_ping/                                 # UDP-based ping utilities
│   ├── README.md                             # UDP module documentation
│   ├── udp_pinger_client.py                  # UDP ping client
│   ├── udp_pinger_server.py                  # UDP ping server with packet loss simulation
│   ├── udp_pinger_client_icmp_error.py       # UDP client with ICMP error detection
│   └── udp_pinger_server_icmp_error.py       # UDP server with ICMP error injection
├── tcp_ping/                                 # TCP-based ping utilities
│   ├── README.md                             # TCP module documentation
│   ├── tcp_pinger_client.py                  # TCP ping client
│   ├── tcp_pinger_server.py                  # TCP ping server
│   ├── tcp_pinger_server_threaded.py         # Multithreaded TCP server
│   ├── tcp_pinger_client_icmp_error.py       # TCP client with ICMP error handling
│   └── tcp_pinger_server_icmp_error.py       # TCP server with ICMP error injection
└── icmp_ping/                                # ICMP-based ping utilities
    ├── README.md                             # ICMP module documentation
    └── icmp_network_pinger.py                # ICMP pinger using raw sockets
```

---

## 🎯 Getting Started

### Prerequisites
- Python 3.x
- Linux/Unix system (for raw socket support)
- Root privileges (for ICMP pinger and raw socket operations)

### Running UDP Pinger
```bash
cd udp_ping/

# Terminal 1: Start UDP Server
python3 udp_pinger_server.py

# Terminal 2: Run UDP Client
python3 udp_pinger_client.py
```

### Running TCP Pinger
```bash
cd tcp_ping/

# Terminal 1: Start TCP Server
python3 tcp_pinger_server.py

# Terminal 2: Run TCP Client
python3 tcp_pinger_client.py
```

### Running Multithreaded TCP Server
```bash
cd tcp_ping/

# Terminal 1: Start Multithreaded TCP Server
python3 tcp_pinger_server_threaded.py

# Terminal 2+: Run multiple TCP Clients
python3 tcp_pinger_client.py
```

### Running ICMP Pinger (requires root)
```bash
cd icmp_ping/

# Run ICMP pinger
sudo python3 icmp_network_pinger.py
```

### UDP with ICMP Error Simulation
```bash
cd udp_ping/

# Terminal 1: Start UDP Server with ICMP errors
python3 udp_pinger_server_icmp_error.py

# Terminal 2: Run UDP Client with ICMP error detection
python3 udp_pinger_client_icmp_error.py
```

### TCP with ICMP Error Simulation
```bash
cd tcp_ping/

# Terminal 1: Start TCP Server with ICMP errors
sudo python3 tcp_pinger_server_icmp_error.py

# Terminal 2: Run TCP Client with ICMP error handling
python3 tcp_pinger_client_icmp_error.py
```

---

## 📊 Key Metrics Measured

1. **Round Trip Time (RTT)**: Time between sending and receiving a ping packet
2. **Minimum RTT**: Fastest response time observed
3. **Maximum RTT**: Slowest response time observed
4. **Average RTT**: Mean of all RTT measurements
5. **Packet Loss Rate**: Percentage of packets lost/not responded to
6. **ICMP Error Codes**: Type and code of ICMP error messages received

---

## 🔧 Configuration

### Modifying Server/Client Addresses
Edit the following variables in each script:
- `server_ip`: The server's IP address
- `server_port`: The port number (default: 14008)
- `num`: Number of ping operations

### Adjusting Timeout Values
- Modify `client.settimeout(1)` to change timeout duration (in seconds)

### Changing Packet Loss Rate
- In `udp_pinger_server.py` and similar files, modify the condition `if rand > 8:` 
- Higher threshold = lower packet loss rate

---

## 📈 Output Example

```
Set the number of ping operations: 5
Initiating Ping

Sent Ping 0 <timestamp>
Received PING 0 <TIMESTAMP>
RTT: 0.125 Milliseconds

Sent Ping 1 <timestamp>
Received PING 1 <TIMESTAMP>
RTT: 0.098 Milliseconds

# 2 Request timed out for the packet

Sent Ping 3 <timestamp>
Received PING 3 <TIMESTAMP>
RTT: 0.110 Milliseconds

Sent Ping 4 <timestamp>
Received PING 4 <TIMESTAMP>
RTT: 0.105 Milliseconds

Ping statistics for 127.0.0.1:
     Packets: Sent = 5, Received = 4, Lost = 1 (20.0% loss)
Approximate round trip times in milli-seconds:
     Minimum: 0.10 ms, Maximum: 0.13 ms, Average: 0.11 ms
```

---

## 🛠️ Troubleshooting

### Permission Denied for Raw Sockets
```bash
# Run with sudo for ICMP pinger
sudo python3 icmp_network_pinger.py
```

### Connection Refused
- Ensure server is running on the specified address and port
- Check firewall rules and port availability

### Timeout Issues
- Increase timeout value in `client.settimeout()`
- Check network connectivity to the target host

### Module Not Found
```bash
# Ensure required modules are available
python3 -c "import socket; import threading; import struct"
```

---

## 📚 Learning Outcomes

By using this project, learners will understand:
- **Socket Programming**: Creating and managing network sockets
- **Protocol Implementation**: UDP, TCP, and ICMP protocol mechanics
- **Network Diagnostics**: Measuring and analyzing network performance
- **Error Handling**: Detecting and handling network-related errors
- **Concurrency**: Implementing multithreaded server architectures
- **Raw Sockets**: Direct network packet manipulation and analysis

---


## 🧑‍🤝‍🧑 Contributors
- **Vinaykumar Kadari (CS24MTECH14008)** → TCP Pinger, ICMP Pinger, Error Handling
- **P. Rushi Keswar Reddy (CS24MTECH11018)** → ICMP_Pinger, TCPPingerThreading, UDP ICMP Client/Server
- **Kishor Kumar Patro (SM24MTECH14001)** → UDP Pinger, UDP ICMP Server

## 📝 References

- [Python Socket Programming Documentation](https://docs.python.org/3/howto/sockets.html)
- [ICMP Protocol Specification - RFC 792](https://tools.ietf.org/html/rfc792)
- [UDP Protocol Specification - RFC 768](https://tools.ietf.org/html/rfc768)
- [TCP Protocol Specification - RFC 793](https://tools.ietf.org/html/rfc793)
- [Linux Traffic Control (tc-netem)](https://www.pico.net/kb/how-can-i-simulate-delayed-and-dropped-packets-in-linux/)
- [Socket Programming with Raw Sockets](http://sockraw.org/papers/sock_raw)

---

## 📄 License

This project is provided as-is for educational and learning purposes.

---

## 💡 Future Enhancements

- [ ] IPv6 support for ping clients and servers
- [ ] Support for custom ping payload sizes
- [ ] Graphical visualization of network statistics
- [ ] Integration with system-level network monitoring tools
- [ ] Configuration file support for server/client settings
- [ ] Docker containerization for easy deployment
- [ ] Network bandwidth measurement tools
- [ ] Traceroute implementation

---

## 🤝 Contributing

Contributions are welcome! Please ensure:
- Code follows Python best practices (PEP 8)
- All files include descriptive headers
- Documentation is clear and comprehensive
- New features include example usage
