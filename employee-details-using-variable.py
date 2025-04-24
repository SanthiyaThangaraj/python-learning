'''Create a class Employee with the following:

A public variable name

A protected variable _department

A private variable __salary

A method show_details() to print all three

Then create an object and call the method to display the values.'''

class employee:
    def __init__(self, name,dept,salary):
        self.name=name
        self._dept=dept
        self.__salary=salary

    def show_details(self):
        print(self.name)
        print(self._dept)
        print(self.__salary)

empl1=employee("Santhiya","Developer",10000)
empl1.show_details()
empl2=employee("Janu","Testing",12000)
empl2.show_details()
