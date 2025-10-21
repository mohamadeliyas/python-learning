# ============================================================================
# Topic: Functions - Advanced
# Description: Advanced function concepts, *args, **kwargs, real-world problems
# ============================================================================


# SECTION 1: Q1 - Basic Function with Return
# ============================================================================

def give_water():
    return "Bottle of Water"

output = give_water()
print(f"Give Water: {output}")


# SECTION 2: Q2 - Function Returning Numeric Value
# ============================================================================

def get_age():
    return 25

print(f"Age: {get_age()}")


# SECTION 3: Q3 - Function with Parameter and String Concatenation
# ============================================================================

def make_pizza(toppings):
    return toppings + " Pizza"

output = make_pizza("Cheese")
print(f"Pizza: {output}")


# SECTION 4: Q4 - Function Returning Multiple Values
# ============================================================================

def add(a, b):
    return a + b, a - b  # Return two values as tuple

adding, subtract = add(5, 3)
print(f"Addition: {adding}")
print(f"Subtraction: {subtract}")


# SECTION 5: Q5 - Function with Print and Return
# ============================================================================

def test():
    print("Inside function")
    return "Result"

output = test()
print(f"Returned from test(): {output}")


# SECTION 6: Q6 - Function with Calculation
# ============================================================================

def calculate_discount(price):
    return price * 0.1

discount = calculate_discount(200)
final_price = 200 - discount
print(f"Discount: {discount}")
print(f"Final Price: {final_price}")


# SECTION 7: Q7 - Simple Return Value - Number
# ============================================================================
# Write a function that returns the number 100

def number():
    return 100

output = number()
print(output)


# SECTION 8: Q8 - Simple Return Value - Message
# ============================================================================
# Write a function that returns the message "Learning Python is fun"

def message():
    return "Learning Python is fun"

output = message()
print(output)


# SECTION 9: Q9 - Function with Input
# ============================================================================
# Write a function get_name() that takes your name as input and returns it

def get_name():
    name = input("Enter a name: ")
    return name

output = get_name()
print(f"My name is {output}")


# SECTION 10: Q10 - Function with Two Parameters - Addition
# ============================================================================
# Create a function add_numbers(a, b) that returns their sum

def add_numbers(a, b):
    return a + b

sum = add_numbers(5, 6)
print(sum)


# SECTION 11: Q11 - Function with Two Parameters - Multiplication
# ============================================================================
# Write a function multiply(x, y) that returns the product of two numbers

def multiply(x, y):
    return x * y

product = multiply(5, 6)
print(product)


# SECTION 12: Q12 - Function with String Parameter
# ============================================================================
# Write a function greet(name) that returns "Hello, <name>"

def greet(name):
    return f"Hello {name}"

output = greet("Eliyas")
print(output)


# SECTION 13: Q13 - Function with Discount Calculation
# ============================================================================
# Write a function get_discount(price) that returns 10% of the price

def get_discount(price):
    return price * 0.10

original_price = 100
discount = get_discount(original_price)
final_price = original_price - discount
print(f"Final amount after 10% discount: {final_price}")


# SECTION 14: Q14 - Function with Area Calculation
# ============================================================================
# Write a function get_area(length, width) that returns the area of a rectangle

def get_area(length, width):
    return length * width

total = get_area(5, 3)
print(f"Area is: {total}")


# SECTION 15: Q15 - Function with Unit Conversion
# ============================================================================
# Write a function convert_to_seconds(minutes) that returns total seconds

def convert_to_seconds(minutes):
    return minutes * 60

total = convert_to_seconds(3)
print(total)


# SECTION 16: Q16 - Function with Boolean Return - Even Check
# ============================================================================
# Write a function is_even(n) that returns True if even, else False

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

output = is_even(7)
print(output)


# SECTION 17: Q17 - Function with Conditional Logic - Pass/Fail
# ============================================================================
# Write a function grade(score) that returns Pass or Fail based on score >= 50

def grade(score):
    if score >= 50:
        return "Pass"
    else:
        return "Fail"

output = grade(4)
print(output)


# SECTION 18: Q18 - Function with Multiple Conditions - Comparison
# ============================================================================
# Write a function compare(a, b) that returns comparison result

def compare(a, b):
    if a > b:
        return "a is greater"
    elif b > a:
        return "b is greater"
    else:
        return "Equal"

output = compare(3, 3)
print(output)


# SECTION 19: Q19 - Function Returning Multiple Values - Calculations
# ============================================================================
# Write a function calculate(a, b) that returns sum, difference, and product

def calculate(a, b):
    return a + b, a - b, a * b  # Return three values as tuple

x, y, z = calculate(5, 7)
print(f"Sum: {x}")
print(f"Difference: {y}")
print(f"Product: {z}")


# SECTION 20: Q20 - Function with Tax Calculation
# ============================================================================
# Function that accepts price and tax_rate, calculates total bill with tax

def calc_with_tax(price, tax):
    tax_amount = price * tax
    final_amount = price + tax_amount  # Add tax to price
    return final_amount

total = calc_with_tax(200, 0.10)
print(total)


