"""
Network Diagnostics: TCP Pinger Server with Threading Support

PROBLEM STATEMENT:
    Single-threaded TCP servers can only handle one client at a time, creating bottlenecks.
    This multithreaded implementation enables concurrent client connections, simulating
    real-world server scenarios with simulated packet loss for comprehensive testing.

DESCRIPTION:
    This module implements a multithreaded TCP ping server that:
    - Accepts multiple concurrent TCP client connections
    - Spawns a new thread for each client connection
    - Echoes received messages back to clients
    - Simulates packet loss by randomly dropping responses
    - Handles connection errors in individual threads
    - Provides scalable server architecture for testing

USE CASES:
    - Multithreaded server implementation and testing
    - Concurrent client connection handling
    - Scalability testing with multiple simultaneous clients
    - Load testing for TCP-based services
    - Realistic server simulation with packet loss
"""

import random
from socket import *
import threading

# Function to handle each client connection
def handle_client(connectionSocket, address):
    print(f"Connection established with {address}")
    
    try:
        c = 0
        while c < 100:
            c += 1
            # Generate a random number between 1 and 10
            rand = random.randint(1, 10)

            # Receive the message from the client
            message = connectionSocket.recv(1024)

            if not message:
                # If no message is received, break out of the loop
                break

            # Capitalize the message from the client
            message = message.upper()

            # Simulate packet loss by not responding if rand > 8
            if rand > 8:
                print(f"Packet from {address} lost (rand={rand})")
            else:
                # Otherwise, the server responds
                connectionSocket.send(message)
                print(f"Packet from {address} responded: {message.decode()}")

    except Exception as e:
        print(f"Error handling request from {address}: {e}")

    finally:
        # Close the connection with the client after the loop ends
        connectionSocket.close()
        print(f"Connection with {address} closed.")

# Create a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the socket to the address and port
serverSocket.bind(('127.0.0.1', 14008))

# Start listening for incoming connections
serverSocket.listen(5)

print("TCP server with threading support up and listening...")
cnt = 0

while cnt < 10:
    cnt += 1
    # Accept a new client connection
    connectionSocket, address = serverSocket.accept()

    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(connectionSocket, address))
    client_thread.start()
