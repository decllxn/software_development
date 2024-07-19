#!/usr/bin/env python3
# Overriding methods: When a method in the child class has the same name as the method
# in the parent class, the method in the child class overrides the one in the parent class

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):

    # Method overriden
    def greet(self):
        # super().greet() # Call's the parent's greet method
        print("Hello from Child")

## Example usage
child = Child()
child.greet()
# Output: Hello from Child



# Even when a method is overriden, you can still access the parent class method using
# super()
