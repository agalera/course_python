import threading
import queue
import requests


q = queue.Queue()
sem = threading.BoundedSemaphore(20)
lock = threading.Lock()
result = 0

r = requests.get('http://firecarrot.com:9000').json()['result']
for url in r:
    q.put(url)


def worker():
    global result
    request = requests.Session()
    while True:
        try:
            url = q.get(timeout=10)
        except queue.Empty:
            break

        with sem:
            print("get", url)
            r = request.get(url)

        r = r.json()['result']
        with lock:
            result += r


threads = []

for x in range(40):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(result)  # 333283335000
