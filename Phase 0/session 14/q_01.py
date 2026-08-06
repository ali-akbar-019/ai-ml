class Car:
    def __init__(self, brand, model):
        print("Car is created")
        self.brand = brand
        self.model = model
    def display(self):
        print(f"{self.brand} - {self.model}")


car1 = Car("Honda", 2001)
car1.display()

