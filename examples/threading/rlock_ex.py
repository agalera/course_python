import threading


rlock = threading.RLock()


def example2(values):
    if not values:
        return

    with rlock:
        print("in lock")
        values.pop()
        example2(values)


threads = []

for x in range(10):
    threads.append(threading.Thread(target=example2, args=(list(range(5)),)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
