# SLICE OPERATOR SUMMARY

# syntax
# == myList[start:stop:step] ==

# IMPORTANT:
# start = included
# stop = excluded
# step = jump size

text = "programming"

text[0:4]    # "prog"
text[::2]    # every 2 letters
text[::-1]   # reverse string

# NEGATIVE INDEXING
text[-1]     # last character
text[-2:]    # last 2 characters

# LIST SLICING
numbers = [10, 20, 30, 40, 50]

numbers[1:3]     # [20, 30]
numbers[::-1]    # reverse list

# INSERT using slices
numbers[2:2] = [999]
# inserts 999 at index 2

# REPLACE using slices
numbers[2:3] = [777]
# replaces item at index 2

# NORMAL replace
numbers[2] = 555
# replace one item directly