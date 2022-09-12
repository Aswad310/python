class Teacher:
    # constructor
    def __init__(self):
        print("Constructor is Running : : : : ")
    
teacher= Teacher()

# Non- Parameterised Constructor
class Student:
    def __init__(self):
        self.id=1
        print("Student Id: ", self.id)

student= Student()
student= Student()

# Parameterised Constructor
class Student:
    def __init__(self, id):
        self.id=id
        print("Student Id: ", self.id)

student= Student(193320)
student= Student(193321)