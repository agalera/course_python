print(range(10))
print(list(range(10)))


def example_generator():
    for x in range(10):
        print("gen new value")
        yield x * 2


for value in example_generator():
    print(value)


# bad plan
def new_id():
    n = 0
    while True:
        yield n
        n += 1


generator_id = new_id()

for x in range(100):
    print(generator_id.__next__())
