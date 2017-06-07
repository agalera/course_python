from scapy.all import *
output=sr(IP(dst='google.com')/ICMP())
print ('Output is:', output)
result, unanswered=output
print('Result is:', result)
