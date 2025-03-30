# List == Array
students = ["Aryan", "Mohit", "Karan"]
#               0       1       2
#              -3      -2      -1

print(students)

# first value
print(students[0])

# Print mohit
print(students[-2])

# Add Bob
students.append("Bob")

# Remove karan
students.remove("Karan")

print(len(students))

# List Slicing & Iteration
team_member = ["John", "Emma", "Ryan", "Sophia", "Unknown"]

print(team_member[1:3]) # "Emma", "Ryan"
print(team_member[1:])  # "Emma", "Ryan", "Sophia"
print(team_member[:3])  # "John", "Emma", "Ryan"
print(team_member[:-1]) # "John", "Emma", "Ryan"
print(team_member[3:])  # "Sophia"
print(team_member[-1:]) # "Sophia"
print(team_member[::-1]) # Rever your array

# Loop list in python
for member in team_member:
    print("Hi,", member)

# Check if my array contains Unknown
for member in team_member:
    if member == "Unknown":
        print("Yes it contains Unknown")

# Add all number
numbers = [10, 15, 60, 70]
total = 0

for num in numbers:
    total += num

print("Total", total)
