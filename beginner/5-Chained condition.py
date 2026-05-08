# ================================================================
#   LESSON: CHAINED CONDITIONALS & NESTED STATEMENTS
# ================================================================


# ----------------------------------------------------------------
# 1. THE THREE KEYWORDS: and, or, not
# ----------------------------------------------------------------

# AND → both conditions must be True to get True
print(True and False)   # False
print(True and True)    # True
print(False and False)  # False

# OR → at least one condition must be True to get True
print(True or False)    # True
print(True or True)     # True
print(False or False)   # False

# NOT → flips the result
print(not True)         # False
print(not False)        # True


# ----------------------------------------------------------------
# 2. COMBINING KEYWORDS
# ----------------------------------------------------------------

print((True or False) and False)    # False
print(False and True and True)      # False
print((True or False) and True)     # True
print(True and not False)           # True

print(not (1 > 2 and 2 - 7 == -5)) # True


# ----------------------------------------------------------------
# 3. USING AND / OR TO ALLOW OR REJECT VALUES
# ----------------------------------------------------------------

# AND → use when BOTH conditions must pass (narrowing)
# example: only allow adults with a valid ID
age = 20
has_id = True
if age >= 18 and has_id:
    print("Welcome in!")

# OR → use when EITHER condition is enough to reject (widening net)
# example: reject ages that are too low OR too high
age = -5
if age < 0 or age > 120:
    print("Invalid age.")

# COMMON MISTAKE: using AND when you mean OR for exclusion
# WRONG:  if age < 0 and age > 120  → NEVER triggers (impossible)
# RIGHT:  if age < 0 or age > 120   → catches both bad ends


# ----------------------------------------------------------------
# 4. BOUNDARY CONDITIONS — always double check <= vs <
# ----------------------------------------------------------------

# "between 12 and 17" means 12 and 17 ARE included → use <=
age = 12
if 12 <= age <= 17:
    print("Teen price")   # prints — 12 is included

# WRONG: 12 < age < 17 would miss age 12 and age 17 entirely


# ----------------------------------------------------------------
# 5. COMBINING WITH IF STATEMENTS
# ----------------------------------------------------------------

food = "pizza"
drink = "juice"

if food == "pizza" and drink == "juice":
    print("Those are my favorite as well!")
else:
    print("One of those is not my favorite.")


# ----------------------------------------------------------------
# 6. NESTED STATEMENTS
# ----------------------------------------------------------------
# Nesting = putting an if inside another if.
# Each nested level adds 4 spaces of indentation.

answer = "20"

if int(answer) >= 18:
    country = "canada"
    if country == "canada":
        print("Me as well!")
    else:
        print("Oh, I do not live there.")


# ----------------------------------------------------------------
# 7. FULL EXAMPLE — cinema ticket pricing
#    combines: functions, nested ifs, and, or, not, exit()
# ----------------------------------------------------------------

def get_price(age, weekend):
    if age < 12:
        price = 5
    elif 12 <= age <= 17:
        price = 8
    elif 18 <= age <= 64:
        price = 12
        if weekend == True:     # nested: surcharge only for adults
            price += 3
    else:
        price = 7
    return price                # return, don't print inside the function


age = int(input("Age: "))
weekend_input = input("Is it the weekend? (y/n): ")

# validate inputs before doing anything
if age < 0 or age > 120:
    print("Invalid age.")
    exit()

if weekend_input == "y":
    weekend = True
elif weekend_input == "n":
    weekend = False
else:
    print('Please type "y" or "n".')
    exit()

print(f"Ticket price: ${get_price(age, weekend)}")


# ----------------------------------------------------------------
# 8. QUICK REFERENCE
# ----------------------------------------------------------------

# Situation                              Keyword to use
# -------------------------------------------------------
# Both things must be true to allow   →  and
# Either wrong should reject           →  or
# Flip a condition                     →  not
# Value outside a range (too low/high) →  or
# Value inside a range                 →  and  (or chained <=)
# Neither this nor that                →  and  (not x and not y)
# Either this or that is enough        →  or

# ================================================================