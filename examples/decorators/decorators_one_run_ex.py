events = {}

def subscribe(event):
    def decorator(func):
        print('add event')
        events[event] = func
        return func
    return decorator


@subscribe('example')
def example():
    return


example()
example()
