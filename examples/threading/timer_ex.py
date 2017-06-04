import threading


def hello():
    print("hello!")


t = threading.Timer(2, hello)
t.start()
print("waiting hello")
t.join()
