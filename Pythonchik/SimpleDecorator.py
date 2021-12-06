import functools


def nonify(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if func(*args, **kwargs):
            return func(*args, **kwargs)
        else:
            return 
    return wrapper
