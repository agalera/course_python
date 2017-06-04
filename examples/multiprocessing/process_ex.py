from multiprocessing import Process


def example():
    print("example")


t = Process(target=example).start()
t.start()
t.join()
