# ==========================================
# LISTS — CORE THINGS TO REMEMBER
# ==========================================


# CREATE A LIST
fruits = ["apple", "banana", "orange"]


# ACCESS ITEMS (INDEXING)
print(fruits[0])   # first item
print(fruits[-1])  # last item


# REPLACE AN ITEM USING INDEX
fruits[1] = "pear"


# FIND AN ITEM POSITION
pos = fruits.index("orange")


# REPLACE ITEM WITHOUT KNOWING INDEX
fruits[pos] = "mango"


# ADD ITEM TO END
fruits.append("grape")


# REMOVE SPECIFIC ITEM BY VALUE
fruits.remove("apple")


# REMOVE ITEM BY INDEX
del fruits[0]


# LOOP THROUGH A LIST
for item in fruits:
    print(item)