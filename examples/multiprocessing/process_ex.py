from multiprocessing import Process


def example():
    print("example")


t = Process(target=example)
t.start()
t.join()
