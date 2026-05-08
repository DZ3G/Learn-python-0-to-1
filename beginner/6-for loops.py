# A for loop repeats code multiple times.

# Example:

for x in range(3):
    print(x)

# Output:
# 0
# 1
# 2


# ------------------------------------------
# 2. LOOP VARIABLE
# ------------------------------------------

# "x" changes value every loop iteration.
# It is often called a counter variable.

for x in range(5):
    print("Current value:", x)


# ------------------------------------------
# 3. RANGE FUNCTION
# ------------------------------------------

# Syntax:
# range(start, stop, step)

# start -> where counting begins
# stop  -> where counting stops (NOT INCLUDED)
# step  -> how much to increase each time


# ------------------------------------------
# 4. range(stop)
# Starts at 0
# Increases by 1
# Stops BEFORE stop
# ------------------------------------------

for x in range(4):
    print(x)

# Output:
# 0
# 1
# 2
# 3


# ------------------------------------------
# 5. range(start, stop)
# ------------------------------------------

for x in range(2, 6):
    print(x)

# Output:
# 2
# 3
# 4
# 5


# ------------------------------------------
# 6. range(start, stop, step)
# ------------------------------------------

for x in range(0, 10, 2):
    print(x)

# Output:
# 0
# 2
# 4
# 6
# 8


# ------------------------------------------
# 7. IMPORTANT RULE
# ------------------------------------------

# The stop value is NEVER included.

for x in range(5):
    print(x)

# 5 is NOT printed


# ------------------------------------------
# 8. COMMON USES
# ------------------------------------------

# Repeat something multiple times

for x in range(3):
    print("Hello")


# Count numbers

for x in range(1, 6):
    print(x)


# Even numbers

for x in range(0, 11, 2):
    print(x)

