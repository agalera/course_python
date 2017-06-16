import threading
import queue
from time import sleep


queue = queue.Queue()
try_list = []


def worker():
    name = threading.currentThread().name
    sleep(1)
    if name == "write":
        print("write")
        for x in range(1000):
            try_list.append(x)
            sleep(0.1)
        print("finish write")
    elif name == "read":
        sleep(1)
        print("read")
        for x in try_list:
            print(x)
            sleep(0.05)


threads = []
threads.append(threading.Thread(target=worker, name='write'))
threads.append(threading.Thread(target=worker, name='read'))

for thread in threads:
    thread.start()


for thread in threads:
    thread.join()


from pprint import pprint