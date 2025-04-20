# this toturial we will cover Lists and Dictionaries in Python
# Lists are used to store multiple items in a single variable
# Lists are created using square brackets
# Lists are ordered, changeable, and allow duplicate values

# syntax for creating a list
# mylist = ["apple", "banana", "cherry"]

# Examples of Lists

# numbers = [1, 2, 3, 4, 5]  # Creating a list of numbers

# print(numbers)  # Output: [1, 2, 3, 4, 5]

# # to get first element of the list
# print(numbers[0])  # Output: 1
# # to get last element of the list
# print(numbers[-1])  # Output: 5
# # to get a range of elements
# print(numbers[1:3])  # Output: [2, 3]
# # to get the length of the list
# print(len(numbers))  # Output: 5
# # to add an element to the list
# numbers.append(6)  # Adding 6 to the list
# print(numbers)  # Output: [1, 2, 3, 4, 5, 6]
# # to remove an element from the list
# numbers.remove(3)  # Removing 3 from the list
# print(numbers)  # Output: [1, 2, 4, 5, 6]
# # to insert an element at a specific position in the list
# numbers.insert(2, 8)  # Inserting 3 at position 2 in the list
# print(numbers)  # Output: [1, 2, 3, 4, ]
# # to sort the list
# numbers.sort()  # Sorting the list
# print(numbers)  # Output: [1, 2, 4, 5, 6]
# # to reverse the list
# numbers.reverse()  # Reversing the list
# print(numbers)  # Output: [6, 5, 4, 2, 1]

# # to clear the list
# numbers.clear()  # Clearing the list
# print(numbers)  # Output: []
# # to copy the list
# numbers = [1, 2, 3, 4, 5]  # Creating a list of numbers
# numbers2 = numbers.copy()  # Copying the list
# print(numbers2)  # Output: [1, 2, 3, 4, 5]
# # Lists can contain different data types
# mixed_list = [1, "apple", 3.14, True]  # Creating a mixed list
# print(mixed_list)  # Output: [1, "apple", 3.14, True]
# # Lists can be nested
# nested_list = [1, 2, [3, 4], 5]  # Creating a nested list
# print(nested_list)  # Output: [1, 2, [3, 4], 5]
# # Lists can be sliced
# sliced_list = numbers[1:4]  # Slicing the list
# print(sliced_list)  # Output: [2, 3, 4]
# # Lists can be concatenated
# list1 = [1, 2, 3]  # Creating a list
# list2 = [4, 5, 6]  # Creating another list
# concatenated_list = list1 + list2  # Concatenating the lists
# print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]
# # Lists can be multiplied
# multiplied_list = list1 * 3  # Multiplying the list
# print(multiplied_list)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
# # Lists can be checked for membership
# print(1 in list1)  # Output: True
# print(4 in list1)  # Output: False


# Dictionaries are used to store data values in key:value pairs
# Dictionaries are created using curly braces{}
# Dictionaries are unordered, changeable, and do not allow duplicates
# syntax for creating a dictionary
# mydict = {"name": "John", "age": 30}
# Examples of Dictionaries

# Student = {
#     "name": "John",  # Creating a dictionary with key-value pairs
#     "age": 30,
#     "is_student": True,
#     "courses": ["Math", "Science", "English"],
#     "address": {
#         "street": "123 Main St",
#         "city": "New York",
#         "state": "NY",
#     },
# }  # Creating an  address dictionary within the student dictionary

# Output: {'name': 'John', 'age': 30, 'is_student': True, 'courses': ['Math', 'Science', 'English'], 'address': {'street': '123 Main St', 'city': 'New York', 'state': 'NY'}}
# print(Student)
# # # to get the value of a key
# print(Student["name"])  # Output: John
# # # to get the value of a nested key
# print(Student["address"]["city"])  # Output: New York
# # # to get the keys of the dictionary
# print(Student.keys())  # Output: dict_keys(['name', 'age', 'is_student', 'courses', 'address'])
# # # to get the values of the dictionary
# print(Student.values())  # Output: dict_values(['John', 30, True, ['Math', 'Science', 'English'], {'street': '123 Main St', 'city': 'New York', 'state': 'NY'}])
# # # to get the items of the dictionary
# print(Student.items())  # Output: dict_items([('name', 'John'), ('age', 30), ('is_student', True), ('courses', ['Math', 'Science', 'English']), ('address', {'street': '123 Main St', 'city': 'New York', 'state': 'NY'})])
# # # to add a new key-value pair to the dictionary
# Student["grade"] = "A"  # Adding a new key-value pair to the dictionary
# print(Student)  # Output: {'name': 'John', 'age': 30, '
# # # to update the value of a key
# Student["age"] = 31  # Updating the value of a key
# print(Student)  # Output: {'name': 'John', 'age': 31, 'is_student': True, 'courses': ['Math', 'Science', 'English'], 'address': {'street': '123 Main St', 'city': 'New York', 'state': 'NY'}, 'grade': 'A'}
# # to remove a key-value pair from the dictionary
# del Student["is_student"]  # Removing a key-value pair from the dictionary
# print(Student)  # Output: {'name': 'John', 'age': 31, 'courses': ['Math', 'Science', 'English'], 'address': {'street': '123 Main St', 'city': 'New York', 'state': 'NY'}, 'grade': 'A'}

# # to clear the dictionary
# Student.clear()  # Clearing the dictionary
# print(Student)  # Output: {}

# # to copy the dictionary
# Student2 = Student.copy()  # Copying the dictionary

# print(Student2)  # Output: {'name': 'John', 'age': 31, 'is_student': True, 'courses': ['Math', 'Science', 'English'], 'address': {'street': '123 Main St', 'city': 'New York', 'state': 'NY'}, 'grade': 'A'}
# # to check if a key exists in the dictionary
# print("name" in Student)  # Output: True

# what is  Sets
# Sets are used to store multiple items in a single variable
# Sets are created using curly braces{}

mysets = {1, 2, 3, 4, 5, 5}  # Creating a set
print(mysets)  # Output: {1, 2, 3, 4, 5}
