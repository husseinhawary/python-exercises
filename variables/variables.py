a = 50
b = a

print(id(a))
print(id(b))

a = 500

print(id(a))

# recommended variable name
# Camel Case -> nameOfStudents
# Pascal Case -> NameOfStudents
# Snake Case -> name_of_students

# global variable

x = 101


def main_function():
    global x
    print(x)

    x = "welcome to javatpoint"
    print(x)


main_function()
print(x)

y = 3

print(y ** 2)

tuple_ = ("Python", "Loops", "Sequence", "Condition", "Range")

# iterating over tuple_ using range() function
for iterator in range(len(tuple_)):
    print(iterator)     # this will print the index
    print(tuple_[iterator].upper())


i = 1
while i <= 10:
    print(i, end=" ")
    i += 1

print("*" * 50, end=" ")

my_list = [1, 2, 3, 4]
count = 1
for item in my_list:
    if item == 4:
        print("Item matched")
        count += 1
        break
print("Found at location", count)

names = ["Hussein", "Anas"]

new_name = "#".join(names)

print(new_name)
print(new_name.split("#"))

name = "hussein"
print(name.split())

# print duplicated

list_1 = [1, 2, 3, 4, 1, 3]
list_2 = []

for item in list_1:
    if item not in list_2:
        list_2.append(item)

print(list_2)

for i in range(len(list_1)):
    for j in range(i + 1, len(list_1)):
        if list_1[i] == list_1[j]:
            print("duplicated")


def get_duplicated_items(numbers):
    for number in range(len(numbers)):
        for num in range(number + 1, len(numbers)):
            if numbers[number] == numbers[num]:
                print(f"{numbers[number]} number is duplicated")


get_duplicated_items(list_1)