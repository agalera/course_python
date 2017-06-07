from scapy.all import *


res, unans = traceroute(["www.microsoft.com","www.cisco.com","www.yahoo.com","www.wanadoo.fr","www.pacsec.com"],dport=[80,443],maxttl=20,retry=-2)


res.graph()
res.graph(type="ps",target="| lp")
res.graph(target="> /tmp/graph.svg")

