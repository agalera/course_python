from contextlib import contextmanager, ContextDecorator


@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


with tag("h1"):
    print("foo")


class mycontext(ContextDecorator):
    def __enter__(self):
        print('Starting')
        return self

    def __exit__(self, *exc):
        print('Finishing')
        return False


@mycontext()
def fnc():
    print("holaa")


fnc()


with mycontext():
    print("hola")
