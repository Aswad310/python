data= ["aswad", "ali", "abad"]

search= input("Enter name: ")

for dis in data:
    if search==dis:
        # data present
        print("Name find!!!")
        break
else:
    # no data
    print("No name find sorry!")