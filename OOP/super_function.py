class Person:
    def __init__(self, id, name):
        self.id= id
        self.name= name

    def display(self):
        print("Id:", self.id)
        print("Name: ", self.name)

class Employee(Person):
    def __init__(self, id, name, age, address):
        super().__init__(id, name)
        self.address= address
        self.age= age
    
    def display(self):
        super().display()
        print("Address: ", self.address)
        print("Age: ", self.age)

emp = Employee(193329, "Aswad", 19, "Lahore")
emp.display()

