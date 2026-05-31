import time
income = 0
expenses = 0
username = "Moh"
transaction = ""

def input_handling(op):
    while True:
        try:
            select = int(input("-> "))
            if select in op:
                return select
            else:
                print("Please select a valid option")
        except ValueError:
            print("Please enter a number!")

def greeting():
    print("Hello", username, "welcome back!")

def check_transaction():
    try:
        with open("transaction.txt", "r") as file:
            global transaction
            transaction = file.read()
            print("here is the last transaction: ")
            print(transaction)
    except FileNotFoundError:
        print("Error: no such file is found")

def current_balance():
    print("##############################")
    print(f"income: {income}$")
    print(f"expenses: {expenses}$")
    print(f"current balance is: {income - expenses}$")
    print("##############################")
    time.sleep(3)

def add_transaction():
    print("#########################")
    option = [1,2]
    global income
    global expenses

    print("please select an option: ")
    print("1 - income")
    print("2 - expenses")
    choice = input_handling(option)

    if choice == 1:
        while True:
            try:
                add = int(input("Add amount: "))
                income += add
                break
            except ValueError:
                print("please enter a valid number!")
    elif choice == 2:
        while True:
            try:
                cut = int(input("expenses amount: "))
                expenses += cut
                break
            except ValueError:
                print("please enter a valid number!")
    
    print(f"The net income is {income - expenses}")
    with open("transaction.txt", "a") as save:
        save.write("##################################\n")
        save.write(f"income: {income}\n")
        save.write(f"expenses: {expenses}\n")
        save.write(f"Net income: {income - expenses}\n")
    
    time.sleep(3)

def load_transactions():
    global income, expenses
    try:
        with open("transaction.txt", "r") as file:
            lines = file.readlines()
        
        print("DEBUG lines:", lines)  # add this
        
        for line in reversed(lines):
            if line.startswith("income:"):
                print("FOUND income line:", repr(line))  # add this
                income = int(line.split(":")[1].strip())
            if line.startswith("expenses:"):
                print("FOUND expenses line:", repr(line))  # add this
                expenses = int(line.split(":")[1].strip())

    except FileNotFoundError:
        pass 

def option():
    option = [1,2,3]
    print("#################################")
    print("Select option: ")
    print("1 - check balance")
    print("2 - add transaction")
    print("3 - quit session")
    
    return input_handling(option)
    




greeting()
load_transactions()
print(f"DEBUG income={income} expenses={expenses}") 

while True:
    choice = option()

    if choice == 1:
        current_balance()
    elif choice == 2:
        add_transaction()
    elif choice == 3:
        exit()
    
        

