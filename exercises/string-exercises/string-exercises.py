"""
Exercise 1A: Create a string made of the first, middle and last character
Write a program to create a new string made of an input string’s first, middle, and last character.
"""


def get_first_mid_last_char_from_string(given_string):
    first_letter = given_string[0]
    mid_letter = given_string[int(len(given_string) / 2)]
    last_letter = given_string[-1]
    print(first_letter + mid_letter + last_letter)


get_first_mid_last_char_from_string("Anas")

"""
Exercise 4: Arrange string characters such that lowercase letters should come first
"""


def arrange_string_chars(user_string):
    lower = []
    upper = []

    for char in user_string:
        if char.islower():
            lower.append(char)
        else:
            upper.append(char)

    sorted_string = "".join(lower + upper)
    print(f"Sorted string {sorted_string}")


arrange_string_chars("PYnAtivE")

"""
Exercise 5: Count all letters, digits, and special symbols from a given string
Given:

str1 = "P@#yn26at^&i5ve"
"""


def count_letters_digits_symbols(given_string):
    letters_count = 0
    digits_count = 0
    symbols_count = 0

    for item in given_string:
        if item.isalpha():
            letters_count += 1
        elif item.isdigit():
            digits_count += 1
        else:
            symbols_count += 1
    print(f"Letters count is :- {letters_count}")
    print(f"Digits count is :- {digits_count}")
    print(f"Symbols count is :- {symbols_count}")


count_letters_digits_symbols("P@#yn26at^&i5ve")

print("************ Exercise 6 ****************")
"""
Exercise 6: Create a mixed String using the following rules
Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1,
then the last char of s2, Next, the second char of s1 and second last char of s2, 
and so on. Any leftover chars go at the end of the result.
"""

print("************ Exercise 7 ****************")
"""
Exercise 7: String characters balance Test
Write a program to check if two strings are balanced. 
For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2.
The character’s position does not matter.
"""


def check_two_string_balance(given_string_1, given_string_2):
    is_balanced = True
    for s1 in given_string_1:
        if s1 in given_string_2:
            continue
        else:
            is_balanced = False
    print(f"Are the two strings balanced ? {is_balanced}")


check_two_string_balance("Yn", "PYnative")

print("************ Exercise 8 ****************")
"""
Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
Write a program to find all occurrences of “USA” in a given string ignoring the case.
"""


def count_sting_occurrency():
    string_1 = "Welcome to USA. usa awesome, isn't it?"
    sub_string = "USA"

    temp_string = string_1.lower()
    count = temp_string.count(sub_string.lower())
    print(f"Count of USA is:- {count}")


count_sting_occurrency()

print("************ Exercise 9 ****************")
"""
Exercise 9: Calculate the sum and average of the digits present in a string
Given a string s1, write a program to return the sum and average 
of the digits that appear in the string, ignoring all other characters.
"""


def calc_sum_and_average(given_string):
    count = 0
    sum_value = 0
    for char in given_string:
        if char.isdigit():
            count += 1
            sum_value += int(char)
    average = sum_value / count

    print(f"Sum value = {sum_value}")
    print(f"Average value = {average}")


calc_sum_and_average("PYnative29@#8496")

print("************ Exercise 10 ****************")
"""
Exercise 10: Write a program to count occurrences of all characters within a string
"""


def count_char_occurrency(given_sting):
    char_dict = {}
    for char in given_sting:
        char_count = given_sting.count(char)
        char_dict[char] = char_count
    print(char_dict)


count_char_occurrency("Hussein")

print("************ Exercise 11 ****************")
"""
Exercise 11: Reverse a given string
"""


def reverse_string(given_string):
    reversed_string = given_string[-1:: -1]
    reversed_string = "".join(reversed(given_string))
    print(reversed_string)


reverse_string("PYnative")


print("************ Exercise 12 ****************")
"""
Exercise 12: Find the last position of a given substring
Write a program to find the last position of a substring “Emma” in a given string.

Given:

str1 = "Emma is a data scientist who knows Python. Emma works at google."
"""


def get_last_position_of_substring(given_string, sub_string):
    # The rfind() method finds the last occurrence of the specified value
    return given_string.rfind(sub_string)


main_str = "Emma is a data scientist who knows Python. Emma works at google."
sub_str = "Emma"
print(get_last_position_of_substring(main_str, sub_str))


print("************ Exercise 13 ****************")
"""
Exercise 13: Split a string on hyphens
Write a program to split a given string on hyphens and display each substring.

Given:

str1 = Emma-is-a-data-scientist
"""


def split_sting_based_on_delimiter(given_string, delimiter):
    strings = given_string.split(delimiter)
    print(strings)
    for string in strings:
        print(string)


split_sting_based_on_delimiter("Emma-is-a-data-scientist", "-")


print("************ Exercise 14 ****************")
"""
Exercise 14: Remove empty strings from a list of strings
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
"""


def remove_empty_string_from_list_solution_1(strings):
    for string in strings:
        if string == "" or string is None:
            strings.remove(string)
    print(strings)


def remove_empty_string_from_list_solution_2(strings):
    filtered_list = []
    for string in strings:
        if string:
            filtered_list.append(string)

    print(filtered_list)


def remove_empty_string_from_list_solution_3(strings):
    filtered_list = list(filter(None, strings))
    print(filtered_list)


str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
remove_empty_string_from_list_solution_1(str_list)
remove_empty_string_from_list_solution_2(str_list)
remove_empty_string_from_list_solution_3(str_list)