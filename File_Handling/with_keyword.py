with open("aswad.txt", "w") as f:
    f.write("My name is Aswad\nMy brother name is Abad Ali.")

with open("aswad.txt", "r") as f:
    data= f.read()
    print(data)