from calculator import *
print(dir())
while True:
    user= input("Choose? ")

    if user.isnumeric() == True:
        user = int(user)
        
        if user==1:
            x= input("Enter value A: ")
            y= input("Enter value B: ")
            if x.isnumeric() == True and y.isnumeric() == True:
                x= int(x)
                y= int(y)
                add(x, y)
            else:
                print("Numeric Only!")

        elif user==2:
            x= input("Enter value A: ")
            y= input("Enter value B: ")
            if x.isnumeric() == True and y.isnumeric() == True:
                x= int(x)
                y= int(y)
                sub(x, y)
            else:
                print("Numeric Only!")
            
        elif user==3:
            x= input("Enter value A: ")
            y= input("Enter value B: ")
            if x.isnumeric() == True and y.isnumeric() == True:
                x= int(x)
                y= int(y)
                mul(x, y)
            else:
                print("Numeric Only!")

        elif user==4:
            x= input("Enter value A: ")
            y= input("Enter value B: ")
            if x.isnumeric() == True and y.isnumeric() == True:
                x= int(x)
                y= int(y)
                div(x, y)
            else:
                print("Numeric Only!")

        elif user==5:
            break
        
        else:
            print("try again!")
    
    else:
        print("Please! Enter only Valid Number")