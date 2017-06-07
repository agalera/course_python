from scapy.all import *


res, unans = sr( IP(dst='192.168.1.2')/TCP(flags='S', dport=(1, 1024)))

res.summary()
