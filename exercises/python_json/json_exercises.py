import json

student = {
    "Name": "Peter",
    "Roll_no": "0090014",
    "Grade": "A",
    "Age": 20,
    "Subject": ["Computer Graphics", "Discrete Mathematics", "Data Structure"]
}

# Write data into json file
with open("data.json", "w") as json_file:
    json.dump(student, json_file)

json_object = json.dumps(student)
print(json_object)

# convert python list into json array
print(json.dumps(["Python", "Java", "C++"]))

# Deserialization
a = (10, 20, 30, 40, 50, 60, 70)
print(type(a))
b = json.dumps(a)
print(type(json.loads(b)))


# Read data from json file
with open("data.json", "r") as json_file:
    json_file_reader = json.load(json_file)
    print(json_file_reader)