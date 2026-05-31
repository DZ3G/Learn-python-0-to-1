# ==============================
# ITERATION BY ITEM - SUMMARY
# ==============================

# Iteration means looping through each element in a collection one by one.

# You can iterate over:
# - Lists
# - Strings
# - Tuples


# ==============================
# BASIC LOOP SYNTAX
# ==============================

# for item in collection:
#     print(item)


# ==============================
# LIST EXAMPLE
# ==============================

my_list = [1, 4, 6, "hi"]

for item in my_list:
    print(item)

# Output:
# 1
# 4
# 6
# hi


# ==============================
# STRING EXAMPLE
# ==============================

my_string = "hello"

for letter in my_string:
    print(letter)

# Output:
# h
# e
# l
# l
# o


# ==============================
# COMMON PATTERNS
# ==============================

# 1. COUNTING ITEMS

count = 0
items = ["admin", "user", "admin", "guest"]

for item in items:
    if item == "admin":
        count += 1

print(count)


# 2. FILTERING ITEMS (CREATE NEW LIST)

names = ["lucas", "admin", "maria", "admin", "john"]

clean_names = []

for name in names:
    if name != "admin":
        clean_names.append(name)

print(clean_names)


# 3. SEARCHING

numbers = [1, 2, 3, 4, 5]

for n in numbers:
    if n == 3:
        print("Found 3")


# ==============================
# IMPORTANT RULES
# ==============================

# - You read elements one by one
# - Do NOT modify a list while looping through it
# - Use a new list if you want to filter data
# - item = current element in loop