#Create a class Employee with attributes name, id, and salary. Add a method to increment salary by a given percentage.

class employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def add(self):
        percent=int(input("Enter percent for increment: "))
        insalary=self.salary*percent
        self.salary+=insalary
        print(f"{self.name},\n Your salary is incremented by {percent}\n Current salary: {self.salary}")

company=employee("Santhiya",95,10000)
company.add()