# SECTION 21: Q21 - Function with *args - Variable Arguments
# ============================================================================
# Function that accepts any number of arguments and returns their sum

def add_all(*argn):
    total = 0
    for num in argn:
        total += num
    return total

print(add_all(1, 6, 9))


# SECTION 22: Q22 - Function with *args - Filter Squares Greater Than 30
# ============================================================================
# Write a function that takes any number of values and filters squares > 30

def square_filter(*n):
    for num in n:
        square = num * num
        if square >= 30:  # Check if square is greater than 30
            print(f"{square} is greater than 30")

square_filter(4, 5, 6)


# SECTION 23: Q23 - Function with *args - Filter Even Numbers
# ============================================================================
# Return only even numbers from a list of any numbers

def even_filter(*n):
    for num in n:
        if num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is not even")

even_filter(44, 55, 66)


# SECTION 24: Q24 - Function with User Input - Temperature Converter
# ============================================================================
# Problem: Temperature Converter - Convert Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * (9/5) + 32  # Apply conversion formula
    return fahrenheit

user = float(input("Enter a Celsius: "))
print(f"{user}°C is equal to {celsius_to_fahrenheit(user):.2f}°F")


# SECTION 25: Q25 - Function with Conditional Logic - Voter Eligibility
# ============================================================================
# Problem: Voter Eligibility Check - Takes name and age, checks if eligible

def voter_check(name, age):
    if age >= 18:
        print(f"{name} is eligible to vote")
    else:
        print(f"{name} is not eligible to vote")

name = input("Enter a name: ")
age = int(input("Enter a age: "))
voter_check(name, age)


# SECTION 26: Q26 - Function with Multiple Parameters - Bill Calculator
# ============================================================================
# Problem: Bill Calculator with Tax - Accepts price and quantity, returns total

def bill_with_tax(price, quantity):
    total_price = price * quantity
    tax = total_price * 0.10
    final_amount = total_price + tax  # Add 10% tax
    return final_amount

price = int(input("Enter a total price: "))
quantity = int(input("Enter a total quantity: "))
bill = bill_with_tax(price, quantity)
print(f"Total amount with 10% tax: ₹{bill}")


# SECTION 27: Q27 - Function with String Comparison - Login System
# ============================================================================
# Problem: Login System - Checks username and grants/denies access

def check_login(username):
    if username == "admin" or username == "guest":
        print("Access Granted")
    else:
        print("Access Denied")
    return(username)

user = input("Enter a user name: ").lower()
check_login(user)


# SECTION 28: Q28 - Function with *args - Summation Tool
# ============================================================================
# Problem: Summation Tool - Accepts any number of numbers and returns sum

def total_sum(*numbs):
    total = sum(numbs)  # Use built-in sum() function
    print(total)

total_sum(18, 7, 10, 44)


# SECTION 29: Q29 - Function with **kwargs - Profile Display
# ============================================================================
# Problem: Profile Display - Accepts person's details using key-value pairs

def profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

profile(Name="Eliyas", Age=23)


# SECTION 30: Q30 - Function with List Parameter - Word Counter
# ============================================================================
# Problem: Word Counter - Accepts a sentence and returns word count

def count_words(sentence):
    total = len(sentence)
    print(total)
    return total

user = input("Enter a sentence: ").split()
count_words(user)


# SECTION 31: Q31 - Function with Multiple Parameters - Receipt Generator
# ============================================================================
# Problem: Mini Receipt Generator - Prints receipt with name and total bill

def print_receipt(name, item1_price, item2_price):
    final_amount = item1_price + item2_price
    print(f"Receipt for: {name}")
    print(f"Total: ₹{final_amount}")

name = input("Enter your name: ").capitalize()
item1_price = int(input("Item 1 amount: "))
item2_price = int(input("Item 2 amount: "))
print_receipt(name, item1_price, item2_price)


# SECTION 32: Q32 - Function with Conditional Logic - Smart Score Evaluator
# ============================================================================
# Problem: Smart Score Evaluator - Accepts 3 marks, calculates average, returns grade

def grade_calculator(sub1, sub2, sub3):
    average = (sub1 + sub2 + sub3) / 3
    if average >= 90:
        print("Grade A")
    elif average >= 75:
        print("Grade B")
    elif average >= 50:
        print("Grade C")
    else:
        print("Fail")
    print(f"Average: {round(average, 2)}")

sub1 = int(input("Enter a subject 1 mark: "))
sub2 = int(input("Enter a subject 2 mark: "))
sub3 = int(input("Enter a subject 3 mark: "))
grade_calculator(sub1, sub2, sub3)


# SECTION 33: Q33 - Function Definition - Square Calculator
# ============================================================================
# Problem: Square Calculator - Helper function for calculations

def square(n):
    return n * n

print(square(5))
print(square(9))


# ============================================================================
# Advanced Functions Summary:
# - Multiple return values as tuples
# - *args for variable number of arguments
# - **kwargs for key-value pairs
# - Real-world problem solving
# - User input with functions
# - Arithmetic and conditional operations
# - Boolean returns and filters
# - Multiple calculations in one function
# - Professional function naming
# - F-string formatting in functions
# ============================================================================