# create function  
def sayHello(name):
    print(f"Hello {name}")


user = input("please type your name: ")
sayHello(user)

def square(n):
    return int(n)**2

number = input("please enter a number: ")
print(square(number))


def isEven(n):
    if int(n) % 2 == 0:
        return True
    else:
        return False

print(isEven(number))