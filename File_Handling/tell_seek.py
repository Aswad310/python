data= "You are so Pro"

f= open("valo.txt", "w")
f.write(data)

with open("valo.txt", "r+") as f:
    data= f.read()
    print("Data before Modification: ",data)
    print("Cursor at first:",f.tell())
    f.seek(11)
    print("Cursor at second:",f.tell())
    f.write("Noob")
    f.seek(0)

    data2= f.read()
    print("Data after Modification: ",data2)