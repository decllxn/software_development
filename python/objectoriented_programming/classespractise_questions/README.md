## 1. Creating Classes and Objects:

Define a class Car with attributes make, model, and year. Initialize these attributes in the constructor (__init__ method).
Create two objects, car1 and car2, of the Car class with different make, model, and year values.
Print the attributes of each car object using dot notation (e.g., car1.make).
## 2. Object Methods:

Add a method greet_owner to the Car class that takes the owner's name as an argument and prints a personalized greeting message.
Call the greet_owner method on both car1 and car2 objects with different owner names.
## 3. Modifying Object State:

Add a method drive to the Car class that increases the car's mileage by a specified amount (e.g., 10 miles).
Create a new object car3 of the Car class.
Call the drive method on car3 a few times to simulate driving.
Print the mileage of car3 to see the updated value.
## 4. Class Inheritance:

Define a new class ElectricCar that inherits from the Car class.
Add a new attribute battery_range (in miles) to the ElectricCar class. Initialize it in the constructor.
Create an object electric_car of the ElectricCar class, providing appropriate values for inherited and new attributes.
Print the details of electric_car, including inherited and specific attributes.
## 5. Method Overriding:

Override the greet_owner method in the ElectricCar class to include a message about the car being electric.
Call the greet_owner method on both electric_car and a Car object to observe the different behavior.
Bonus Challenge:

Implement a class BankAccount with attributes account_number, balance, and methods for depositing, withdrawing, and checking the balance.
Enforce constraints on withdrawals (e.g., prevent negative balances).
Create multiple bank account objects and simulate transactions.