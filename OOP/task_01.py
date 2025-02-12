class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def show_info(self):
        print(f"Make: {self.make} \nModel: {self.model} \nYear: {self.year}")

car = Car("Toyota", "Camry", 2020)
car.show_info()
