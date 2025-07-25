# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
server_ip='127.0.0.1'
# Assign IP address and port number to socket
serverSocket.bind((server_ip, 14008))

print(f"Server is listening on port: {14008} and ip: {server_ip}")

while True:
    # Generate a random number between 1 to 10 (both inclusive)
    rand = random.randint(1, 10)

    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    message=message.decode('utf-8')

    # Capitalize the message from the client
    message = message.upper()
    print(f"Received from {address[0]}:{address[1]}: {message}")
    # If rand is greater than 8, we consider the packet lost and do not respond to the client
    if rand > 8:
        continue

    # Otherwise, the server response
    serverSocket.sendto(message.encode('utf-8'),address)