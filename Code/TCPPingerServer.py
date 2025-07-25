import random
from socket import *
import threading

# Create a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the socket to the address and port
serverSocket.bind(('127.0.0.1', 14008))

# Start listening for incoming connections
serverSocket.listen(5)

print("TCP server up and listening...")
cnt=0
while cnt<10:
    cnt+=1
    # Accept a new client connection
    connectionSocket, address = serverSocket.accept()
    print(f"Connection established with {address}")

    try:
        c=0
        while c<100:
            # Generate a random number between 1 and 10
            c+=1

            # Receive the message from the client
            message = connectionSocket.recv(1024)

            if not message:
                # If no message is received, break out of the loop
                break

            # Capitalize the message from the client
            message = message.upper()

            # Otherwise, the server responds
            connectionSocket.send(message)
            print(f"Packet from {address} responded: {message.decode()}")

    except Exception as e:
        print(f"Error handling request from {address}: {e}")

    finally:
        # Close the connection with the client after the loop ends
        connectionSocket.close()
        print(f"Connection with {address} closed.")

