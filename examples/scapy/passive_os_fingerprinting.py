from scapy.all import *


load_module('p0f')
print(sniff(prn=prnp0f))

