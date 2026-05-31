# ==========================================
# CATCHING ERRORS (TRY / EXCEPT)
# ==========================================

# Sometimes code crashes when an error occurs.

# Example:

num = input("Enter a number: ")

# int("hello") causes an error
# because Python cannot convert "hello" to an integer

try:
    num = int(num)
    print(num + 5)
except:
    print("That is not a valid number")


# ==========================================
# HOW IT WORKS
# ==========================================

# try:
#     code that MIGHT fail
#
# except:
#     code that runs if an error occurs


# Example:

try:
    result = 10 / 0
    print(result)
except:
    print("Cannot divide by zero!")


# ==========================================
# WHY USE IT?
# ==========================================

# Without try/except:
#
# Program crashes ❌
#
# With try/except:
#
# Program continues running ✅


# ==========================================
# COMMON USE CASE
# ==========================================

while True:
    try:
        age = int(input("Enter your age: "))
        print(f"You are {age} years old")
        break
    except:
        print("Please enter a valid number")


# ==========================================
# SUMMARY
# ==========================================

# try:
#     risky code
# except:
#     handle the error

# Useful when:
# - Converting input
# - Reading files
# - Dividing numbers
# - Any operation that may fail

#exercice !
num = input("please give a number: ")

try:
    num = int(num)
    print("You entered:", num)
except:
    print("That's not a number!")

############################################

inp1 = input("First number: ")
inp2 = input("Scond number: ")

try: 
    inp1 = int(inp1)
    inp2 = int(inp2)
    result = inp1 + inp2
    print("Result:", result)
except:
    print("You entered a Invalid number(s)")

###################################################



while True: 
    try : 
        number = input("Enter a number: ")
        number = int(number)
        print("Thank you!")
        break
    except:
        print("Invalid number!")

