import threading


def in_thread():
    print(threading.get_ident())


threading.Thread(target=in_thread).start()


class Example(threading.Thread):
    def run(self):
        for x in range(10):
            print(threading.get_ident(), x)


t = Example()
t.start()
t.join()
