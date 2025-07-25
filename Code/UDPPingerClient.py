# UDPPingerClient.py
import socket
import time  # Import time library

while True:
    
    # Ask the user to set the number of ping operations
    num = int(input("Set the number of ping operations: "))
            
    print("Initiating Ping\n")
    server_ip = '172.21.149.80'
    
    # Create a UDP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    
    server_address = (server_ip, 14008)  # Set IP Address and Port Number of Socket
    
    client.settimeout(1)  # Sets a timeout value of 1 second

    rtt_time = []  # List to store Round-Trip Times (RTTs)
    packet_lost = 0  # Count of lost (timed-out) pings

    try:
        # Loop to ping the server 'num_pings' times
        for i in range(num):
            start = time.time()  # Start time when message is sent to server
            message = 'Ping ' + str(i) + " " + time.ctime(start)
            try:
                sent = client.sendto(message.encode("utf-8"), server_address)
                print("Sent " + message)
                data, server = client.recvfrom(4096)  # Maximum data received 4096 bytes
                print("Received " + str(data.decode("utf-8")))
                end = time.time()
                elapsed = end - start
                rtt_time.append(elapsed * 1000)  # Store RTT in milliseconds
                print("RTT: " + str(elapsed * 1000) + " Milliseconds\n")
            except socket.timeout:
                print("#" + str(i) + " Request timed out for the packet\n")
                packet_lost += 1  # Increment packet loss count
    finally:
        print("Ping completed, terminating socket connection...")
        client.close()

   
    # Calculate and print the minimum, maximum, and average RTTs after all pings are done
    if rtt_time:
        minimum_rtt = min(rtt_time)
        maximun_rtt = max(rtt_time)
        average_rtt = sum(rtt_time) / len(rtt_time)

        packet_loss_rate = (packet_lost / num) * 100
        # Print all stats in one line at the end
        print("\n")
        print("Ping statistics for {}:".format(server_ip))
        print("     Packets: Sent = {}, Received = {}, Lost = {} ({}% loss)".format(num,num-packet_lost, packet_lost, packet_loss_rate))
        print("Approximate round trip times in milli-seconds:")
        print("     Minimum: {:.2f} ms, Maximum: {:.2f} ms, Average: {:.2f} ms\n".format(minimum_rtt, maximun_rtt, average_rtt))

    else:
        print("Ping attempts failed.\n")