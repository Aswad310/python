# String to List
def string_to_list(d):
    list= d.split(",")
    print("String to List: ",list)

    # LIST to String
    print("List to String: ", ",".join(list))

# calling function
data= input("Enter comma seprated String: ")

if data == "" or data.isnumeric()==True or data.isspace()==True:
    print("String can't be empty or numeric. . .")
else:
    string_to_list(data)