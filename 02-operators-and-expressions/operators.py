# ============================================================================
# Topic: Operators
# Description: Arithmetic, assignment, comparison, logical, and exponentiation
#              operators with practical examples
# ============================================================================

# SECTION 1: Arithmetic Operators
# ============================================================================
# Arithmetic operators: +, -, *, /, //, %
# Used for mathematical calculations on numeric values

# Example 1.1: Calculate total shopping cost
# Problem: Calculate total cost of 3 shirts, 2 jeans, plus shipping
shirt_price = 250  # Price of one shirt in rupees
jeans_price = 1000  # Price of one pair of jeans in rupees
shipping_cost = 150  # Shipping fee in rupees

total = shirt_price * 3 + jeans_price * 2 + shipping_cost
print("Total cost ₹:", total)


# Example 1.2: Convert seconds to hours, minutes, and seconds
# Problem: Break down 3672 seconds into hours, minutes, and remaining seconds
# Floor division (//) divides and discards decimal part
# Modulo (%) returns remainder after division
total_seconds = 3672

hours = total_seconds // 3600  # 3600 seconds in one hour
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60  # 60 seconds in one minute
seconds = remaining_seconds % 60

print(hours, "hour,", minutes, "minute,", seconds, "seconds")


# SECTION 2: Assignment Operators
# ============================================================================
# Assignment operators: =, +=, -=, *=, /=
# Assign values and perform operations simultaneously

# Example 2.1: Update score progressively
# Problem: Track score changes with different operations
score = 0  # Initialize score to zero

score += 10  # Equivalent to: score = score + 10
print("After adding 10:", score)

score *= 2  # Equivalent to: score = score * 2
print("After multiplying by 2:", score)

score -= 5  # Equivalent to: score = score - 5
print("Final Score:", score)


# SECTION 3: Exponentiation Operator
# ============================================================================
# Exponentiation: **
# Raises a number to a power (repeated multiplication)

# Example 3.1: Calculate powers of a number
# Problem: Find square, cube, and 4th power of 4
number = 4

square = number ** 2  # 4 to the power of 2
cube = number ** 3  # 4 to the power of 3
power4 = number ** 4  # 4 to the power of 4

print("Square (4²):", square)
print("Cube (4³):", cube)
print("Power 4 (4⁴):", power4)


# SECTION 4: Comparison Operators
# ============================================================================
# Comparison: >, <, >=, <=, ==, !=
# Compare values and return True or False (boolean)

# Example 4.1: Check if scores meet passing criteria
# Problem: Verify if math and science scores are passing (≥ 35)
math_score = 85
science_score = 78
passing_score = 35

is_math_pass = math_score >= passing_score
is_science_pass = science_score >= passing_score

print("Math passed:", is_math_pass)
print("Science passed:", is_science_pass)


# SECTION 5: Logical Operators
# ============================================================================
# Logical: and, or, not
# Combine conditions and return True or False

# Example 5.1: Check entry permission using AND and OR
# Problem: Determine concert entry based on age, ticket, and VIP status
# Rules: (Age ≥ 18 AND has ticket) OR is VIP member
age = 19
has_ticket = True
is_vip = False

entry_allowed = (age >= 18 and has_ticket) or is_vip
print("Entry Allowed:", entry_allowed)


# Example 5.2: Check access using NOT operator
# Problem: Verify access when user is NOT verified
is_verified = False

access_granted = not is_verified
print("Access Granted:", access_granted)


# SECTION 6: Equality Operators
# ============================================================================
# Equality: ==, !=
# == checks if values are equal
# != checks if values are not equal

# Example 6.1: Compare numeric equality
# Problem: Check if two values are equal or different
a = 10
b = 10
c = 5

are_equal = a == b
are_not_equal = a != c

print("10 == 10:", are_equal)
print("10 != 5:", are_not_equal)


# SECTION 7: Operator Precedence
# ============================================================================
# Operator Precedence: Order of evaluation (highest to lowest)
# 1. ** (exponentiation)
# 2. *, /, //, % (multiplication, division, modulo)
# 3. +, - (addition, subtraction)
# 4. ==, !=, <, >, <=, >= (comparison)
# 5. not (logical NOT)
# 6. and (logical AND)
# 7. or (logical OR)

# Example 7.1: Demonstrate precedence in calculations
# Without understanding precedence, calculations can produce wrong results
result1 = 2 + 3 * 4
print("2 + 3 * 4 =", result1)
# Multiplication first: 3 * 4 = 12, then 2 + 12 = 14

result2 = (2 + 3) * 4
print("(2 + 3) * 4 =", result2)
# Parentheses override precedence: 2 + 3 = 5, then 5 * 4 = 20

result3 = 2 ** 3 * 4
print("2 ** 3 * 4 =", result3)
# Exponentiation first: 2 ** 3 = 8, then 8 * 4 = 32


# ============================================================================
# Operators Summary:
# - Arithmetic: +, -, *, /, //, %
# - Assignment: =, +=, -=, *=, /=
# - Comparison: ==, !=, >, <, >=, <=
# - Logical: and, or, not
# - Exponentiation: **
# - Use parentheses to override default precedence
# ============================================================================