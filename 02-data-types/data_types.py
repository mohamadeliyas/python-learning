num = "100"
convert = int(num) +25
print(convert)

age = 25
print("You are", age, "years old")

value = 3.5
print("Type of value is:", type(value))
 
'''word = "hello"                #In Python, you cannot convert a non-numeric string (like "hello") 
convert_word = int(word)      #into an integer using the int() function—this will raise a ValueError.
print(convert_word)'''

word = "eliyas"
print(bool(word))

word = "hello"
convert_word = bool(word)
print(type(convert_word))

name = "ada lovelace"
print(name.title())

import sys
user_name = sys.argv[1]
age = int(input("Enter Your Current Age:"))
def future_age(age):
    return age + 10
result = future_age(age)
print('Hello', user_name, 'in 10 years you will be', result, 'year old')
