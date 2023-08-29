"""
https://pynative.com/python-dictionary-exercise-with-solutions/
"""
"""
Exercise 1: Convert two lists into a dictionary
Below are the two lists. Write a Python program to convert them into a dictionary
in a way that item from list1 is the key and item from list2 is the value

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Expected output:

{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
"""


def convert_two_lists_into_dict(list_1, list_2):
    res_dict = dict(zip(list_1, list_2))
    print(res_dict)

    # Solution 2
    res_dict_v2 = dict()
    for i in range(len(list_1)):
        res_dict_v2.update({list_1[i]: list_2[i]})
    print(res_dict_v2)


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
convert_two_lists_into_dict(keys, values)

"""
Exercise 2: Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
Expected output:

{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
"""


def merge_two_dict(dict_1, dict_2):
    dict_3 = {**dict_1, **dict_2}
    print(dict_3)

    # Solution 2
    dict3_v2 = dict_1.copy()
    dict3_v2.update(dict_2)
    print(dict3_v2)


dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
merge_two_dict(dict1, dict2)