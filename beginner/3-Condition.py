# ==========================================
# COMPARISON OPERATORS & CONDITIONS REVIEW
# ==========================================

# ------------------------------------------
# 1. COMPARISON OPERATORS
# ------------------------------------------

# <    less than
# <=   less than or equal to
# >    greater than
# >=   greater than or equal to
# ==   equal to
# !=   not equal to


# ------------------------------------------
# 2. NUMBER COMPARISONS
# ------------------------------------------

x = 5
y = 9

print(x > y)      # False
print(y == x)     # False
print(x < y - 1)  # True
print(x + 1 != y) # True
print(2.0 > 5)    # False


# ------------------------------------------
# 3. STRING COMPARISONS
# ------------------------------------------

print("hello" == "hello")  # True

# Capital letters matter
print("tim" == "Tim")      # False

# Python compares letters alphabetically
print("a" > "b")           # False
print("apple" < "tim")     # True


# ------------------------------------------
# 4. STRING VS NUMBER
# ------------------------------------------

# Different data types are not equal
print("5" == 5)  # False


# ------------------------------------------
# 5. INVALID COMPARISONS
# These create errors
# ------------------------------------------

# print(2 > "hello")
# print(3.0 < "tim")

# You cannot compare numbers and strings
# using <, <=, >, >=


# ------------------------------------------
# 6. CONDITIONS STORED IN VARIABLES
# ------------------------------------------

check = "tim" == "joe"
print(check)  # False

larger = 1 > 5
print(larger) # False


# ------------------------------------------
# 7. COMPARING BOOLEAN VALUES
# ------------------------------------------

bothSame = larger == check

# False == False -> True
print(bothSame)  # True