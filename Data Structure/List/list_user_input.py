lenght= int(input("Enter Lenght of List: "))
l=[]
for i in range(0 , lenght):
    data= input("Enter data" + str([i]) + ": ")
    l.append(data)
    
print(l)