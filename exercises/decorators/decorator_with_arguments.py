def do_twice(func):
    def wrapper_function(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_function

