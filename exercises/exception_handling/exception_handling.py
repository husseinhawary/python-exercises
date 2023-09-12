a = ["Python", "Exceptions", "try and except"]
try:
    for i in range(4):
        print(a[i])
except IndexError:
    print("index out of range")
finally:
    print("end of try-except block")

num = [3, 4, 5, 7]
if len(num) > 3:
    raise Exception(f"Length of the given list must be less than or equal to 3 but is {len(num)}")
