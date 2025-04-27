'''Create a class Appliance with:
Attribute: power
Create a class Fan that inherits from Appliance and has:
Attribute: speed
Task:
Create a Fan object with power = 60W and speed = "High".
Print both attributes.'''


class appliance:
    def __init__(self, power,speed):
        self.power=power
        self.speed=speed
        print(f"Power: {self.power}")

class fan(appliance):
    def motor(self):
        print(f"Speed: {self.speed}")

obj=fan("60W","High")
obj.motor()
