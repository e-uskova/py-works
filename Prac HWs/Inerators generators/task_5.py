import functools


def check_arguments(*type_list):
    def check(func):
        @functools.wraps(func)
        def wrapper(*args):
            if len(args) < len(type_list):
                raise TypeError
            for i in range(len(type_list)):
                if not isinstance(args[i], type_list[i]):
                    raise TypeError
            func(*args)
        return wrapper
    return check
