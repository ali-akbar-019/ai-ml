# Encapsulation

# Encapsulation means:

# Keeping data and methods together, while protecting important data.


class Student:
    def __init__(self):
        self.name = "Ali"


std = Student()

print(std.name)

class Student2:
    def __init__(self, name):
        self.__name = name
    def getName(self):

        return self.__name

std2 = Student2("ali")
print(std2._Student2__name) #ese access kar sakte a, cz python me private nahi hota q k ye mature logo ki lang ha , jab access nai krna chahte to na karo ye public private kya ha
print(std2.getName())
    