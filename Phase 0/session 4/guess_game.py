import random

secret_number = random.randint(1, 100)

guess_count = 0
while True:
    guess = int(input("Guess a number between 0 - 100"))
    if(guess == secret_number):
        print("Guessed",secret_number, " in ",guess_count, "tries")
        break
    elif guess > secret_number:
        print("Your guess is larger")
    elif guess < secret_number: 
        print("Your guess is smaller")

    guess_count +=1
    if guess_count == 4:
        print("You have reached the guess limit")
        break