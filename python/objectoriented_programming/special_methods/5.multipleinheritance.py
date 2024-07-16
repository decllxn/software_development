# In case of multiple inheritance, you need to be cautious how init methods are called
# Python calls the init method of the most derived class first, then the init method of the next

class A:
    def __init__(self, attributeA):
        self.attributeA = attributeA
    
class B:
    def __init__(self, attributeB):
        self.attributeB = attributeB

class C(A, B): # Multiple inheritance
    def __init__(self, attributeA, attributeB):
        A.__init__(self, attributeA) # Call init method of A
        B.__init__(self, attributeB) # Call the init method of A

object = C("valueA", "ValueB")
print(object.attributeA)
print(object.attributeB)