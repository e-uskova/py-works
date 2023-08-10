import functools
ar = []


def substitutive(func):
    @functools.wraps(func)
    def wrapper(*args):
        global ar
        ar = ar + list(args)
        n = func.__code__.co_argcount
        if len(ar) == n:
            func(*ar)
            for a in args:
                ar.remove(a)
        elif len(ar) > n:
            raise TypeError
        else:
            return substitutive(func)
    return wrapper
