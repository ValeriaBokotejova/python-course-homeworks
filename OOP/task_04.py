class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def show_info(self):
        print(f"Make: {self.make} \nModel: {self.model} \nYear: {self.year}")
    
class ElectricCar (Vehicle):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size
    def display_battery(self):
        print(f"Battery Size: {self.battery_size}")

tesla = ElectricCar("Tesla", "Model S", 2022, 100)

tesla.show_info()
tesla.display_battery()
