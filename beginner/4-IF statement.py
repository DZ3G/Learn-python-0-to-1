# ==========================================
# IF / ELIF / ELSE — QUICK REVIEW
# ==========================================

# ------------------------------------------
# 1. IF STATEMENT
# Runs code only if the condition is True
# ------------------------------------------

age = 20

if age >= 18:
    print("Adult")


# ------------------------------------------
# 2. ELSE STATEMENT
# Runs if the IF condition is False
# ------------------------------------------

score = 40

if score >= 50:
    print("Passed")
else:
    print("Failed")


# ------------------------------------------
# 3. ELIF STATEMENT
# Used to check multiple conditions
# ------------------------------------------

grade = 75

if grade >= 90:
    print("Excellent")

elif grade >= 70:
    print("Good")

else:
    print("Failed")


# ------------------------------------------
# 4. INDENTATION
# Python uses indentation to define blocks
# ------------------------------------------

x = 10

if x > 5:
    print("x is greater than 5")


# ------------------------------------------
# 5. EXECUTION ORDER
# Python checks from top to bottom
# Once a condition is True, the others stop
# ------------------------------------------

number = 8

if number > 5:
    print("A")

elif number > 2:
    print("B")

# Only "A" prints


# ------------------------------------------
# 6. NESTED IF
# IF statement inside another IF statement
# ------------------------------------------

username = "admin"
password = "1234"

if username == "admin":

    if password == "1234":
        print("Access granted")

    else:
        print("Wrong password")


# ------------------------------------------
# 7. COMPARISON OPERATORS
# ------------------------------------------

# <    less than
# <=   less than or equal
# >    greater than
# >=   greater than or equal
# ==   equal
# !=   not equal


# ------------------------------------------
# 8. LOGICAL OPERATORS
# ------------------------------------------

# and -> both conditions must be True
# or  -> one condition must be True
# not -> reverses True/False

country = "France"
age = 19

if age >= 18 and country == "France":
    print("Allowed")