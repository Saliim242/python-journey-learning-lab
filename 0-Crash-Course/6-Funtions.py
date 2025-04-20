# Funtions in python
# Function is a block of code which only runs when it is called
# Function is a block of code that is reusable and takes parameters and returns a value

# syntax of function is:

# def function_name(parameters):
#     # code to be executed

#     return value
# function_name() # calling the function


# An Example of function

# def greet(name):
#     print("Hello " + name + ", welcome to the world of Python")


# # calling the function
# greet("Salim Abukar Ahmed")


# def greet_user(firstname, lastname, age):
#     print(f"Hello {firstname} {lastname} , Welcome Back we are missed you!")
#     print(f"Your age is {age} years old")


# name = input("Enter your name: ")
# last = input("Enter your last name: ")
# age = int(input("Enter your age: "))
# greet_user(name, last, age)


# Function with default parameters
# def greet_user(firstname, lastname, age=18):
#     print(f"Hello {firstname} {lastname} , Welcome Back we are missed you!")
#     print(f"Your age is {age} years old")


# Example of function with parameters and rerurn value

# def add_numbers(num1, num2):
#     return num1 + num2

# # calling the function


# result = add_numbers(5, 10)
# print(f"The sum of 5 and 10 is {result}")


# # Function with multiple return values
# def add_subtract(num1, num2):
#     sum = num1 + num2
#     subtract = num1 - num2
#     return sum, subtract


# # calling the function
# result, add = add_subtract(10, 5)
# print(f"The sum of 10 and 5 is {result} and the subtract is {add}")
# Function with arbitrary arguments
# what is arbitrary arguments
# Arbitrary arguments are used when we don't know how many arguments will be passed to the function
def greet_users(*names):
    for name in names:
        print(f"Hello {name}, welcome to the world of Python!")


# calling the function
greet_users("Salim", "Abukar", "Ahmed", "Ali", "Mohammed")


# Function with keyword arguments
# # keyword arguments are used when we want to pass arguments with their names
# def greet_user(firstname, lastname, age):
#     print(f"Hello {firstname} {lastname} , Welcome Back we are missed you!")
#     print(f"Your age is {age} years old")
