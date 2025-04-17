# we will learn python Conditionals
# Python Conditionals are used to perform different actions based on different conditions
# Python supports the following conditional statements:if, elif, else, switch (in Python 3.10 and later)

# if statement
# The if statement is used to test a condition. If the condition is true, the code block inside the if statement will be executed.

# Example of Temperature

# print('Welcome to the Temperature ')

# temp = 30;

# if temp >= 30:
#     print('It is hot')
# elif temp < 10:
#     print('It is cold')
# elif temp == 20:
#     print('It is warm')
# else:
#     print('It is moderate')


# Example of Age and driver licence  using logical operators

# print('Welcome to the Driver License Eligibility Checker')
# age = int(input('Enter your age '))
# # This will prompt the user to enter their age

# has_license = input('Do you have a driver license (yes/no) ').lower()
# # This will prompt the user to enter whether they have a driver license

# if age >= 18 and has_license == 'yes':
#     print('You are eligible to get a driver license')
# elif age >= 18 and has_license == 'no':
#     print('You are eligible to apply for a driver license')
# elif age < 18 and has_license == 'yes':
#     print('You are not eligible to get a driver license')
# else:
#     print('You are not eligible to get a driver license')


# Nested if elif
# Example Score marks

# print('Welcome to the Score Checker')
# score = int(input('Enter your score '))

# # This will prompt the user to enter their score
# if score >= 90:
#     print('You got an A')
# elif score >= 80:
#     print('You got a B')
# elif score >= 70:
#     print('You got a C')
# elif score >= 60:
#     print('You got a D')
# elif score >= 50:
#     print('You got an E')
# else:
#     print('You got an F')


# using "in" operator with if condtion

# Example of checking if a number is in a list
# numbers = [1, 2, 3, 4, 5]
# number = int(input('Enter a number '))
# if number in numbers:
#     print(f'{number} is in the list')
# else:
#     print(f'{number} is not in the list')


# Example of checking if a character is in a string
# string = 'Hello World'
# character = input('Enter a character ')
# if character in string:
#     print(f'{character} is in the string')
# else:
#     print(f'{character} is not in the string')



# Ternary Operator 
# 
# # The ternary operator is a shorthand way of writing an if-else statement. It is used to assign a value to a variable based on a condition.
# Example of Ternary Operator

print('Welcome to the Ternary Operator Example')
num = int(input('Enter a number '))
# This will prompt the user to enter a number
result = 'Even' if num % 2 == 0 else 'Odd'
# This will assign 'Even' to result if num is even, otherwise it will assign 'Odd'
print(f'The number {num} is {result}')
# This will print the result
# This is a simple example of using the ternary operator to check if a number is even or odd

#Example 2

age = 17

marired =  "Married" if age >= 18 else "Single"
print(f'You are {marired}')