# ============================================================================
# Topic: Variables
# Description: Variable assignment, printing, updating, and naming conventions
# ============================================================================

# SECTION 1: Basic Variable Assignment and Printing
# ============================================================================

# Simple variable assignment
message = "Hello Python Crash Course world!"
print(message)

# Multiple variable assignments
status = "Beginner"
print(status)

language = "Learning Python"
print(language)

# Numeric variable
age = 23
print("You are", age, "years old")


# SECTION 2: Multiple Variables Together
# ============================================================================

# Using multiple variables in print statements
your_name = "Mohamed Eliyas"
your_age = 23
print("My name is", your_name, "and my age is", your_age)

# Using f-strings for string formatting
city = "Coimbatore"
print(f"Hello {your_name}, you are {your_age} years old")
print(f"I live in {city}")


# SECTION 3: Variable Updates
# ============================================================================

# Update string variable
message = "This is the original message."
print(message)

message = "This is the updated message."
print(message)

# Update numeric variable
counter = 1
print("Counter:", counter)

counter = 5
print("Counter:", counter)

counter = counter + 1
print("Counter:", counter)

# Update multiple variables
name = "Alice"
print("Name:", name)

name = "Bob"
print("Name:", name)


# SECTION 4: Variable Naming Conventions
# ============================================================================

# Snake_case naming (lowercase with underscores)
user_name = "Elon"
total_score = 95
first_message = "Welcome"
student_age = 20

print(f"User: {user_name}")
print(f"Score: {total_score}")
print(f"Message: {first_message}")
print(f"Age: {student_age}")


# SECTION 5: Multiple Variables in Memory
# ============================================================================

# Multiple independent variables
name = "Sarah"
email = "sarah@email.com"
phone = "555-1234"

print(name)
print(email)
print(phone)

# Different variable names, same value
favorite_color = "blue"
favorite_animal = "blue"

print(favorite_color)
print(favorite_animal)

# ============================================================================
# Key Takeaways:
# - Variables store data with a name label
# - Create: variable_name = value
# - Update: assign a new value to the same variable name
# - Use snake_case for professional naming
# - Multiple variables can exist simultaneously
# ============================================================================