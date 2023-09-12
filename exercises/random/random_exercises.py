import random


def rand_rand():
    num = random.random()
    print(num)


rand_rand()


def rand_int(start, end):
    num = random.randint(start, end)
    print(num)


rand_int(1, 500)


def rand_range(*args):
    num = random.randrange(*args)
    print(num)


rand_range(1, 10)
rand_range(1, 10, 2)


def rand_choice(*args):
    num = random.choice(*args)
    print(num)


rand_choice("Random Module")
rand_choice([23, 54, 765, 23, 45, 45])
rand_choice((12, 64, 23, 54, 34))


def rand_shuffle(list_shuffle):
    random.shuffle(list_shuffle)
    print(list_shuffle)


rand_shuffle([34, 23, 65, 86, 23, 43])
