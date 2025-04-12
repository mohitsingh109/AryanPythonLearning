# Sets (unique value, unordered)

# Red-Black Tree (This is the reason why it's unique value, unordered)

# this store unique value only
departments = { "Aryan", "Mohit", "Aryan", "Mohit" }

print(departments)
departments.add("Rohit")
print(departments)
#departments.add("Rohit")
#departments.add("Rohit")
#departments.add("Rohit")
#departments.add("Rohit")
departments.add("Karan")
print(departments)

departments.remove("Karan")

# It is not supported operation unordered
# print(departments[0])

for dep in departments:
    print(dep)
