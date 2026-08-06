try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))

    print(a/b)

except ValueError:
    print("Please enter numbers only")
except ZeroDivisionError:
    print("Can not divide by zero")
    