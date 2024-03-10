class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.reading=555

    def get_descriptive_name(self):
        long_name = (f"{self.year} {self.make} {self.model}")
        return long_name.title()

    def update_odometer(self, mileage):
        if mileage == self.reading:
            self.reading = mileage
            print(self.reading)
        else:
            print(f"You can not change an odometer! to {mileage}")

class Battery:
    def __init__(self,battery_size = 75):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

class ElectricCar(Car):
    def __init__(self, model,make,year):
        super().__init__(model, make, year)
        self.battery=Battery(67)
 
my_tesla = ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
