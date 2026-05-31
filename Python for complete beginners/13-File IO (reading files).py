# file_io_reading.py
# Beginner Python - File I/O (Reading Files)

# -----------------------------
# 1. Opening a file (basic way)
# -----------------------------

# "r" = read mode
file = open("example.txt", "r")

# -----------------------------
# 2. Reading the entire file
# -----------------------------

content = file.read()
print("FULL FILE CONTENT:\n")
print(content)

# Always close the file when done
file.close()


# -----------------------------
# 3. Reading line by line
# -----------------------------

file = open("example.txt", "r")

print("\nLINES:\n")
line = file.readline()

while line != "":
    print(line.strip())  # remove \n
    line = file.readline()

file.close()


# -----------------------------
# 4. Reading all lines into a list
# -----------------------------

file = open("example.txt", "r")

lines = file.readlines()

print("\nLIST OF LINES:")
print(lines)

# Removing newline characters
clean_lines = []

for line in lines:
    clean_lines.append(line.strip())

print("\nCLEAN LINES:")
print(clean_lines)

file.close()


# -----------------------------
# 5. Better practice (recommended)
# using "with" (auto closes file)
# -----------------------------

print("\nUSING WITH STATEMENT:\n")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# File is automatically closed here


# -----------------------------
# 6. Simple processing example
# -----------------------------

with open("example.txt", "r") as file:
    lines = file.readlines()

print("\nNUMBER OF LINES:", len(lines))

for i, line in enumerate(lines):
    print(f"Line {i + 1}: {line.strip()}")