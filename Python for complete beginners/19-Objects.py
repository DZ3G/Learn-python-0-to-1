# ==========================================
# OBJECTS & CLASSES - QUICK NOTES
# ==========================================


# ==========================================
# WHAT IS AN OBJECT?
# ==========================================

# In Python, almost EVERYTHING is an object.
# When you create a variable, you are creating an object
# of a specific class (data type).

x = 1          # object of class int
name = "Alice" # object of class str
nums = [1, 2]  # object of class list

# Each class comes with its own attributes and methods.
# For example, integers can be added, divided, multiplied...
# Strings can be uppercased, split, stripped...


# ==========================================
# THE type() FUNCTION
# ==========================================

# Use type() to find out what class an object belongs to.

print(type("hello"))   # -> <class 'str'>
print(type(1))         # -> <class 'int'>
print(type([1, 3]))    # -> <class 'list'>
print(type(3.14))      # -> <class 'float'>
print(type(True))      # -> <class 'bool'>


# ==========================================
# WHAT IS A CLASS?
# ==========================================

# The built-in data types (int, str, list...) are just classes!
# That means we can CREATE OUR OWN data types by writing our own classes.

# Think of a class as a blueprint.
# An object is a house built from that blueprint.
# You can build many houses (objects) from one blueprint (class).


# ==========================================
# CREATING A CLASS
# ==========================================

class Number:
    def __init__(self):       # Constructor method
        self.var = 24         # Attribute: data stored on the object

    def display(self):        # Method: action the object can perform
        print(self.var)


# ==========================================
# CREATING AN INSTANCE (OBJECT)
# ==========================================

# "Instantiating" a class means creating a new object from it.

newNum = Number()    # This calls __init__() automatically
newNum.display()     # OUTPUT: 24

# We can create as many instances as we want:
anotherNum = Number()
anotherNum.display() # OUTPUT: 24


# ==========================================
# KEY VOCABULARY
# ==========================================

# class        -> the blueprint (e.g. Number)
# object       -> an instance built from the blueprint (e.g. newNum)
# __init__()   -> constructor: runs automatically when object is created
# self         -> refers to the current object being used
# attribute    -> a variable that belongs to the object (e.g. self.var)
# method       -> a function that belongs to the object (e.g. display())


# ==========================================
# SUMMARY
# ==========================================

# - Everything in Python is an object.
# - Objects belong to a class.
# - Use type() to check an object's class.
# - Classes are blueprints for creating custom objects.
# - __init__() is called automatically on creation.
# - self refers to the object itself inside the class.