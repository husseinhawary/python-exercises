"""
Exercises Link -> https://pynative.com/python-functions-exercise-with-solutions/
"""

"""
Exercise 1: Create a function in Python
Write a program to create a function that takes two arguments, name and age, and print their value.
"""


def user_info(name, age):
    print(name, age)


user_info("Hussein", "31")

"""
Exercise 2: Create a function with variable length of arguments
"""


def func1(*args):
    for i in args:
        print(i)


func1(20, 30)
func1(40, 50, 60)
func1("Hussein")


"""
Exercise 3: Return multiple values from a function
Write a program to create function calculation() such that it 
can accept two variables and calculate addition and subtraction.
Also, it must return both addition and subtraction in a single return call.
"""


def calculation(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction


add, sub = calculation(40, 10)
print(add, sub)

"""
Exercise 6: Create a recursive function
Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
"""


def addition(num):
    if num:
        return num + addition(num - 1)
    else:
        return 0


print(addition(10))
