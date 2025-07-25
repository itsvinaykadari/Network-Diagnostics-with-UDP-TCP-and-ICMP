### README for Running UDP and TCP Pinger Programs

This guide explains how to run the provided programs from each folder (`Part1`, `Part2`, and `Part3`). Each folder contains both client and server files. Below are the instructions for running each part and file in a simple format.

---

## **Part 1: UDP Pinger**

### **Server:**
- File: `UDP_icmp_server.py` or `UDPPingerServer.py`
- **How to run:**
  1. Open a terminal.
  2. Navigate to the `Part1` directory.
  3. Run the server:
     ```bash
     python3 UDP_icmp_server.py
     ```
     or
     ```bash
     python3 UDPPingerServer.py
     ```

### **Client:**
- File: `UDP_icmp_client.py` or `UDPPingerClient.py`
- **How to run:**
  1. Open a second terminal.
  2. Navigate to the `Part1` directory.
  3. Run the client:
     ```bash
     python3 UDP_icmp_client.py
     ```
     or
     ```bash
     python3 UDPPingerClient.py
     ```

---

## **Part 2: TCP Pinger**

### **Server:**
- File: `TCP_icmp_server.py`, `TCPPingerServer.py`, or `TCPPingerThreading.py`
- **How to run:**
  1. Open a terminal.
  2. Navigate to the `Part2` directory.
  3. Run the server:
     ```bash
     python3 TCP_icmp_server.py
     ```
     or
     ```bash
     python3 TCPPingerServer.py
     ```
     For multi-threading:
     ```bash
     python3 TCPPingerThreading.py
     ```

### **Client:**
- File: `TCP_icmp_client.py` or `TCPPingerClient.py`
- **How to run:**
  1. Open a second terminal.
  2. Navigate to the `Part2` directory.
  3. Run the client:
     ```bash
     python3 TCP_icmp_client.py
     ```
     or
     ```bash
     python3 TCPPingerClient.py
     ```

---

## **Part 3: ICMP Pinger**

### **Server:**
- No separate server file required for this part.

### **Client:**
- File: `ICMP_Pinger.py`
- **How to run:**
  1. Open a terminal.
  2. Navigate to the `Part3` directory.
  3. Run the client:
     ```bash
     python3 ICMP_Pinger.py
     ```
