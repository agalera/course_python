import threading
import time


lock = threading.Lock()


def example():
    print("waiting acquire")
    lock.acquire()
    print("in thread!!!")
    time.sleep(2)
    print("release")
    lock.release()


def example2():
    print("waiting acquire")
    with lock:
        print("in thread!!!")
        time.sleep(2)
    print("release")


threads = [threading.Thread(target=example2) for x in range(10)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
