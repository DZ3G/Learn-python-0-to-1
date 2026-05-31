# ==============================
# STRING METHODS - SUMMARY
# ==============================

# String methods are built-in tools in Python
# They are used like: data.method()

# They help manipulate and clean strings easily


# ==============================
# 1. .strip()
# ==============================

# Removes spaces at the beginning and end of a string

text = "   hello   "
print(text.strip())

# Output: "hello"


# ==============================
# 2. .split()
# ==============================

# Splits a string into a list of words (by default spaces)

text = "my name is lucas"
words = text.split()

print(words)

# Output: ["my", "name", "is", "lucas"]


# You can also choose a separator:
text2 = "apple,banana,orange"
fruits = text2.split(",")

print(fruits)

# Output: ["apple", "banana", "orange"]


# ==============================
# 3. .lower()
# ==============================

text = "HeLLo WoRLD"
print(text.lower())

# Output: "hello world"


# ==============================
# 4. .upper()
# ==============================

text = "hello world"
print(text.upper())

# Output: "HELLO WORLD"


# ==============================
# 5. len()
# ==============================

text = "hello world"
print(len(text))

# Output: 11 (includes spaces)


# ==============================
# REAL USE CASE (VERY IMPORTANT)
# ==============================

answer = input("What is my name? ")

if answer.lower().strip() == "tim":
    print("Correct!")
else:
    print("Incorrect")


# ==============================
# WHY THIS IS IMPORTANT
# ==============================

# - .strip() removes accidental spaces from user input
# - .lower() makes comparison case-insensitive
# - prevents user mistakes from breaking logic