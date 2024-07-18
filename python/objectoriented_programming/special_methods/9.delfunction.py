#!/usr/bin/env python3
# Automatic invokation: The del method is called automaticaly when an object's reference count
# drops to zero.

# Unpredictable timing: Unlike constructors, init, the exact time when a destructor is called is not predictable
# and can be different from one run to the next.
# it depends on when the python garbage collector decides to delete the object

# Example

class FileManager:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        print(f"File {filename} opened.")

    def write(self, data):
        self.file.write(data)
    
    def __del__(self):
        self.file.close()
        print(f"File {self.file.name} closed.")

# Creating an instance
file_manager = FileManager('example.txt')
file_manager.write('Hello World!')

# Deleting the instance
del file_manager