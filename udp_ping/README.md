"""
UDP Ping Module

This folder contains all UDP-based ping utilities for network diagnostics.

Files:
- udp_pinger_client.py: Basic UDP ping client
- udp_pinger_server.py: UDP ping server with simulated packet loss
- udp_pinger_client_icmp_error.py: UDP client with ICMP error detection
- udp_pinger_server_icmp_error.py: UDP server with ICMP error injection

Quick Start:
    # Terminal 1
    python3 udp_pinger_server.py
    
    # Terminal 2
    python3 udp_pinger_client.py

Features:
- Connectionless UDP communication
- RTT measurement
- Packet loss simulation and detection
- ICMP error handling
"""
