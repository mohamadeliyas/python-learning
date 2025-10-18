# ============================================================================
# Topic: Strings
# Description: String methods, operations, indexing, and manipulation
# ============================================================================

import readline


# SECTION 1: String Case Conversion and Length
# ============================================================================

sentence = input("Write a sentence: ")
stripped = sentence.strip()
print(stripped.upper())
print(stripped.lower())
print(len(stripped))


# SECTION 2: Extract First and Last Word
# ============================================================================

user = input("Enter your sentence: ")
stripped = user.strip()
word = stripped.split()
print(word[0])
print(word[-1])
print(len(word))


# SECTION 3: Search Text and Find Position
# ============================================================================

user = input("Enter your words: ")
search = input("Search: ")
user_lower = user.lower()
search_lower = search.lower()

if search_lower in user_lower:
    position = user_lower.find(search_lower)
    print(position)
else:
    print("Not Found")


# SECTION 4: Find First and Last Occurrence of Keyword
# ============================================================================

user = input("Enter a sentence: ")
keyword = input("Enter a keyword: ")

user_lower = user.lower()
keyword_lower = keyword.lower()

if keyword_lower in user_lower:
    print("Keyword Found")
    first_position = user_lower.find(keyword_lower)
    last_position = user_lower.rfind(keyword_lower)
    print("First occurrence at index:", first_position)
    print("Last occurrence at index:", last_position)
else:
    print("Keyword not found")


# SECTION 5: Count Keyword Occurrences (Substring Match)
# ============================================================================

user = input("Enter your sentence: ")
password = input("Enter your code: ")

cleaned = user.strip()
words = cleaned.split()
total = len(words)

cleaned_lower = cleaned.lower()
password_lower = password.lower()

match_count = cleaned_lower.count(password_lower)

print("Total words:", total)
print("Keyword match count:", match_count)


# SECTION 6: Count Exact Word Occurrences (Loop Method)
# ============================================================================

user = input("Enter you sentence: ")
password = input("Create Password: ")
cleaned = user.strip()
words = cleaned.split()
total = len(words)

cleaned_lower = cleaned.lower()
password_lower = password.lower()

match_count = 0
for word in words:
    if word.lower() == password_lower:
        match_count += 1

print("Total words:", total)
print("Keyword match count:", match_count)


# SECTION 7: Count Total Words and Characters
# ============================================================================

user = input("Enter a sentence: ")
cleaned = user.strip()
words = cleaned.split()
total_character = len(cleaned)
total_words = len(words)

print("Total characters:", total_character)
print("Total words:", total_words)


# SECTION 8: Get First and Last Word with Count
# ============================================================================

user = input("Enter a sentence: ")
cleaned = user.strip()
word = cleaned.split()
total_words = len(word)

print("First word:", word[0])
print("Last word:", word[-1])
print("Total words:", total_words)


# SECTION 9: Password Masking with Asterisk
# ============================================================================
# Ask user to enter a password, number of visible letters (from end), and mask with asterisk.
# Show masked password: masked part + visible part.

Password = input("Enter your code: ")
visibility = int(input("how many letters (from the end) should remain visible: "))
mask = '*' * (len(Password) - visibility)
masked_word = mask + Password[-visibility:]
print(masked_word)


# SECTION 10: Password Masking with Custom Symbol (Variant 1)
# ============================================================================
# Create a custom password masker. Show only last n characters and hide the rest using a given symbol.

customer_password = input("Enter your password: ")
characters_shown = int(input("How many character to shown in password: "))
masking_symbol = input("Ex: @, #, *: ")
masked = masking_symbol * (len(customer_password) - characters_shown)
visible = customer_password[-characters_shown:]
full = masked + visible
print("Password:", full)


# SECTION 11: Password Masking with Custom Symbol (Variant 2)
# ============================================================================
# Ask user to enter a password, number of visible characters (from end), and masking symbol.
# Show masked password: masked part + visible part.

user = input("Enter your password: ")
visibility = int(input("Enter how many digits to shown: "))
symbols = input("Enter a symbol (Eg;# ,@, *): ")
masking = symbols * (len(user) - visibility)
masked_password = user[-visibility:]
Total = masking + masked_password
print(Total)


