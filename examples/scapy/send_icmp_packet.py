from scapy.all import *
packet = IP(dst="192.168.1.2")/ICMP()/"Helloooo!"
send(packet)
packet.show()
