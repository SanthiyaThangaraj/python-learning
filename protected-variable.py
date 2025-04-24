'''Create a class Animal with:

A protected variable _type (e.g., "Mammal")

A method to print _type

Then create a child class Dog and access _type from the child class using an object of Dog'''

class animal:
    def __init__(self, type):
        self._type=type
    def types(self):
        print(f"Type of the animal: {self._type}")

class dog(animal):
    
    def show_type(self):
        print(f"Dog is a: {self._type}")

obj=dog("Mammal")
obj.types()
obj.show_type()
    
