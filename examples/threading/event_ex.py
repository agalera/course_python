import threading
import time

event = threading.Event()


def example():
    print("thread waiting event")
    event.wait()
    print("event ok")


threads = [threading.Thread(target=example) for x in range(10)]

for thread in threads:
    thread.start()

time.sleep(2)
event.set()

for thread in threads:
    thread.join()
