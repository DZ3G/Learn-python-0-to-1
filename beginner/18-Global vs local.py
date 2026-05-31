# ==========================================
# GLOBAL VS LOCAL VARIABLES - QUICK NOTES
# ==========================================


# ==========================================
# LOCAL VARIABLES
# ==========================================

# A variable created INSIDE a function is LOCAL.
# It only exists within that function.
# You cannot access it from outside.

def myFunc():
    y = 7
    print(y)  # Works fine inside the function

myFunc()
# print(y)  # ERROR: y is not defined outside the function

# Rule: local variables live and die inside their function.


# ==========================================
# GLOBAL VARIABLES
# ==========================================

# A variable created OUTSIDE any function is GLOBAL.
# All functions can read it.

x = 7

def myFunc2():
    print(x)  # Works! x is global, visible everywhere

myFunc2()  # OUTPUT: 7


# ==========================================
# TRYING TO MODIFY A GLOBAL FROM A FUNCTION
# ==========================================

# Attempting to change a global variable inside a function
# actually creates a NEW local variable — it doesn't touch the global!

x = 7

def myFunc3():
    x = 5       # This creates a LOCAL x, not the global one!

myFunc3()
print(x)        # OUTPUT: 7  (global x was not changed)


# ==========================================
# THE GLOBAL KEYWORD
# ==========================================

# To actually modify a global variable from inside a function,
# use the "global" keyword to declare your intent.

x = 7

def myFunc4():
    global x    # Tell Python: "I mean the global x"
    x = 5

myFunc4()
print(x)        # OUTPUT: 5  (global x was changed)


# ==========================================
# WARNING: AVOID GLOBAL VARIABLES
# ==========================================

# Using global variables is generally BAD practice because:
# - Functions become dependent on external state
# - Harder to reuse functions in other programs
# - Makes code harder to debug and maintain

# ACCEPTABLE use: program-specific functions that will never be reused.

# PREFERRED approach: pass values as arguments and return results.

x = 7

def myFunc5(value):     # Receive the value as a parameter
    value = 5
    return value        # Return the new value instead

x = myFunc5(x)
print(x)                # OUTPUT: 5 (clean, no global needed)


# ==========================================
# SUMMARY
# ==========================================

# | Concept       | Where defined       | Accessible where?        |
# |---------------|---------------------|--------------------------|
# | Local var     | Inside a function   | Only inside that function |
# | Global var    | Outside functions   | Everywhere               |
# | global keyword| Inside a function   | Lets you modify the global|

# Prefer passing arguments and returning values over using global.