from tkinter import Y


# List Concatination
x= ["asawd", "ali", "butt"]
y= [1, 2, 3]

z= x+y
print("List Concatination: ",z)

# Multiplication Operator
print("Multiplication Operator: ",2*z)

# Nested List
a = [80, 90]
b = [10, 20, 30, a]
print(b[0])
print(b[1])
print(b[2])
print(b[3])

## List Comprehensions
# 1
x = [1, 2, 3, 4]
y = []
for i in x:
   y.append(i*2)
# print(y)

# 2
x = [1, 2, 3, 4]
y = [i*2 for i in x]
# print(y)

#
print("HELLO")
s=range(1, 20, 3)
for i in s:  #This loop is for knowing what is in s
   print(i)
m=[x for x in s if x%2==0] #List comprehension
print(m)