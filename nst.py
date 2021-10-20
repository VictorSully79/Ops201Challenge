# nst.py
# Victor Sullivan
# 20211019
# TCP Port Range Scanner that tests whether a TCP port is open or closed.

import sys
import socket
import random
import scapy
from scapy.all import sr1,IP,ICMP,TCP

host = "scranme.nmap.org"
port_range = [21, 22, 23]
src_port = 22
dst_port = 22
response = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0)

for dst_port in port_range:
    src_port = random.randint(1025,65534)

    if response is None:
        print("packet filtered")
    elif(response.haslayer(TCP)):
        if(response.getlayer(TCP).flags == 0x12):
            print("Port " + str(dst_port) + " is open")
        elif (response.getlayer(TCP).flag == 0x14):
            print("Port " + str(dst_port) + " is closed")
        else:
            print("The port is filtered and dropped")