# ============================================================================
# Topic: Functions
# Description: Function definition, calling, parameters, return values, and sys.argv
# ============================================================================

import sys


# SECTION 1: Q1 - Basic Function Definition and Calling
# ============================================================================
# Create a simple function with no parameters and call it multiple times

def say_hello():
    print("Hello, Python")

say_hello()
say_hello()


# SECTION 2: Q2 - Function with Parameter and Return Value
# ============================================================================
# Create a function that accepts a parameter and returns a value

def greet_user(name):
    return f"Welcome {name}"

output = greet_user("Eliyas")
print(output)


# SECTION 3: Q3 - Function with Multiple Calls
# ============================================================================
# Create a function and call it multiple times

def show_message():
    print("This is a Message")

show_message()
show_message()
show_message()


# SECTION 4: Q4 - Function with Parameters and Arithmetic
# ============================================================================
# Create a function that accepts two parameters and returns arithmetic result

def add_number(a, b):
    return a + b  # Add two numbers and return sum

result = add_number(5, 7)
print(f"Sum: {result}")


# SECTION 5: Q5 - Return Statement Behavior
# ============================================================================
# Show that code after return does not execute in a function

def greet_user():
    print("Hello")
    return "Goodbye"  # Stops here, line below never runs
    print("See you soon")

result = greet_user()
print(result)


# SECTION 6: Q6 - Return Stops Execution
# ============================================================================
# Demonstrate that return terminates function execution immediately

def double_message():
    print("Message 1")
    print("Message 2")
    return "Done"  # Function ends here
    print("This won't show")

result = double_message()
print(result)


# SECTION 7: Q7 - Function with Conditional Logic
# ============================================================================
# Create a function that checks if a number is big or small

def number_check(num):
    print("Checking number")
    if num > 10:
        return "Big"  # If condition true, return immediately
    return "Small number"

result = number_check(num=12)
print(result)


# SECTION 8: Q8 - Function with Age Verification
# ============================================================================
# Create a function that checks if age is 18 or more and returns Adult or Minor

def age_check(num):
    print("Checking age")
    if num >= 18:
        return "Adult"  # Check condition and return based on result
    return "Minor"

result = age_check(num=20)
print(result)


# SECTION 9: Q9 - Age Calculator with sys.argv and Function
# ============================================================================
# Problem: Take user's name from sys.argv and current age from input, calculate age in 10 years

user_name = sys.argv[1]  # Get from command-line
age = int(input("Enter Your Current Age: "))

def future_age(age):
    return age + 10

result = future_age(age)
print(f"Hello {user_name}, in 10 years you will be {result} years old")


# SECTION 10: Q10 - Shopping Bill Calculator with Function
# ============================================================================
# Problem: Ask for item price and quantity, calculate total with 5% tax

item_price = float(input("Price: "))
quantity = int(input("Total Quantity: "))

def calculate_total(price, quantity):
    total = price * quantity
    tax = total * 0.05  # Calculate 5% tax
    final_amount = total + tax  # Add tax to get final amount
    return final_amount

final_amount = calculate_total(item_price, quantity)
print(f"Total bill with tax is: {final_amount}")


# SECTION 11: Q11 - Greeting with sys.argv and Function
# ============================================================================
# Problem: Use sys.argv for city and input() for name and age to return greeting

city = sys.argv[1]  # Get from command-line
name = input("Enter your name: ")
age = int(input("Enter your age: "))

def greeting(name, age, city):
    return f"Welcome {name} from {city}. Next year you will be {age + 1} years old"

final = greeting(name, age, city)
print(final)


# SECTION 12: Q12 - sys.argv Command-Line Arguments
# ============================================================================
# Problem: Use command-line arguments to print age and greet user by name and city

age = int(sys.argv[1])  # First command-line argument
print(f"Your age is {age}")

city = sys.argv[2]  # Second command-line argument
name = input("Enter your user name: ")
print(f"Hello {name} from {city}")


# ============================================================================
# Functions Summary:
# - def keyword to define functions
# - Parameters allow functions to accept input
# - return statement sends value back to caller
# - return stops function execution immediately
# - Functions can have conditional logic
# - Call functions using function_name()
# - sys.argv for command-line arguments
# - Functions with multiple parameters
# - Functions with arithmetic operations
# - Combining input() with functions
# - f-strings in return statements
# - Functions returning different values based on conditions
# ============================================================================