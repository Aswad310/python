# empty dictionary
d={}

emp= int(input("Enter total No. of employes"))
i=1
while i<=emp:
    emp_name= input("Enter Emp name: ")
    emp_sal= input("Enter Emp salery: ")
    d[emp_name]=emp_sal
    i= i+1

print(d)

for x in d:
    print("Employ name is:",x,"and his salary is:",d[x])
