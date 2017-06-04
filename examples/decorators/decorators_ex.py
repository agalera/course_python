import functools


def perms(perms):
    if isinstance(perms, str):
        perms = [perms]

    def decorator(func):  # it is called with a function to be decorated
        @functools.wraps(func)  # preserve original name, docstring, etc
        def wrapper(*args, **kwargs):
            # get user by cookies / headers and query db
            fake_user = {'username': 'pepito',
                         'perms': ['editor.delete', 'editor.upload']}
            for perm in perms:
                if perm not in fake_user['perms']:
                    raise "No perms"

            kwargs['user'] = fake_user
            return func(*args, **kwargs)  # call the original function
        return wrapper  # this will be assigned to the decorated name
    return decorator


@perms(['editor.upload', 'editor.delete'])
def my_func(user):
    print("user:", user)


def required_login(func):
    def wrapper(*args, **kwargs):
        kwargs['user'] = {'username': 'example'}
        return func(*args, **kwargs)
    # al devolver el wrapper, lo llaman pasandole los args, kwargs
    return wrapper


@required_login
def my_func2(user):
    print("user:", user)


my_func()
my_func2()
