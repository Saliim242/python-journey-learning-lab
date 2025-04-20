# This totorial is part of a crash course on Python programming.
# In this tutorial, we will learn about error handling in Python.
# Error handling is a way to respond to errors that occur during the execution of a program.
# It allows us to gracefully handle errors and continue the execution of the program.


# In Python, we use try and except blocks to handle errors.
# The try block contains the code that may raise an error.
# The except block contains the code that will be executed if an error occurs.
# We can also use the else block to execute code if no errors occur.

# We can also use the finally block to execute code that will run regardless of whether an error occurs or not.
# This is useful for cleaning up resources, such as closing files or releasing network connections.

# Let's look at an example of error handling in Python.

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers.")
        return None
    else:
        print("Result:", result)
        return result
    finally:
        print("Execution completed.")


# In this example, we define a function called divide_numbers that takes two arguments.
# We use a try block to attempt to divide the two numbers.
# If a ZeroDivisionError occurs, we catch it in the except block and print an error message.
# If a TypeError occurs, we catch it in the second except block and print a different error message.
# If no errors occur, we print the result and return it.
# The finally block is executed regardless of whether an error occurs or not.
# Let's test the function with different inputs.


# divide_numbers(10, 2)  # Valid input
# divide_numbers(10, 0)  # Division by zero
# divide_numbers(10, "a")  # Invalid input
# In this example, we see how error handling allows us to gracefully handle errors and continue the execution of the program.
# We can also raise our own exceptions using the raise statement.
# This is useful when we want to enforce certain conditions in our code.


def check_positive(number):
    if number < 0:
        raise ValueError("Error: Number must be positive.")
    else:
        print("Number is positive.")
        return number
# In this example, we define a function called check_positive that takes a number as an argument.
# If the number is negative, we raise a ValueError with a custom error message.


# If the number is positive, we print a message and return the number.
# Let's test the function with different inputs.
check_positive(10)  # Valid input
# check_positive(-5)  # Invalid input
# In this example, we see how we can raise our own exceptions to enforce certain conditions in our code.
# This allows us to create more robust and reliable programs.
# In summary, error handling is an important aspect of programming that allows us to gracefully handle errors and continue the execution of the program.
