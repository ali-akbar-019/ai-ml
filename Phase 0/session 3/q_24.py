pin = int(input("Enter the pin: "))
correct_pin = 1234
balance = 10000

if(pin == correct_pin):
    amount = int(input("Withdraw Amount: "))
    if amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        print(amount,"has been withdrawn from your account")
else:
    print("Invalid Pin")