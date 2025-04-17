# first command
# Python is a high-level, interpreted programming language that is widely used for web development, data analysis, artificial intelligence, scientific computing, and more.

# Python is known for its simplicity and readability, making it a great choice for beginners and experienced programmers alike.
# Python is an interpreted language, which means that the code is executed line by line, rather than being compiled into machine code before execution.
# python is case sensitive language
# Python is an object-oriented language, which means that it allows you to create and manipulate objects, which are instances of classes.

print("Hello World")  # this is pre defined function that used to print the output

# Variables
# Variables are used to store data values
# Variables are created when you assign a value to it


# Variables do not need to be declared with any particular type and can even change type after they have been set.
# Variables can be assigned with a single value or multiple values

# Strings
# Strings are used to store text data
# Strings can be created using single or double quotes

name = "Salim Abukar Ahmed"  # string

# age = 25  # integer or whole number can be positive or negative
# height = 1.75  # float or decimal number can be positive or negative
# is_student = True  # boolean or true or false


# print("Hello my name is", name)  # this will print the value of name variable
# print("I am", age, "years old")  # this will print the value of age variable
# # this will print the value of height variable
# print("My height is", height, "meters")
# # this will print the value of is_student variable
# print("Am I a student?", is_student)


# String Methods
# String methods are used to perform operations on strings

print(name.upper())  # this will convert the string to uppercase
print(name.lower())  # this will convert the string to lowercase
print(name.title())  # this will convert the string to title case
print(name.split())  # this will split the string into a list of words
# this will replace the string "Salim" with "Ahmed"
print(name.replace("Salim", "Ahmed"))
# this will find the index of the string "Salim" in the name variable
print(name.find("Salim"))
# this will count the number of times "a" appears in the name variable
print(name.count("a"))
print(name.startswith("S"))  # this will check if the string starts with "S"
print(name.endswith("d"))  # this will check if the string ends with "d"

# String Concatenation
# String concatenation is used to join two or more strings together

# Example
first_name = "Salim"
last_name = "Ahmed"
full_name = first_name + " " + last_name
print(full_name)  # this will print the full name

# Type Conversion
# Type conversion is used to convert one data type to another
# Example
age = 25
height = 1.75

# this will convert the age variable to a string
age_str = str(age)
# this will convert the height variable to an integer
height_int = int(height)
# this will convert the age variable to a float
age_float = float(age)

print(type(age_str))  # this will print the age variable as a string
print(type(height_int))  # this will print the height variable as an integer


# f string 
# f string is used to format the string
# Example

print(f"My name is {name} and I am {age} years old")  # this will print the name and age variable
# this will print the name and age variable