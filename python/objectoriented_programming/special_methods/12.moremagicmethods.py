# More magic methods
# Example with car class

class Car:
    def __init__(self, model, mileage):
        self.model = model
        self.mileage = mileage
        self.features = []
 
    # Returns the length, of the features list
    def __len__ (self):
        return len(self.features)
    
    # Retrieves a feature by index
    def __getitem__(self, index):
        return self.features[index]
    
    # Sets a feature by index
    def __setitem__(self, index, value):
        self.features[index] = value

    # Deletes a feature by index
    def __delitem__(self, index):
        del self.features[index]

    # Returns an iterator for the featured list
    def __iter__(self):
        return iter(self.features)
    
    # Checks is a feature is int the list
    def __contains__(self, feature):
        return feature in self.features
    

# Example usage

myCar = Car("Bmw", 3000)
myCar.features.extend(["Air Conditioning", "Sunroof", "Leather Seats"])
# .extend allows you to append alot of items

print(len(myCar)) # output: 3
print(myCar[0]) # output: Air Conditioning

myCar[1] = "Heated seats"
print(myCar[1]) # output: Heated seats

del myCar[2]
print(list(myCar))
# output: ['Air Conditioning', 'Heated seats']

print("Sunroof" in myCar)
