# Multiple inheritance is a feature in OOP where a class can inherit attributes and methods from more than one parent class
# Example

class Flyer:
    def fly(self):
        print("Flying...")

class Swimmer:
    def swim(self):
        print("Swimming...")

class Crawler:
    def crawl(self):
        print("Walking...")

class water_birds(Flyer, Swimmer):
    pass

duck = water_birds()
# You can use methods from 2 different classes
duck.fly()
duck.swim()
