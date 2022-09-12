########## __add__ ##########
class Sum: 
    def __init__(self, pages):
        self.pages = pages
    
    def __add__(self, others):
        return self.pages + others.pages

s1= Sum(100)
s2= Sum(200)
print(s1+s2)

########## __gt__ ##########
class Student:
    def __init__(self, name, marks):
        self.name= name
        self.marks= marks

    def __gt__(self, others):
        return self.marks > others.marks

std1= Student("Aswad", 600)
std2= Student("Abad", 500)
ans= std1>std2

if ans==True:
    print(std1.name,"Student1 wins!")
else:
    print(std1.name,"Student2 wins!")