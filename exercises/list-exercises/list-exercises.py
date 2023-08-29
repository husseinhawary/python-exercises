"""
https://pynative.com/python-list-exercise-with-solutions/
"""

"""
Exercise 1: Reverse a list in Python
Given:
list1 = [100, 200, 300, 400, 500]
Expected output:
[500, 400, 300, 200, 100]
"""


def reverse_list_solution_1(items_list):
    items_list.reverse()
    print(items_list)


def reverse_list_solution_2(items_list):
    print(items_list[:: -1])


list_items = [100, 200, 300, 400, 500]
list_items2 = [100, 200, 300, 400, 500]
reverse_list_solution_1(list_items)
reverse_list_solution_2(list_items2)

"""
Exercise 2: Concatenate two lists index-wise
Write a program to add two lists index-wise. Create a new list that contains
the 0th index item from both the list,then the 1st index item, and so on till
the last element. any leftover items will get added at the end of the new list.

Given:
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
Expected output:
['My', 'name', 'is', 'Kelly']
"""


def concatenate_two_lists(list_1, list_2):
    """
    Use the zip() function. This function takes two or more iterables (like list, dict, string),
    aggregates them in a tuple, and returns it.
    """
    list_3 = [i + j for i, j in zip(list_1, list_2)]
    print(list_3)


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
concatenate_two_lists(list1, list2)

"""
Exercise 3: Turn every item of a list into its square
Given a list of numbers. write a program to turn every item of a list into its square.

Given:

numbers = [1, 2, 3, 4, 5, 6, 7]
Expected output:

[1, 4, 9, 16, 25, 36, 49]
"""


def calculate_square(numbers):
    squares = []
    for number in numbers:
        square = number * number
        squares.append(square)
    print(squares)

    # Second Solution
    # squares_v2 = [number * number for number in numbers]
    # print(squares_v2)


calculate_square([1, 2, 3, 4, 5, 6, 7])



"""
Exercise 4: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
Expected output:

['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
"""


def concatenate_two_list_strings(list_1, list_2):
    list_3 = []
    for i in list_1:
        for j in list_2:
            list_3.append(i + j)
    print(list_3)
    # Solution 2
    concatenated_list = [i + j for i in list_1 for j in list_2]
    print(concatenated_list)


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
concatenate_two_list_strings(list1, list2)


"""
Exercise 5: Iterate both lists simultaneously
Given a two Python list. Write a program to iterate both lists simultaneously
and display items from list1 in original order and items from list2 in reverse order.

Given
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
Expected output:
10 400
20 300
30 200
40 100
"""


def iterate_over_two_lists_simultaneously(list_1, list_2):
    for i, j in zip(list_1, list_2[:: -1]):
        print(i, j)


list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
iterate_over_two_lists_simultaneously(list1, list2)