#ok now that we know all the variable type it time we know the basic operation 
#input and output operation
#we already figure out an ouput operation in the previous lesson 
print("hello world!")
#but it time for the user to actully give us some input from there end too
#This will allow for the user to input some text and hit the enter key when they are done. Since we typically want to store what the user inputted we declare a variable to hold that input (see below).
response = input()
print(response)

#but we actully make it more intresting because input() can also act as a print() function
name = input("please insert your name: ")
print("hello ", name + "!") #difference between comma and a plus is after the comma the print() will autmatically add a space after it

#now for operators:
 
1 + 1 == 2  # addition 

1 - 1 == 0# subtraction

5/2 == 2.5 # division

5*2 == 10 # multiplication 

5**2 == 25 # exponential

5 // 2 == 2# integer division (removes decimal portion)

5 % 2 == 1  # modulus (gives remainder of division) 

x = 5
y = 6

d = 12 % 5     # d is 2
z = x + y      # z is 11
w = x - y      # w is -1
q = 5 * 6      # q is 30
u = 10 / x     # u is 2.0
p = 10 * 2.0   # p is 20.0
t = x ** 3     # t is 125
c = 28 // y    # c is 5

#operation for string 
newStr = "hello" + "tim"  # newStr is "hellotim"
newStr2 = "python" * 3    # newStr2 is "pythonpythonpython"

#now let put this all together 
print("hello let add two numbers together !")
fv1 = input("please enter your first number: ")
fv2 = input("please enter your second number: ")

SUM_fv12 = int(fv1) + int(fv2) #don't forget to specify the variable type 
#because user input is always stored as str!
print("your total value is:",SUM_fv12)
