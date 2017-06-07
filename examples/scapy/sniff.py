from scapy.all import *


p = sniff(iface='eth0', timeout=10, count=5)
p.summary()
