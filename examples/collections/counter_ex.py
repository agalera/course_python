from collections import Counter
from pprint import pprint

# create counter, example 1, manual insert
cnt = Counter()

for color in ["red", "blue", "red"]:
    cnt[color] += 1

pprint(cnt)

# create counter, example 2, use list
cnt = Counter(["red", "blue", "red"])

pprint(cnt)

# create counter, example 3, use dict
cnt = Counter({"red": 2, "blue": 1})

pprint(cnt)

# create counter, example 4, use kwargs
cnt = Counter(red=2, blue=1)

pprint(cnt.most_common(3))

# create counter, example 5, use string
cnt = Counter("hello world")

pprint(cnt.most_common(3))

# subtract
cnt = Counter(red=10, blue=5)
cnt.subtract(Counter(red=5, blue=1))
pprint(cnt)

# elements
cnt = Counter(red=10, blue=5)
pprint(list(cnt.elements()))
