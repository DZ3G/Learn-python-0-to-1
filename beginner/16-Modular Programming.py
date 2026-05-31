# ==========================================
# MODULAR PROGRAMMING - QUICK NOTES
# ==========================================

# What is a module?
# A module is simply another Python file (.py)
# that contains reusable code (functions, classes, variables).

# Why use modules?
# - Organize code
# - Reuse code
# - Avoid copy-pasting
# - Easier maintenance

# ==========================================
# FILE STRUCTURE
# ==========================================

# calculator.py

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b


# ==========================================
# IMPORT ENTIRE MODULE
# ==========================================

# main.py

import calculator

result = calculator.add(5, 3)
print(result)  # 8

# Syntax:
# import module_name
# module_name.function()


# ==========================================
# IMPORT SPECIFIC FUNCTIONS
# ==========================================

# main.py

from calculator import add

print(add(5, 3))

# Syntax:
# from module_name import function_name


# ==========================================
# IMPORT MULTIPLE FUNCTIONS
# ==========================================

from calculator import add, multiply

print(add(2, 3))
print(multiply(2, 3))


# ==========================================
# IMPORTANT
# ==========================================

# Both files must be in the same folder:

# project/
# ├── calculator.py
# └── main.py

# ==========================================
# SUMMARY
# ==========================================

# import module
# module.function()

# from module import function
# function()

# Modules help keep code clean and reusable.