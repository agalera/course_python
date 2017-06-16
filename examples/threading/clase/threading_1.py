import threading
from time import sleep


sem = threading.Semaphore(2)


def example(values):
    with sem:
        print("launch request")
        sleep(2)
        print("finish request")


threads = []

for x in range(10):
    threads.append(threading.Thread(target=example, args=(list(range(5)),)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
