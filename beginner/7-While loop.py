# ==========================================
# WHILE LOOPS — QUICK REVIEW
# ==========================================

# ------------------------------------------
# 1. WHAT IS A WHILE LOOP
# ------------------------------------------

# Repeats code while a condition is True

# Example:
# while condition:
#     do something


# ------------------------------------------
# 2. WHEN TO USE IT
# ------------------------------------------

# Use when you DON'T know how many times
# the loop will run


# ------------------------------------------
# 3. BASIC EXAMPLE
# ------------------------------------------

while False:
    print("Runs while condition is True")


# ------------------------------------------
# 4. INFINITE LOOP + BREAK
# ------------------------------------------

while True:
    user = input("Type 5 to stop: ")

    if user == "5":
        break

    print("Try again")


# ------------------------------------------
# 5. COMMON PATTERN (INPUT LOOP)
# ------------------------------------------

run = True

while run:

    answer = input("What is 5 + 7? ")

    if answer == "12":
        print("Correct!")
        run = False

    else:
        print("Try again")


# ------------------------------------------
# 6. KEY IDEAS
# ------------------------------------------

# - True condition → loop continues
# - False condition → loop stops
# - break → immediately exits loop