import threading
import time


sem = threading.Semaphore(2)


def example2():
    with sem:
        print("in with")
        time.sleep(1)
    print("release")


threads = []

for x in range(10):
    threads.append(threading.Thread(target=example2))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
