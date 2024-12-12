# Importing Scapy
from scapy.all import ARP, Ether, srp

# Target IP
target_ip = input("Enter the target IP (e.g., 192.168.1.0/24): ")

# Create an ARP packet and an Ethernet frame
arp = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether / arp

# Send the packet and capture the responses
result = srp(packet, timeout=3, verbose=0)[0]

# Print the IP and MAC of each discovered device
print("Available devices on the network:")
print("IP" + " "*18+"MAC")
for sent, received in result:
    print(f"{received.psrc}\t\t{received.hwsrc}")

