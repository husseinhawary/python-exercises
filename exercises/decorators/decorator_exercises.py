from decorator_with_arguments import do_twice
# inner functions before the decorator itself


def func():
    print("We are in first function")

    def func1():
        print("This is the first child function")

    def func2():
        print("This is the second child function")

    func1()
    func2()


func()


# Higher order function -> the function which takes another function as an arguments

def add(x):
    return x + 1


def sub(x):
    return x - 1


def operator(fun, x):
    return fun(x)


print(operator(add, 10))
print(operator(sub, 10))


def outer_div(fun):
    def inner(x, y):
        if x < y:
            x, y = y, x
            return fun(x, y)
    return inner


@outer_div
def divide(x, y):
    print(x / y)


divide(2, 4)


@do_twice
def display(name):
    print(f"Hello {name}")


display("Hussein")