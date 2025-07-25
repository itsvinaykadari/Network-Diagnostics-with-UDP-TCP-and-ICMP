import random
import struct
from socket import *
import threading

def checksum(data):
    s = 0
    for i in range(0, len(data), 2):
        w = (data[i] << 8) + (data[i+1] if i+1 < len(data) else 0)
        s = s + w
    s = (s >> 16) + (s & 0xffff)
    s = ~s & 0xffff
    return s

def create_icmp_packet(type, code):
    # Type 3 is Destination Unreachable, type 11 is Time Exceeded, etc.
    header = struct.pack('bbHHh', type, code, 0, 0, 0)
    my_checksum = checksum(header)
    header = struct.pack('bbHHh', type, code, my_checksum, 0, 0)
    return header

# Bind the TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('172.21.135.35', 14008))
serverSocket.listen(5)

print("TCP server up and listening...")
cnt = 0

while cnt < 10:
    cnt += 1
    connectionSocket, address = serverSocket.accept()
    print(f"Connection established with {address}")

    try:
        c = 0
        while c < 100:
            c += 1
            rand = random.randint(1, 10)
            message = connectionSocket.recv(1024)
            
            if not message:
                break

            message = message.upper()
            
            if rand < 7:
                connectionSocket.send(message)
                print(f"Packet from {address} responded: {message.decode()}")
                
            elif rand >= 7 and rand <= 8:
                print(f"Sending ICMP Destination Unreachable to {address} (rand={rand})")
                icmp_packet = create_icmp_packet(3, 1)  # Type 3 (Destination Unreachable), Code 1 (Host Unreachable)
                rawSocket = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP)
                rawSocket.sendto(icmp_packet, address)
                rawSocket.close()
                
            elif rand > 8:
                print(f"Sending ICMP Port Unreachable to {address} (rand={rand})")
                icmp_packet = create_icmp_packet(3, 3)  # Type 3 (Destination Unreachable), Code 3 (Port Unreachable)
                rawSocket = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP)
                rawSocket.sendto(icmp_packet, address)
                rawSocket.close()
            
    except Exception as e:
        print(f"Error handling request from {address}: {e}")
    finally:
        connectionSocket.close()
        print(f"Connection with {address} closed.")