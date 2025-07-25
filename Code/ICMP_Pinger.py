from socket import *
import os
import sys
import struct
import time
import select

ICMP_ECHO_REQUEST = 8
ICMP_DEST_UNREACHABLE = 3 
rtts = []
def checksum(string):
    """
    This function takes a argument of a string to calculate the checksum value

    Argument: string(byte)

    Output: checksum value

    """
    csum = 0
    countTo = (len(string) // 2) * 2
    count = 0
    while count < countTo:
        thisVal = string[count+1] * 256 + string[count]
        csum = csum + thisVal
        csum = csum & 0xffffffff
        count = count + 2
    if countTo < len(string):
        csum = csum + string[len(string) - 1]
        csum = csum & 0xffffffff
    csum = (csum >> 16) + (csum & 0xffff)
    csum = csum + (csum >> 16)
    answer = ~csum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer

def receiveOnePing(mySocket, ID, timeout, destAddr):
    """
    Receive one ping from the socket.

    Argument : ICMP socket object,ping request identifier,time out and destination address

    Output : Information of a ping response

    """
    timeLeft = timeout
    while True:
        startedSelect = time.time()
        whatReady = select.select([mySocket], [], [], timeLeft)
        howLongInSelect = (time.time() - startedSelect)
        if whatReady[0] == []:  # Timeout
            return "Request timed out."
        timeReceived = time.time()
        recPacket, addr = mySocket.recvfrom(1024)
        # Fetch the ICMP header from the IP packet
        icmpHeader = recPacket[20:28]#as first 20 bytes are ip header 
        type, code, checksum, packetID, sequence = struct.unpack("bbHHh", icmpHeader)
        
        # Handle ICMP Destination Unreachable errors (Type 3)
        if type == 3:
            if code == 0:
                return "Error: Network unreachable"
            elif code == 1:
                return "Error: Host unreachable"
            elif code == 2:
                return "Error: Protocol unreachable"
            elif code == 3:
                return "Error: Port unreachable"
            else:
                return f"Error: Destination unreachable, ICMP code {code}"

        # Calculate RTT
        sentTime = struct.unpack('d', recPacket[28:])[0]
        rtt = (timeReceived - sentTime) * 1000  # Convert to ms
        
        # Handle valid Echo Reply (Type 0)
        if packetID == ID:
            rtts.append(rtt)
            return f"Reply from {addr[0]}: time={rtt:.2f}ms"
        #to response if both the response or icmp error not recieved in time
        timeLeft = timeLeft - howLongInSelect
        if timeLeft <= 0:
            return "Request timed out."

def sendOnePing(mySocket, destAddr, ID):
    """
    Send one ping to the given destination address.

    Argument : ICMP socket object , destination address , ping request's identifier

    Output: Sends ICMP echo request to the dest. address

    """
    myChecksum = 0
    # Make a dummy header with a 0 checksum
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    data = struct.pack("d", time.time())
    # Calculate the checksum on the data and the dummy header.
    myChecksum = checksum(header + data)
    # Get the right checksum, and put it in the header
    if sys.platform == 'darwin':
        myChecksum = htons(myChecksum) & 0xffff
    else:
        myChecksum = htons(myChecksum)
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    packet = header + data
    mySocket.sendto(packet, (destAddr, 0))  # AF_INET address must be tuple, port is 0 for ICMP

def doOnePing(destAddr, timeout):
    """
    Perform a single ping operation.

    Argument : Destination address and maximum waiting of ping response

    Output : Round trip time of the ping

    """
    icmp = getprotobyname("icmp")
    # SOCK_RAW is a powerful socket type. For more details: http://sockraw.org/papers/sock_raw
    mySocket = socket(AF_INET, SOCK_RAW, icmp)
    myID = os.getpid() & 0xFFFF  # Return the current process ID
    sendOnePing(mySocket, destAddr, myID) #to send the packet
    delay = receiveOnePing(mySocket, myID, timeout, destAddr) # receive the packet 
    mySocket.close()
    return delay

def ping(host,numPing, timeout=1):
    """
    Ping a host and print the result.

    Argument : Host's IP address and the time-out time

    Output: Delay
    
    """
    dest = gethostbyname(host)
    print(f"Pinging {dest} using Python:")
    print("")
    # Send ping requests to the server at approximately one-second intervals.
    for i in range(numPing):
        delay = doOnePing(dest, timeout)
        print(delay)
        time.sleep(1)  # Pause for one second between sending packets.
    
    # Calculate and print statistics
    if rtts:
        min_rtt = min(rtts)
        max_rtt = max(rtts)
        avg_rtt = sum(rtts) / len(rtts)
        packet_loss_rate = ((numPing - len(rtts)) / numPing) * 100

        print(f"\nMinimum RTT: {min_rtt:.2f} ms")
        print(f"Maximum RTT: {max_rtt:.2f} ms")
        print(f"Average RTT: {avg_rtt:.2f} ms")
        print(f"Packet loss rate: {packet_loss_rate:.2f}%")
    else:
        print("No RTTs recorded.")
        print("Packet loss rate: 100%")
numPing=int(input("Enter number of pings :"))
ping("192.168.167.187",numPing)  
