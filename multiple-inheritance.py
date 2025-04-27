'''Create three classes:

Animal → has attribute type

Mammal inherits from Animal

Human inherits from Mammal

Task:

Create a Human object and set type = "Warm-blooded"

Print the value of type.'''

class animal:
    def __init__(self,type):
        self.type=type
        print(f"This is a  {self.type} animal")

class mammal(animal):
        print("This is a mammal")
class human(mammal):
    def deta(self):
        print("This is a human")


h=human("Warm-blooded")
h.deta()

