# Logical operator
# and
# or
# not

# and
username="admin"
key="xyz"

result = username == "admin" and key == "xyz"
#         True               and True ==> True
print(f"Result username is admin and key is xyz: {result}")

key="abc"
result = username == "admin" and key == "xyz"
#         True               and False ==> False
print(f"Result username is admin and key is xyz: {result}")

"""
And
TRUE  TRUE  ==> True
TRUE  FALSE ==> False
FALSE TRUE ==> False
FALSE FALSE ==> False
"""

# or
username="manager"

result = username == "admin" or username == "root" or username == "manager"
print(f"Access Allowed: {result}")

"""
Or
TRUE  TRUE  ==> True
TRUE  FALSE ==> True
FALSE TRUE ==> True
FALSE FALSE ==> False
"""

# not (Reverse a condition)

username = "blocked"
result = not username != "blocked"  # False ==> True
print(f"User is not blocked: {result}")
result = username == "blocked"
print(f"User is not blocked: {result}")
