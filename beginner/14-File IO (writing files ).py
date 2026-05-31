# file_io_writing.py
# Beginner Python - File I/O (Writing Files)

# -----------------------------------
# 1. Writing to a file (overwrite mode)
# -----------------------------------

# "w" mode = write (creates file or overwrites existing one)

file = open("example.txt", "w")

file.write("Hello World!\n")
file.write("This is my first file write.\n")
file.write("Python file I/O is simple.\n")

file.close()

print("File written successfully!")


# -----------------------------------
# 2. Reading back what we wrote
# -----------------------------------

file = open("example.txt", "r")

content = file.read()
print("\nFILE CONTENT:\n")
print(content)

file.close()


# -----------------------------------
# 3. Appending to a file (add more text)
# -----------------------------------

# "a" mode = append (does NOT delete existing content)

file = open("example.txt", "a")

file.write("This line was appended later.\n")
file.write("We did not overwrite the file.\n")

file.close()

print("Text appended successfully!")


# -----------------------------------
# 4. Read again to see changes
# -----------------------------------

file = open("example.txt", "r")

print("\nUPDATED FILE CONTENT:\n")
print(file.read())

file.close()


# -----------------------------------
# 5. Better practice (recommended way)
# using "with" (auto-closes file)
# -----------------------------------

print("\nUSING WITH STATEMENT:\n")

with open("example.txt", "w") as file:
    file.write("Using 'with' automatically closes the file.\n")
    file.write("This is the safest way to handle files.\n")

# no need to call close() 

with open("example.txt", "r") as file:
    print(file.read())


# -----------------------------------
# 6. Key modes summary (important)
# -----------------------------------

print("\nFILE MODES:")
print("r = read")
print("w = write (overwrite)")
print("a = append")
print("r+ = read and write")