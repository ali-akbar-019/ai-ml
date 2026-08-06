class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    pass

dog = Dog()
dog.eat()


class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("I am ", self.name)

class Student(Person):
    def __init__(self, name, cgpa):
        super().__init__(name)
        self.cgpa = cgpa
    def introduce(self):
        super().introduce()
        print("I am ", self.name, " and my CGPA: ", self.cgpa)

st = Student("ali akbar", 3.99)
st.introduce()


