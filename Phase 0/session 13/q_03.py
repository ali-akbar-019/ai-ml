def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper

def greet():
    print("Hello")

greet = decorator(greet)
greet()

# can also do like this
@decorator
def greet2():
    print("Hello")

greet2()