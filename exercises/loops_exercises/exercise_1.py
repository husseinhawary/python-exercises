"""
The below link is the exercise's link
Python Loop Exercise - https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/
"""

"""
Exercise 1: Print First 10 natural numbers using while loop
"""


def print_first_10_natural_numbers():
    i = 1
    while i <= 10:
        print(i)
        i += 1


print_first_10_natural_numbers()

print("************ Exercise 2 ****************")

"""
Exercise 2: Print the following pattern
Write a program to print the following number pattern using a loop.

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
"""


def print_the_above_patters(numbers):
    for i in range(1, numbers):
        for j in range(1, i + 1):
            print(j, end=" ")
        print("")


print_the_above_patters(6)

print("************ Exercise 3 ****************")

"""
Exercise 3: Calculate the sum of all numbers from 1 to a given number
Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
"""

# def calculate_sum_numbers():
#     given_number = int(input("Enter number: "))
#     # total = 0
#     # for num in range(1, given_number + 1):
#     #     total += num
#     # print(f"Sum is {total}")
#
#     # Second Solution
#     total = sum(range(1, given_number + 1))
#     print(f"Sum is {total}")
#
#
# calculate_sum_numbers()
#
# print("************ Exercise 4 ****************")

"""
Exercise 4: Write a program to print multiplication table of a given number
For example, num = 2 so the output should be

2
4
6
8
10
12
14
16
18
20
"""

# def print_multiplication():
#     number = int(input("Enter number: "))
#
#     for num in range(1, 11):
#         multiplication = number * num
#         print(multiplication)
#
#
# print_multiplication()
#
# print("************ Exercise 5 ****************")

"""
Exercise 5: Display numbers from a list using loop
The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop
"""

# def display_list(numbers):
#     for number in numbers:
#         if number > 500:
#             break
#         elif number > 150:
#             continue
#         elif number % 5 == 0:
#             print(number)
#
#
# display_list([12, 75, 150, 180, 145, 525, 50])


print("************ Exercise 6 ****************")

"""
Exercise 6: Count the total number of digits in a number
For example, the number is 75869, so the output should be 5.
"""


def count_digits(digits):
    count = 0
    while digits != 0:
        # the floor division // rounds the result down to the nearest whole number
        digits = digits // 10
        count += 1
    print(count)


count_digits(75869)

print("************ Exercise 7 ****************")

"""
Exercise 7: Print the following pattern
Write a program to use for loop to print the following reverse number pattern

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
"""


def print_patters_reversed(numbers):
    for i in range(1, numbers):
        for j in range(numbers - i, 0, -1):
            print(j, end=" ")
        print(" ")


print_patters_reversed(6)

print("************ Exercise 8 ****************")

"""
Exercise 8: Print list in reverse order using a loop
"""


def reverse_list_solution_1(list):
    reversed_list = reversed(list)
    for item in reversed_list:
        print(item)


def reverse_list_solution_2(list):
    for item in range(len(list) - 1, -1, -1):
        print(list[item])


reverse_list_solution_1([10, 20, 30, 40, 50])
print("****** Solution 2 ********")
reverse_list_solution_2([10, 20, 30, 40, 50])

print("************ Exercise 9 ****************")

for number in range(-10, 0):
    print(number)

print("************ Exercise 10 ****************")
for number in range(5):
    print(number)
else:
    print("Done")

print("************ Exercise 11 ****************")
"""
Exercise 11: Write a program to display all prime numbers within a range
"""


def get_prime_numbers_within_range(start, end):
    for num in range(start, end + 1):
        if num > 1:
            # Check for factors
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(f"{num} is a prime number")
        else:
            print("Invalid prime number")


get_prime_numbers_within_range(25, 50)


def check_prime_number(num):
    if num > 1:
        for factor in range(2, num):
            if num % factor == 0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")


check_prime_number(11)


print("************ Exercise 12 ****************")

"""
Exercise 12: Display Fibonacci series up to 10 terms
The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.

For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.
"""


def print_fibonacci_series(target_number):
    first_number = 0
    second_number = 1
    for num in range(target_number):
        print(first_number, end=" ")
        result = first_number + second_number
        first_number = second_number
        second_number = result
    else:
        print("")



print_fibonacci_series(10)



print("************ Exercise 13 ****************")
"""
Exercise 13: Find the factorial of a given number
5! = 5 × 4 × 3 × 2 × 1 = 120
"""


def calc_factorial(given_number):
    fact = 1
    for num in range(1, given_number + 1):
        fact *= num
    else:
        print(fact)


calc_factorial(5)


print("************ Exercise 14 ****************")
"""
Exercise 14: Reverse a given integer number
"""


def reverse_integer(num):
    reversed_number = 0
    while num > 0:
        remaining = num % 10
        reversed_number = (reversed_number * 10) + remaining
        num = num // 10
    else:
        print(reversed_number)


reverse_integer(12345)


print("************ Exercise 15 ****************")
"""
Exercise 15: Use a loop to display elements from a given list present at odd index positions
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Note: list index always starts at 0

Expected output:

20 40 60 80 100
"""


def print_list_odd_index(numbers):
    for num in range(len(numbers) + 1):
        if num % 2 != 0:
            print(numbers[num], end=" ")


print_list_odd_index([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])


print("************ Exercise 16 ****************")
"""
Exercise 16: Calculate the cube of all numbers from 1 to a given number
"""


def calc_cube(given_number):
    for num in range(1, given_number + 1):
        cube = num ** 3
        print(f"Current number is {num} and the cube is {cube}")


calc_cube(6)



print("************ Exercise 17 ****************")
"""
Exercise 17: Find the sum of the series upto n terms
Write a program to calculate the sum of series up to n term. For example,
if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
"""


def calc_sum_of_series_up_n_number_solution_1(given_number, n):
    total_sum = 0
    for num in range(1, n + 1):
        repeated_number = given_number * num
        total_sum += int(repeated_number)
    else:
        print(total_sum)


def calc_sum_of_series_up_n_number_solution_2(given_number, n):
    total_sum = 0
    original_number = given_number
    for num in range(1, n + 1):
        total_sum += given_number
        given_number = (given_number * 10) + original_number
    else:
        print(total_sum)



calc_sum_of_series_up_n_number_solution_1("2", 5)
calc_sum_of_series_up_n_number_solution_2(2, 5)



for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    else:
        print("")
for i in range(5, 1, -1):
    for j in range(1, i):
        print("*", end=" ")
    else:
        print("")

