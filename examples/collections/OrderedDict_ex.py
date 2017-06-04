from collections import OrderedDict
from random import randrange
from pprint import pprint


d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

OrderedDict(sorted(d.items(), key=lambda t: t[1]))

od = OrderedDict()
for x in range(10):
    od["example_%s_%s" % (randrange(10), x)] = x

pprint(od)
