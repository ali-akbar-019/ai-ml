
# simple calculator
def addition(num1, num2):
    res = num1  + num2
    print("Addition: ", res)
    menu()
def subtraction(num1, num2):
    res = num1  - num2
    print("Subtraction: ", res)
    menu()
def multiplication(num1, num2):
    res = num1  * num2
    print("Multiplication: ", res)
    menu()
def divide(num1, num2):
    res = num1  / num2
    print("Division: ", res)
    menu()
def menu():
    choice = int(input("""
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
"""))
   
    if choice == 1:
        num1 = int(input("num1: "))
        num2 = int(input("num2: "))
        addition(num1,num2)
    elif choice == 2:
        num1 = int(input("num1: "))
        num2 = int(input("num2: "))
        subtraction(num1,num2)
    elif choice == 3:
        num1 = int(input("num1: "))
        num2 = int(input("num2: "))
        multiplication(num1, num2)
    elif choice == 4:
        num1 = int(input("num1: "))
        num2 = int(input("num2: "))
        divide(num1, num2)
    else:
        return
    

menu()