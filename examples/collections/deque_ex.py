from collections import deque


d = deque("example")
for letter in d:
    print(letter.upper())

d.appendleft("yep ")
print(d)

d.append("!!")
print(d)

print(d.pop())

print(d.popleft())

d.extend('awesome')
print(d)

d.extendleft('wow')
print(d)


print(d.rotate(1))

print(d.rotate(-1))

print(deque(reversed(d)))

d.clear()

try:
    d.pop()
except IndexError:
    print("deque is empty")

