import threading
import time


barrier = threading.Barrier(2, timeout=20)


def worker():
    print("worker starting")
    time.sleep(10)
    print("worker started")
    print("waiting other workers")
    barrier.wait()
    print("worker ok")


def worker2():
    print("worker2 starting")
    time.sleep(1)
    print("worker2 started")
    print("waiting other workers")
    barrier.wait()
    print("worker2 ok")


t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=worker2)

t1.start()
t2.start()

t1.join()
t2.join()
