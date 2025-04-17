# In this Section We will learn about Input and Output in Python
# Input to take the user to Enter data
# Output to display the data on the screen

# Example
# name = input('What is your name ')
# # This will prompt the user to enter their name
# # The input function will wait for the user to enter their name and press Enter
# # The entered name will be stored in the variable name

# print('Hello ' + name)
# # This will print Hello followed by the name entered by the user

# # Age Calculator
# # Example
# age = int(input('Enter your age '))
# # This will prompt the user to enter their age
# years_to_100 = 100 - age
# # The entered age will be converted to an integer and subtracted from 100
# print(f'You will be 100 years old in {years_to_100}  years')
# This will print the number of years left to reach 100


# Lets make a simple calculator
# Example

# print('Welcome to the Simple Calculator')
# print('Please enter two numbers')
# num1 = float(input('Enter the first number '))
# num2 = float(input('Enter the second number '))
# print('Please select an operation')
# print('1. Addition')
# print('2. Subtraction')
# print('3. Multiplication')
# print('4. Division')
# operation = input('Enter the operation (1/2/3/4) ')
# if operation == '1':
#     result = num1 + num2
#     print(f'The result of {num1} + {num2} is {result}')
# elif operation == '2':
#     result = num1 - num2
#     print(f'The result of {num1} - {num2} is {result}')
# elif operation == '3':
#     result = num1 * num2
#     print(f'The result of {num1} * {num2} is {result}')
# elif operation == '4':
#     result = num1 / num2
#     print(f'The result of {num1} / {num2} is {result}')
# else:
#     print('Invalid operation selected')

# This is a simple calculator that takes two numbers and an operation as input
# and prints the result of the operation


# Example meter to centimeter
# Example
# print('Welcome to the Meter to Centimeter Converter')
meters = float(input('Enter the length in meters '))
centimeters = meters * 100
print(f'The length in centimeters is {centimeters}')

# This will convert the length in meters to centimeters


# Example Celsius to Fahrenheit
# Example
# print('Welcome to the Celsius to Fahrenheit Converter')
celsius = float(input('Enter the temperature in Celsius '))
fahrenheit = (celsius * 9/5) + 32  # Explain
print(f'The temperature in Fahrenheit is {fahrenheit}')
# This will convert the temperature in Celsius to Fahrenheit


# End of the section
# # In this section we learned about input and output in Python
# We learned how to use the input() function to get user input and the print() function to
# display output
# We also learned how to convert data types using int() and float() functions
# We also learned how to use f-strings to format strings
