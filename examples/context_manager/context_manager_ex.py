from contextlib import contextmanager, ContextDecorator


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
