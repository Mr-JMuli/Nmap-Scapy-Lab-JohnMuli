from scapy.all import *

packet = IP(dst="192.168.1.10")/ICMP()
send(packet)

print("ICMP packet sent")
