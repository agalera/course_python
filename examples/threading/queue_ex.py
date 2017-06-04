import threading
import queue

queue = queue.Queue()


def worker():
    while True:
        print("wait new task")
        task = queue.get()
        print("run task", task)


threads = [threading.Thread(target=worker) for x in range(2)]


for x in range(100):
    queue.put(x)

for thread in threads:
    thread.start()


for thread in threads:
    thread.join()
