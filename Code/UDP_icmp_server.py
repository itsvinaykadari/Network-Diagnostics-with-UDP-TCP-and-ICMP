import random
import socket
import struct
import os

# Create a UDP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_ip = '172.21.132.171'
server_port = 14008
serverSocket.bind((server_ip, server_port))

print(f"Server is listening on port: {server_port} and IP: {server_ip}")

# Function to send ICMP Destination Unreachable or Port Unreachable
def send_icmp_error(dest_addr, error_type, code):
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    
    packet_id = os.getpid() & 0xFFFF
    header = struct.pack('!BBHHH', error_type, code, 0, packet_id, 1)
    
    # Include dummy IP header for compatibility with some systems
    ip_header = struct.pack('!BBHHHBBH4s4s',
                            69, 0, 84, 54321, 0, 255, socket.IPPROTO_ICMP, 0,
                            socket.inet_aton(server_ip),
                            socket.inet_aton(dest_addr))
    
    # Send ICMP error packet to client
    sock.sendto(ip_header + header, (dest_addr, 0))
    sock.close()

while True:
    rand = random.randint(1, 10)
    message, client_address = serverSocket.recvfrom(1024)
    message = message.upper()
    client_ip, client_port = client_address
    print(f"Received from {client_ip}:{client_port}: {message.decode('utf-8')}")

    if rand <= 6:
        # Send UDP packet normally
        serverSocket.sendto(message, client_address)
    elif rand > 6 and rand <= 8:
        # Send ICMP Destination Unreachable (Type 3, Code 0)
        print(f"Sending ICMP Destination Unreachable to {client_ip}")
        send_icmp_error(client_ip, 3, 0)
    elif rand > 8:
        # Send ICMP Port Unreachable (Type 3, Code 3)
        print(f"Sending ICMP Port Unreachable to {client_ip}")
        send_icmp_error(client_ip, 3, 3)