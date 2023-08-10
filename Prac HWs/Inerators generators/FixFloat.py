import functools


def fix(number):
    def wrap(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            new_args, new_kwargs = [], {}
            for arg in args:
                new_args.append(round(arg, number) if isinstance(arg, float) else arg)
            for key, value in kwargs.items():
                new_kwargs[key] = round(value, number) if isinstance(value, float) else value
            return round(func(*new_args, **new_kwargs), number)
        return wrapper
    return wrap