# SECTION 12: Password Masking with Custom Symbol (Variant 3)
# ============================================================================

user = input("Enter your word: ")
symbols = input("Enter a symbol (e.g. #, *, @): ")
ask = int(input("How many characters (from the end) should be left visible: "))
mask = symbols * (len(user) - ask)
visible = user[-ask:]
masked_word = mask + visible
print(masked_word)


# SECTION 13: String Formatting with F-strings
# ============================================================================

song = "levitating"
artist = "dua lipa"
print(f"{song.title()} by {artist.title()}")

name = "ada lovelace"
print(name.title())

famous_person = "Elon Musk"
message = '"Work like hell"'
print(f'{famous_person} once said, {message}')


# SECTION 14: String Trimming Methods (strip, lstrip, rstrip)
# ============================================================================

name = "\t    Steve jobs and Tony Stark   \n"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

# Raw string
name_raw = r"\t Steve jobs and Tony Stark \n"
print(name_raw)


# SECTION 15: File Extension Removal
# ============================================================================

filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))


# SECTION 16: Direct String Output
# ============================================================================

print('Elon Musk once said, "When something is important enough, you do it even if the odds are not in your favour"')


# SECTION 17: Title Case with Character and Word Count
# ============================================================================
# Write a program to print the sentence in title case and show character & word counts. Ignore extra spaces.

user = input("Enter a sentence: ")
clean = user.strip()
title_case = clean.title()
word_count = len(clean.split())
char_count = len(clean.replace(" ", ""))

print("Title case:", title_case)
print("Character count:", char_count)
print("Word count:", word_count)


# SECTION 18: Title Case with Stats (Variant)
# ============================================================================
# Remove side spaces, convert to title case, and display character count and word count. Output must be clear.

user = input("Enter your sentence: ")
cleaned = user.strip().title()
words = cleaned.split()
char_count = len(cleaned.replace(" ", ""))

print("Title case:", cleaned)
print("Word count:", len(words))
print("Character count:", char_count)


# SECTION 19: Compare Two Names (Case and Space Insensitive)
# ============================================================================
# Compare two names and check if they're the same. Ignore case and extra spaces.

name1 = input("enter your name: ")
name2 = input("enter your name: ")
clean_name1 = name1.strip().lower()
clean_name2 = name2.strip().lower()

if clean_name1 == clean_name2:
    print('Same')
else:
    print("Not same")


# SECTION 20: Compare First and Last Name
# ============================================================================
# Compare two name inputs. If they are same (ignoring case and extra spaces), print "Same". Otherwise, print "Different".

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

case_space = first_name.lower().strip()
case_space2 = last_name.lower().strip()

if case_space2 == case_space:
    print("Same")
else:
    print("Different")


# SECTION 21: Count Exact Word Matches
# ============================================================================
# Count how many times a word appears as a separate word (not as part of another word).

customer = input("enter your sentence: ")
word = ("Eliyas")

customer_lower = customer.strip().lower()
word_lower = word.strip().lower()
words = customer_lower.split()
count = words.count(word_lower)

print(f"The word {word} appears {count} times.")


# SECTION 22: Find Keyword First and Last Position
# ============================================================================
# Input a sentence and a keyword.
# If keyword exists (case-insensitive), show:
#   - First position using .find()
#   - Last position using .rfind()
# Else, show "Keyword not found".

user = input("Enter the sentence: ").lower()
keyword = input("Enter the keyword: ").lower()

if keyword in user:
    print("First position is:", user.find(keyword))
    print("Last position is:", user.rfind(keyword))
else:
    print("keyword not found")


# ============================================================================
# Strings Summary:
# - upper(), lower(), title() for case conversion
# - strip(), lstrip(), rstrip() for whitespace removal
# - split() to break sentences into words
# - find(), rfind() to locate substrings
# - in operator to check substring existence
# - count() for substring and word occurrences
# - len() for length calculation
# - f-strings for formatting with variables
# - removesuffix() to remove file extensions
# - Raw strings with r prefix
# - Password masking techniques
# - Case and space insensitive comparison
# ============================================================================