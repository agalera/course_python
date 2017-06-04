from collections import defaultdict
from pprint import pprint

d = defaultdict(list)
for yellow_food in ['banana', 'lemon']:
    d['yellow'].append(yellow_food)
d['red'].append("apple")
d['red'].append("tomato")

pprint(d)

colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

d = defaultdict(list)
for k, v in colors:
    d[k].append(v)

pprint(d.items())
