class Fruits:
    def __init__(self, name: str):  # Specifying that the name is a string
        self._name = name
    
    # Getters and setters enable you to make the variables inaccessible
    def get_name(self):
        print('Getting name.')
        return self._name

    def set_name(self, new_name: str):
        self._name = new_name


if __name__ == "__main__": # Block to prevent it from running if the modeule is imported somewhere
    fruit = Fruits("banana")
    print(fruit.get_name())  # Output the name of the fruit
    fruit.set_name("apple")  # Set a new name for the fruit
    print(fruit.get_name())  # Output the new name of the fruit

  
# Another way to define the property wrapper

class Car:
    def __init__(self, name: str):
        self._name = name

    @property # This is a property wrapper
    def car_name(self):
        print(f'"{self._name}" was accessed')
        return self._name
    
    @car_name.setter  # The setter property
    def car_name(self, value):
        print(f'{self._name} is the now "{value}"')

    @car_name.deleter # The deleter property
    def car_name(self):
        print(f'"{self._name}" was deleted')
        del self._name
    
if __name__ == '__main__':
    car1 = Car('Pagani')
    print(car1.car_name)

    car1.car_name = 'BMW'

    del car1.car_name