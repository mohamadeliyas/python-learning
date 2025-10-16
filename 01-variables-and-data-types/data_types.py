# ============================================================================
# Topic: Data Types
# Description: Understanding Python's fundamental data types - string, integer,
#              float, boolean, and type conversion between them
# ============================================================================

# SECTION 1: String Data Type
# ============================================================================

# String is a sequence of characters enclosed in quotes
name = "Mohamed Eliyas"
print(name)

city = "Coimbatore"
print(city)

# String examples
greeting = "Hello, Python!"
print(greeting)


# SECTION 2: Integer Data Type
# ============================================================================

# Integer is a whole number without decimals
age = 25
print("You are", age, "years old")

year = 2025
print("Current year:", year)

count = 100
print("Count:", count)


# SECTION 3: Float Data Type
# ============================================================================

# Float is a number with decimal points
value = 3.5
print("Value:", value)

height = 5.9
print("Height:", height, "feet")

gpa = 3.75
print("GPA:", gpa)


# SECTION 4: Boolean Data Type
# ============================================================================

# Boolean is True or False value
is_student = True
print("Is student:", is_student)

is_employed = False
print("Is employed:", is_employed)

# Non-empty strings convert to True
word = "eliyas"
result = bool(word)
print("bool('eliyas'):", result)

# Empty strings convert to False
empty_word = ""
result = bool(empty_word)
print("bool(''):", result)


# SECTION 5: Type Conversion - String to Integer
# ============================================================================

# Convert string to integer using int()
num_string = "100"
num_integer = int(num_string)
print("String '100' converted to integer:", num_integer)

# Perform arithmetic on converted value
num_string = "100"
convert = int(num_string) + 25
print("100 + 25 =", convert)

# Another example
age_string = "23"
age_integer = int(age_string)
future_age = age_integer + 10
print("In 10 years, age will be:", future_age)


# SECTION 6: Type Conversion - String to Float
# ============================================================================

# Convert string to float using float()
price_string = "19.99"
price_float = float(price_string)
print("String '19.99' converted to float:", price_float)

# Perform arithmetic on converted value
value_string = "5.5"
converted_value = float(value_string) + 2.5
print("5.5 + 2.5 =", converted_value)


# SECTION 7: Type Conversion - Integer to String
# ============================================================================

# Convert integer to string using str()
age = 25
age_string = str(age)
print("Integer 25 converted to string:", age_string)

# Combine with other strings
number = 42
result = "The answer is " + str(number)
print(result)


# SECTION 8: Checking Data Types with type()
# ============================================================================

# Use type() function to check data type of a variable
value = 3.5
print("Type of 3.5:", type(value))

text = "hello"
print("Type of 'hello':", type(text))

number = 42
print("Type of 42:", type(number))

boolean = True
print("Type of True:", type(boolean))


# SECTION 9: Type Conversion - String to Boolean
# ============================================================================

# Non-empty strings convert to True
word = "hello"
convert_word = bool(word)
print("bool('hello'):", convert_word)
print("Type:", type(convert_word))

# Numeric strings convert to True when converted
num_string = "123"
convert_num = bool(num_string)
print("bool('123'):", convert_num)

# Zero and empty values convert to False
zero_string = "0"
convert_zero = bool(zero_string)
print("bool('0'):", convert_zero)


# SECTION 10: Type Conversion Errors
# ============================================================================

# Converting non-numeric string to integer causes ValueError
# Uncomment below to see the error:
'''
word = "hello"
convert_word = int(word)  # This will raise ValueError
print(convert_word)
'''

# To avoid errors, only convert valid numeric strings
valid_number = "100"
result = int(valid_number)
print("Valid conversion:", result)

# ============================================================================
# Key Takeaways:
# - String: Text data in quotes ("hello")
# - Integer: Whole numbers (25, 100, -5)
# - Float: Decimal numbers (3.5, 19.99, -2.5)
# - Boolean: True or False values
# - Convert types: int(), float(), str(), bool()
# - Check types: type(variable)
# - Only convert valid values to avoid errors
# ============================================================================