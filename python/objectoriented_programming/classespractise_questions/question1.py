class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def greet_owner(self, owner):
        print("Hello " + owner + " ,how are you doing?")

    def drive(self):
        mileage = ""
        return mileage + 40
    


car1 = Car("BMW", "M5 Competition", "2022")
car2 = Car("Mercedes", "AMG GT63s", "2024")

print(car1.make)
print(car1.model)
print(car1.year)

print(car2.make,"\n",car2.model,"\n",car2.year)

car1.greet_owner("Jeffery")
car2.greet_owner("Stacy")

car3 = Car("Audi", "Rs5", "2024")
car3.drive
car3.drive
car3.drive

print(car3.mileage)