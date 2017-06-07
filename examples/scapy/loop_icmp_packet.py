from scapy.all import *


srloop(IP(dst="www.goog")/ICMP(), count=3)
