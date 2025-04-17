# In this section we talk about or learn loops in python.
# Loops are used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects.
# Python has two primitive loop commands:
# 1. while loops
# 2. for loops
# The while loop:
# The while loop executes a set of statements as long as a condition is true.
# Syntax: while condition: statement(s)
# Example:
# counter = 0
# while counter <= 5:
#     print("Counter is:", counter)
#     counter += 1
# The for loop:
# The for loop is used for iterating over a sequence (like a list, tuple, dictionary, set, or string).
# With the for loop we can execute a set of statements, once for each item in a sequence.
# Syntax: for item in sequence: statement(s)
# Example:


# for i in range(1, 6):
#     print("Counter is:", i)

# # Reversed for loop
# for i in range(5, 0, -1):
#     print("Counter is:", i)
# Example of a for loop with a list
fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     if ("apple" in fruit):
#         print("Found apple")

#     elif ("banana" in fruit):
#         print("Found banana")

#     else:
#         print("Found something else")
#     # print(fruit)


# Reverseed for loop

# for fruit in reversed(fruits):
#     print(fruit)

# enumerate is used to loop over a list and get the index and value of each item

# for index,fruit in enumerate(fruits):
#     print(index, fruit)
#     # if (index == 1):
#     #     break

#  loops with dictionaries
# person = {
#     "name": "John",
#     "age": 30,
#     "city": "New York",
#     "address": {
#             "street": "123 Main St",
#             "zip": "10001"
#     }
# }

# for key, value in person.items():
#     print(key, value)

# loops with comperehensions
# comprehensions are a concise way to create lists, dictionaries, or sets in Python.
# squares = [x**2 for x in range(10)]
# print(squares)

# loop with zip()
# The zip() function is used to combine two or more iterables (like lists or tuples) into a single iterable.
# It returns an iterator of tuples, where each tuple contains the elements from the input iterables at the same index.

names = ["John", "Jane", "Jim"]
ages = [30, 25, 35]
for name, age in zip(names, ages):
    print(name, age)
