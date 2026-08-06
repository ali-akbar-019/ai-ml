class GuessLimitException(Exception):
    def __init__(self,message):
        super().__init__(message)

try:
    guess = 0
    password = "ali_akbar"
    while True:
        user_guess = input("Guess the password: ")
        if user_guess == password:
            print("Password guess correctly")
            break
        guess+=1
        if(guess >= 3):
            raise GuessLimitException("Guess limit reached")
except GuessLimitException as err:
    print(err)
finally:
    print("Execution Completed")
