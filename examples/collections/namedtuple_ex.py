from collections import namedtuple


Point = namedtuple('point', ['x', 'y'], verbose=True)

p1 = Point(10, 20)
print(p1)
