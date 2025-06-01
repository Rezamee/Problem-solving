def gen ():
    a = str(input("enter a :"))
    b = str(input("enter b :"))
    c = len(a)//2
    d = len(b)//2
    gen = a[:c:1] + b[d::1]
    print(gen) 
    menu()


def sum():
    a = float(input("Enter first number : "))
    b = float(input("Enter second number : "))
    print(a + b)
    menu()


def sub():
    a = float(input("Enter first number : "))
    b = float(input("Enter second number : "))
    print (a - b)
    menu()


def mult():
    a = float(input("Enter first number : "))
    b = float(input("Enter second number : "))
    print (a * b)
    menu()


def div():
    a = float(input("Enter first number : "))
    b = float(input("Enter second number : "))
    print (a / b)
    menu()


def exp():
    a = float(input("Enter first number : "))
    b = float(input("Enter second number : "))
    print (a ** b)
    menu()


def fib ():
    x = int(input("Enter index:"))
    a,b = 0,1
    for _ in range (x):
        a,b = b, a+b
    print (a)
    menu()


def lucas ():
    x = int(input("Enter index:"))
    a,b = 2,1
    for _ in range (x):
        a,b = b, a+b
    print (a)
    menu()


def pell ():
    x = int(input("Enter index:"))
    a,b = 0,1
    for _ in range (x):
        a,b = b, 2*b+a
    print (a)
    menu()


def bTod ():
    binary = input("Enter your number:")
    decimal = int(binary, 2)
    print (decimal)
    menu()


import random
def game ():
    target = random.randint(1, 10)
    guess = int(input("guess : "))
    if guess == target:
        print("correct")
    else:
        print(f"wrong, the number was {target}")
    menu()

def menu():
    print("------MENU------")
    print("")
    print("Menu")
    print("1.Sum")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exponentiation")
    print("6.Genetic Algorithm")
    print("7.Fibonacci Sequence")
    print("8.Lucas Sequence")
    print("9.Pell Sequence")
    print("10.Binary to Decimal")
    print("11.guessing game")
    print("12.Exit")
    print("")
    choise = int(input("Enter your operation number:"))
    if choise == 1:
        print ("Sum :", sum())
    elif choise == 2:
        print ("Subtraction :", sub())
    elif choise == 3:
        print ("Multiplication :", mult())
    elif choise == 4:
        print ("Division :", div())
    elif choise == 5:
        print ("Exponentiation :", exp())
    elif choise == 6:
        print (gen ())
    elif choise == 7:
        print("the Fibonacci number is :" , fib())
    elif choise == 8:
        print("the Fibonacci number is :" , lucas())
    elif choise == 9:
        print("the Pell number is :" , pell())
    elif choise == 10:
        print(bTod())
    elif choise == 11:
        print(game())
    elif choise == 12:
        print("Bye!")
        exit()
    else:
        print("invalid choise!")
        menu()
print(menu())


        
        
    