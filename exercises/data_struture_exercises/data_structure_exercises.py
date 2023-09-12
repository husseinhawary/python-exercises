"""
https://pynative.com/python-data-structure-exercise-for-beginners/
"""

"""
Exercise 1: Create a list 
by picking an odd-index items from the first list and even index items from the second

Given two lists, l1 and l2, write a program to create a third list 
l3 by picking an odd-index element from the list l1 and even index elements from the list l2.

Given:

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

Expected Output:

Element at odd-index positions from list one
[6, 12, 18]
Element at even-index positions from list two
[4, 12, 20, 28]

Printing Final third list
[6, 12, 18, 4, 12, 20, 28]
"""


def list_from_two_diff_lists(list_1, list_2):
    list_3 = []
    for i in range(len(list_1)):
        if i % 2 != 0:
            list_3.append(list_1[i])
    for i in range(len(list_2)):
        if i % 2 == 0:
            list_3.append(list_2[i])
    print(list_3)

    # Solution 2
    list_3_v2 = []
    for i, j in zip(list_1, list_2):
        list1_indices = list_1.index(i)
        list2_indices = list_2.index(j)
        if list1_indices % 2 != 0:
            list_3_v2.append(list_1[list1_indices])
        if list2_indices % 2 == 0:
            list_3_v2.append(list_2[list1_indices])
    print(list_3_v2)


list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
list_from_two_diff_lists(list1, list2)


# Map function
def calculate_addition(n):
    return n + n


numbers = (1, 2, 3, 4)
result = map(calculate_addition, numbers)
print(list(result))