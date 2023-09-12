"""
filter() function
"""


def filter_data(x):
    if x > 5:
        return x


result = filter(filter_data, [1, 2, 6])
print(list(result))


# filter not empty strings
def filter_not_empty_strings(strings):
    not_empty_strings = list(filter(lambda string: string != "", strings))
    return not_empty_strings


strings_list = ['', 'hello', '', 'world', '']
print(filter_not_empty_strings(strings_list))


# Filter out negative numbers from a list:
def filter_negative_numbers(numbers):
    negative_numbers = list(filter(lambda num: num > 0, numbers))
    return negative_numbers


numbers_list = [1, -2, 3, -4, 5, -6]
print(filter_negative_numbers(numbers_list))


# Filter out duplicates from a list:
def filter_out_duplicated_numbers(numbers):
    unique_numbers = list(filter(lambda number: numbers.count(number) == 1, numbers))
    return unique_numbers


print(filter_out_duplicated_numbers([1, 2, 3, 2, 4, 3, 5]))


# Filter the duplicated numbers only and print them
def filter_duplicated_numbers(numbers):
    duplicated_numbers = set(filter(lambda num: numbers.count(num) > 1, numbers))
    for n in duplicated_numbers:
        print(n)


filter_duplicated_numbers([1, 2, 3, 2, 4, 3, 5])

"""
map() function -> returns a list of elements 
after performing operation on the sequence elements (list, tuble, string)
"""


# Example 1: Utilizing map() to square a list of numbers

def calc_squares(numbers):
    squares = list(map(lambda n: n ** 2, numbers))
    print(squares)


calc_squares([1, 2, 3, 4, 5])


def calc_squares_in_range():
    squares = [lambda num=num: num ** 2 for num in range(0, 11)]
    print(list(squares))
    for square in squares:
        print('The square values all numbers from 0 to 10:', square(), end=" ")


calc_squares_in_range()
