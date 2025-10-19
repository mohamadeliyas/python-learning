# ============================================================================
# Topic: Control Flow
# Description: If/Elif/Else statements, conditional logic, and decision making
# ============================================================================


# SECTION 1: Age Classification
# ============================================================================
# Classify a person as Child, Teen, or Adult based on their age input

age = int(input("Enter your age: "))

if age <= 12:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teen")
else:
    print("Adult")


# SECTION 2: Grade Assignment System
# ============================================================================
# Assign grade (A/B/C/F) based on student's mark out of 100

mark = int(input("Enter your mark out of 100: "))

if mark >= 90:
    print("Grade A")
elif mark >= 75:
    print("Grade B")
elif mark >= 50:
    print("Grade C")
else:
    print("Fail")


# SECTION 3: Even or Odd Number Check
# ============================================================================
# Check whether a given number is odd or even

user = int(input("Enter a number: "))

if user % 2 == 0:
    print("Even")
else:
    print("Odd")


# SECTION 4: Password Verification
# ============================================================================
# Check if password matches "admin123", grant or deny access

user = input("Enter a password: ")
password = "admin123"

if user == password:
    print("Grant Access")
else:
    print("Access Denied")


# SECTION 5: Menu Selection System
# ============================================================================
# Ask for letter A/B/C and print custom message for each

customer = input("Enter a letter: ").upper()
A = "You chose Option A: Account Info"
B = "You chose Option B: Billing"
C = "You chose Option C: Contact Support"

if customer == "A":
    print(A)
elif customer == "B":
    print(B)
elif customer == "C":
    print(C)
else:
    print("Invalid Option")


# SECTION 6: Animal Sound Classifier
# ============================================================================
# Get animal name and print corresponding sound

user = input("Enter an animal: ").title()

if user == "Cat":
    print("Meow")
elif user == "Dog":
    print("Bark")
elif user == "Cow":
    print("Moo")
else:
    print("I don't know this animal")


# SECTION 7: FizzBuzz Pattern
# ============================================================================
# Print FizzBuzz based on divisibility by 3 and 5

user = int(input("Enter a Number: "))

if user % 3 == 0 and user % 5 == 0:
    print("FizzBuzz")
elif user % 3 == 0:
    print("Fizz")
elif user % 5 == 0:
    print("Buzz")
else:
    print(user)


# SECTION 8: Weather Classifier
# ============================================================================
# Classify temperature in Celsius into categories

temp = int(input("Enter temperature in Celsius: "))

if temp < 10:
    print("Very Cold")
elif temp >= 10 and temp <= 25:
    print("Normal")
elif temp >= 26 and temp <= 35:
    print("Warm")
else:
    print("Too Hot")


# SECTION 9: Movie Ticket Logic
# ============================================================================
# Determine entry eligibility based on age, ticket, and adult presence

age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ").lower()
with_adult = input("Are you with an adult? (yes/no): ").lower()

if age >= 18:
    print("Entry Allowed: You are 18 or older")
elif age < 18 and has_ticket == "yes" and with_adult == "yes":
    print("Entry Allowed: You're under 18 but have ticket and are with an adult")
else:
    print("Entry Denied")


# SECTION 10: Login System (Strong Condition)
# ============================================================================
# Grant access only if username, password, and length conditions are met

user_name = input("Enter a username: ")
password = input("Enter a password: ")

if user_name == "admin" and password == "admin123" and len(password) >= 8:
    print("Grant access")
else:
    print("Access Denied")


# SECTION 11: Discount System
# ============================================================================
# Calculate discount based on bill amount and display final amount

total_bill = int(input("Enter total amount: "))

if total_bill >= 5000:
    discount = total_bill * 0.20
elif total_bill >= 3000:
    discount = total_bill * 0.10
elif total_bill >= 1000:
    discount = total_bill * 0.05
else:
    discount = 0

final = total_bill - discount

print(f"Original amount: {total_bill}")
print(f"Discount Applied: {discount}")
print(f"Final amount to pay: {final}")


# ============================================================================
# Control Flow Summary:
# - if statement executes if condition is True
# - elif checks alternative conditions
# - else executes if all conditions are False
# - Comparison operators: ==, !=, >, <, >=, <=
# - Logical operators: and, or
# - Modulo operator (%) for divisibility checks
# - Multiple conditions with and/or operators
# - Nested logic and range checks
# ============================================================================