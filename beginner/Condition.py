<   # less than
<=  # less than or equal to
>   # greater than
>=  # greater than or equal to
==  # equal to
!=  # not equal to

x = 5
y = 9

x > y     # this is False
y == x    # this is False
x < y-1   # this is True
x+1 != y  # this is True
2.0 > 5   # this is False

"hello" == "hello"  # this is True
"tim" == "Tim"      # this is False, capital letter matter
"a" > "b"           # this is False can't use this operation
"apple" < "tim"     # this is False


"5" == 5 # this will return False

# NOT ALLOWED
2 > "hello"
3.0 < "tim"
# These result in error

#We can also declare variables to hold the values of conditions.

check = "tim" == "joe"
larger = 1 > 5
bothSame = larger == check  # This will be comparing two boolean values together
# if they are both the same we will get a True value