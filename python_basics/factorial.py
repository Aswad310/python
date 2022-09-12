value= int(input("Give value to get Factorial: "))

fac= 1

for n in range(value):
    x= value-n
    fac= fac*x
print(fac)