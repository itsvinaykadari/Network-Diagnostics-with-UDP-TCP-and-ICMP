"""
Network Diagnostics: UDP Pinger Client with ICMP Error Handling

PROBLEM STATEMENT:
    UDP applications need to detect and handle ICMP error messages.
    When a UDP packet cannot reach its destination, ICMP error packets are returned.
    This utility captures these ICMP errors to provide comprehensive error reporting.

DESCRIPTION:
    This module implements a UDP ping client with ICMP error detection that:
    - Sends UDP ping packets to remote servers
    - Listens for ICMP error responses using raw sockets
    - Detects Destination Unreachable and Port Unreachable errors
    - Measures round-trip time for successful packets
    - Reports network unreachability and port closure scenarios
    - Handles timeouts and multiple error conditions

USE CASES:
    - UDP error diagnosis and network troubleshooting
    - Port reachability testing
    - Network path validation
    - ICMP error message analysis
    - UDP-based service diagnostics
"""

import socket
import time
import struct

ICMP_DEST_UNREACHABLE = 3

def parse_icmp_packet(packet):
    ip_header = packet[:20]
    icmp_header = packet[20:28]
    
    # Unpack ICMP header
    icmp_type, icmp_code, _, _, _ = struct.unpack('!BBHHH', icmp_header)
    return icmp_type, icmp_code

while True:
    num = int(input("Set the number of ping operations: "))
    print("Initiating Ping\n")
    
    server_ip = '127.0.0.1'
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.settimeout(1)
    
    rtt_time = []
    packet_lost = 0
    server_address = (server_ip, 14008)
    
    try:
        for i in range(num):
            start = time.time()
            message = f'Ping {i} {time.ctime(start)}'
            try:
                sent = client.sendto(message.encode("utf-8"), server_address)
                print(f"Sent {message}")
                try:
                    # Create a raw socket to listen for ICMP errors
                    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                    raw_socket.settimeout(1)
                    while True:
                        try:
                            data, addr = client.recvfrom(1024)
                            print(f"Received {data.decode('utf-8')} from {addr}")
                            break
                        except socket.timeout:
                            try:
                                # Check for ICMP error messages
                                icmp_data, icmp_addr = raw_socket.recvfrom(1024)
                                icmp_type, icmp_code = parse_icmp_packet(icmp_data)
                                if icmp_type == ICMP_DEST_UNREACHABLE:
                                    if icmp_code == 0:
                                        print(f"ICMP Error: Destination Unreachable from {icmp_addr[0]}")
                                        packet_lost += 1
                                    elif icmp_code == 3:
                                        print(f"ICMP Error: Port Unreachable from {icmp_addr[0]}")
                                        packet_lost += 1

                                    break
                            except socket.timeout:
                                print(f"# {i} Request timed out")
                                packet_lost += 1
                                break

                finally:
                    raw_socket.close()

                end = time.time()
                elapsed = end - start
                rtt_time.append(elapsed * 1000)
                # if icmp_code == 0:
                #     continue
                # elif icmp_code == 3:
                #     continue
                print(f"RTT: {elapsed * 1000:.3f} ms\n")
            except socket.timeout:
                print(f"# {i} Request timed out for the packet\n")
                packet_lost += 1

    finally:
        print("Ping completed, terminating socket connection...")
        client.close()

    if rtt_time:
        minimum_rtt = min(rtt_time)
        maximum_rtt = max(rtt_time)
        average_rtt = sum(rtt_time) / len(rtt_time)

        packet_loss_rate = (packet_lost / num) * 100
        print(f"Ping statistics for {server_ip}:")
        print(f"     Packets: Sent = {num}, Received = {num - packet_lost}, Lost = {packet_lost} ({packet_loss_rate}% loss)")
        print(f"Approximate round trip times in milli-seconds:")
        print(f"     Minimum = {minimum_rtt:.2f} ms, Maximum = {maximum_rtt:.2f} ms, Average = {average_rtt:.2f} ms\n")
    else:
        print("Ping attempts failed.\n")
