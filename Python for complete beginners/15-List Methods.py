# list_methods_count_index.py
# Beginner Python - List Methods (.count() and .index())

# -----------------------------------
# 1. What is .count()?
# -----------------------------------
# .count() returns how many times an item appears in a list

my_list = ["a", "b", "b", "a", "c", "d"]

print("Original list:", my_list)

print("\nCOUNT METHOD EXAMPLES:")
print("Count of 'a':", my_list.count("a"))  # 2
print("Count of 'b':", my_list.count("b"))  # 2
print("Count of 'z':", my_list.count("z"))  # 0 (not found)


# -----------------------------------
# 2. What is .index()?
# -----------------------------------
# .index() returns the FIRST position of an item in the list

print("\nINDEX METHOD EXAMPLES:")
print("Index of 'a':", my_list.index("a"))  # 0
print("Index of 'b':", my_list.index("b"))  # 1

# WARNING:
# If the item does not exist, .index() will crash with an error
# print(my_list.index("z"))  # ValueError


# -----------------------------------
# 3. Safe way to use index (check first)
# -----------------------------------

item = "c"

if my_list.count(item) > 0:
    print(f"\n'{item}' exists at index:", my_list.index(item))
else:
    print(f"\n'{item}' not found in list")


# -----------------------------------
# 4. Practical example (real use case)
# -----------------------------------

students = ["Tim", "Anna", "John", "Anna", "Mike"]

name_to_check = "Anna"

print("\nSTUDENT LIST ANALYSIS:")
print("Students:", students)

print(f"How many times '{name_to_check}' appears:",
      students.count(name_to_check))

print(f"First position of '{name_to_check}':",
      students.index(name_to_check))


# -----------------------------------
# 5. Important notes (VERY IMPORTANT)
# -----------------------------------

print("\nIMPORTANT NOTES:")
print("- .count(x) → number of times x appears")
print("- .index(x) → first position of x only")
print("- .index(x) crashes if x is not in the list")
print("- Use .count() first if you're unsure")