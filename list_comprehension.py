# task = input("Enter the task type: ")
#
# if task not in ["T1", "T2", "T3", "T4"]:
#     print("Invalid input")
# else:
#     print("Ahww... Correct input")

# 0 to 10 you have to give [0, 1, 4, 9, 16 .....]
result = []
for i in range(11):
    result.append(i ** 2)
print(result)

squares = [i ** 2 for i in range(11)]
print(squares)

# 0 to 20 [0, 2, 4, 6, ... 20]
evens = [i for i in range(21) if i % 2 == 0]
print(evens)

words = ["apple", "banana", "cherry"]
# [a, b, c]
first_letters = [word[0] for word in words]
print(first_letters)

keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']

my_dict = { k:v for k, v in zip(keys, values) }
print(my_dict)

# Remove Vowels from a string
text = "hello world"
# hll wrld
no_vowels = ''.join([char for char in text if char not in 'aeiou'])
print(no_vowels)

emails = ["t1@gmail.com", "t2@gmail.com", "t3@gmail.com"]

print(', '.join(emails))