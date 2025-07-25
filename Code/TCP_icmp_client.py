import time
from socket import *

# Create a TCP socket
client = socket(AF_INET, SOCK_STREAM)

# Set a timeout of 1 second
client.settimeout(1)
server_ip = '127.0.0.1'
# Server address and port
server_address = (server_ip, 14008)

# Establish a connection to the server
client.connect(server_address)

# Ask the user to set the number of ping operations
num = int(input("Set the number of ping operations: "))

print("Initiating Ping\n")

# Track RTTs and packet loss
rtt_time = []
packet_lost = 0

for i in range(num+1):
    # Prepare the ping message
    start_time = time.time()
    message = 'Ping ' + str(i) + " " + time.ctime(start_time)
    try:
        # Send the message to the server
        sent = client.send(message.encode("utf-8"))
        print("Sent " + message)

        # Receive the response from the server
        response = client.recv(1024)
        print("Received " + str(response.decode("utf-8")))
        

        # Calculate RTT in milliseconds
        rtt = (time.time() - start_time)
        rtt_time.append(rtt)

    except ConnectionResetError:
        # print("Sent " + message)
        print("ICMP Error: Destination Unreachable\n")
        packet_lost += 1
    except OSError:
        # print("Sent " + message)
        print("ICMP Error: Port Unreachable\n")
        packet_lost += 1
    except timeout:
        # Handle timeout (packet loss)
        # print("Sent " + message)
        packet_lost += 1
        print("#" + str(i) + " Request timed out for the packet\n")

# Calculate and print the minimum, maximum, and average RTTs after all pings are done
if rtt_time:
    minimum_rtt = min(rtt_time)
    maximun_rtt = max(rtt_time)
    average_rtt = sum(rtt_time) / len(rtt_time)
    packet_loss_rate = (packet_lost / num) * 100
    # Print all stats in one line at the end
    print("\n")
    print("Ping statistics for {}:".format(server_ip))
    print("     Packets: Sent = {}, Received = {}, Lost = {} ({}% loss)".format(num, num-packet_lost, packet_lost, packet_loss_rate))
    print("Approximate round trip times in milli-seconds:")
    print("     Minimum: {:.2f} ms, Maximum: {:.2f} ms, Average: {:.2f} ms\n".format(minimum_rtt, maximun_rtt, average_rtt))
else:
    print("Ping attempts failed.\n")

# Close the client socket
client.close()