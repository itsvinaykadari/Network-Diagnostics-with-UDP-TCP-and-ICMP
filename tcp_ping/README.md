"""
TCP Ping Module

This folder contains all TCP-based ping utilities for network diagnostics.

Files:
- tcp_pinger_client.py: Basic TCP ping client
- tcp_pinger_server.py: TCP ping server
- tcp_pinger_server_threaded.py: Multithreaded TCP server for concurrent clients
- tcp_pinger_client_icmp_error.py: TCP client with ICMP error handling
- tcp_pinger_server_icmp_error.py: TCP server with ICMP error injection

Quick Start:
    # Terminal 1 - Basic Server
    python3 tcp_pinger_server.py
    
    # Terminal 1 - Multithreaded Server (for multiple clients)
    python3 tcp_pinger_server_threaded.py
    
    # Terminal 2+
    python3 tcp_pinger_client.py

Features:
- Connection-oriented TCP communication
- RTT measurement with connection establishment overhead
- Packet loss simulation and detection
- Multithreaded concurrent client handling
- ICMP error detection and injection
"""
