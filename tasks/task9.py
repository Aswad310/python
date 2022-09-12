class Employee:
        employee_name= "Aswad Ali"
        employee_age= "18"

# object creation
emp1= Employee()
print("Orginal Value:")
print(emp1.employee_name)
print(emp1.employee_age)

print("Modification Value:")
emp1.employee_name="Abad"
print(emp1.employee_name)
emp1.employee_age="16"
print(emp1.employee_age)