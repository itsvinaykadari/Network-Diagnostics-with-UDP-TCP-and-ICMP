"""
ICMP Ping Module

This folder contains ICMP-based ping utilities using raw sockets.

Files:
- icmp_network_pinger.py: ICMP echo request pinger using raw sockets

Quick Start:
    # Requires root/sudo privileges
    sudo python3 icmp_network_pinger.py
    
    # Enter target host IP and number of pings when prompted

Features:
- Raw socket ICMP implementation
- Host reachability testing
- RTT measurement for ICMP packets
- ICMP error response handling
- Network connectivity diagnostics
- Works with any reachable host (e.g., 8.8.8.8, google.com)

Requirements:
- Root/sudo privileges for raw socket operations
- Linux/Unix system
"""
