import csv
with open("emp.csv", "w", newline='') as f:
   w=csv.writer(f)
   w.writerow(["EMP NO","EMP NAME","EMP SAL","EMP ADDR"])

   emp_no= int(input("Enter Emp Num: "))

   for x in range(emp_no):
    emp_no= int(input("Enter EMP NO: "))
    emp_name= input("Enter EMP NAME: ")
    emp_sal= int(input("Enter EMP SAL: "))
    emp_add= input("Enter EMP ADD: ")

    w.writerow([emp_no, emp_name, emp_sal, emp_add])

print("Data INSERTED. . .")