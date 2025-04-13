# Dict (key value data structure)
# name, email, age, group (for all the student)
# names = ["Aryan", "Mohit", "Karna"]
# emails = ["test@gmail.com", "m@gmail.com", "??"]
# age = [13, 25, 34]
# group = ["Alpha", "??", "Beta"]

my_dict = {
    "name": "Mohit",
    "age": 25,
    "is_active": True
}

# Fetch value by key index
print(my_dict["name"])
print(my_dict["age"])
print(my_dict["is_active"])

# if you are not sure that key will be present
# and you want to supply default value then we'll use get function
print(my_dict.get("email", "default@gmail.com"))

# Insert data to dict
my_dict["email"] = "mohit@gmail.com"
print(my_dict.get("email", "default@gmail.com"))

# Update data to dict
my_dict["age"] = 31
print(my_dict["age"])

# Remove age
my_dict.pop("age")
print("After deleting age key from my dict: ", my_dict)

# Remove name
del my_dict["name"]
print("After deleting name key from my dict: ", my_dict)

# Remove the last inserted item
my_dict.popitem()
print("After calling popitem my dict: ", my_dict)

# Clear all data from dict
my_dict.clear()
print("After calling clear my dict will be empty: ", my_dict)

my_dict_2 = {
    "aryan": "aryan@gmail.com",
    "mohit": "mohit@gmail.com",
    "karan": "karan@gmail.com"
}

# Loop

for key in my_dict_2:
    print(f"{key} ===> {my_dict_2[key]}")

print("===============================")

for key, value in my_dict_2.items():
    print(f"{key} ===> {value}")

print("===============================")

for key in my_dict_2.keys():
    print(key)

print("===============================")

for value in my_dict_2.values():
    print(value)

# name, email, age, group, is_active (for all the student)
# names = ["Aryan", "Mohit", "Karna"]
# emails = ["test@gmail.com", "m@gmail.com", "??"]
# age = [13, 25, 34]
# group = ["Alpha", "??", "Beta"]

# Key(String) ---> Value(Dict)
student_info_data = {
    "aryan@gmail.com": {
        "name": "Aryan",
        "age": 13,
        "email": "aryan@gmail.com",
        "group": "Alpha"
    },
    "mohit@gmail.com": {
        "name": "Mohit",
        "age": 31,
        "email": "mohit@gmail.com"
    },
    "karan@gmail.com": {
        "name": "Karan",
        "group": "Beta"
    }
}

print(student_info_data)

# Insert group data in Mohit info
mohit_info = student_info_data["mohit@gmail.com"]
mohit_info["group"] = "Beta"

print(student_info_data)

# Add age to karan data
karan_info = student_info_data["karan@gmail.com"]
karan_info["age"] = 21

# Add "is_active": True for aryan
student_info_data["aryan@gmail.com"]["is_active"] = True


# Loop over all the values in my dict
print("===== Loop over all the values in my dict =====")
for student in student_info_data.values():
    print(student)

# delete the key is_active from aryan

del student_info_data["aryan@gmail.com"]["is_active"]

print("===== Loop over all the values in my dict after deleting is_active key=====")
for student in student_info_data.values():
    print(student)