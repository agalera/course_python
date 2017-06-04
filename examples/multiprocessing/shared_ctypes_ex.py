from multiprocessing import Process, Value
from ctypes import *


def worker(counter):
    for x in range(1000):
        with counter:
            counter.value += 1


counter = Value(c_int)

threads = []
for x in range(100):
    threads.append(Process(target=worker, args=(counter, )))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(counter.value)
