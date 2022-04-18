# enter number of members
from asyncio.windows_events import NULL

# user input total No. of members
members= int(input("Enter No. of Members: "))

# declare array variables
first_name= [None] * (members)  # None is null object (used for string only) which is multiply by no. of members
last_name= [None] * (members)   #[None] * (members)  => assigning size of array
name= [None] * (members) 
vol_status= [0] * (members)    # here we use '0' instead of None because None is used with string specfic arrays/variables and the multiply by no. of members
area_status= [0] * (members) 
date_of_joining= [0] * (members) 
fee_paid_status= [0] * (members) 
charges= [0] * (members) 
sponsor_name= [None] * (members)  
sponser_status= [0] * (members)
short_msg= [None] * (members) 


# Task 1

# while loop runs untill i < members
i=0
while(i<members):
    print("\nMember No. " + str(i+1))
    first_name[i]= input("Enter your First Name: ")
    last_name[i]= input("Enter your Last Name: ")

    name[i]= first_name[i] + " " + last_name[i]

    # Menu to become a Volunteer
    print("\n Do you want to become a volunteer \n")
    print("Press 1. To become a volunteer \n")
    print("Press 2. Not want to become a volunteer \n")
    volunteerChoice= int(input("Enter your choice: "))

    # if member selected '1' to become a volunteer. . .
    if (volunteerChoice==1):

        vol_status[i]= 1 # . . . then insert '1' to vol_status[i] array

        # Menu of seleted pier entrance gate
        print("\n Where would you like to work: \n")
        print("Press 1: the pier entrance gate \n")
        print("Press 2: the gift shop \n")
        print("Press 3: painting and decorating \n")
        areaChoice= int(input("Enter your choice: "))

        if(areaChoice==1):
            print(name[i]+ " " +"selected - pier entrance gate")
            area_status[i]= 1  # insert '1' to area_status[i] array 
        elif(areaChoice==2):
            print(name[i]+ " " +"selected - the gift shop")
            area_status[i]= 2  # insert '2' to area_status[i] array
        elif(areaChoice==3):
            print(name[i]+ " " +"selected - painting and decorating")
            area_status[i]= 3  # insert '3' to area_status[i] array
        else:
            print("Wrong Choice!!!")
            area_status[i]= 0 # insert '0' to area_status[i] array 'if Choice was Wrong!!!'

        # date of joning
        date_of_joining[i]= input("\nEnter your date of joining: ")

        # Menu to pay 75$ Membership
        print("\nWant to pay 75$ or not ? \n")
        print("Press 1: to Yes")
        print("Press 2: to No")
        feechoice= int(input("Enter your choice: "))

        if(feechoice==1):
            #fee paid
            fee_paid_status[i]= 1  # insert '1' to fee_paid_status[i] array
            print("Thanks!!! For your 75$ Membership")

            # sum of charges to check the total charges at the end
            charges[i]= charges[i] + 75
        else:
            #add 0 to fee array
            fee_paid_status[i]= 0

# Task 3 
# sponsered Additional part to Task 1 

        # Menu for Sponsered 
        print("\nWant to Sponsor Seaview Pier")  
        print("Press 1: to Yes") 
        print("Press 2: to No")
        sponserChoice= int(input("Enter choice: "))

        if(sponserChoice==1):
            #sponser status
            sponser_status[i]= 1 # insert '1' to sponser_status[i] array
            #store individual name of people who sponsor
            print("Thanks! "+ name[i] +" for sponsering Wooden Plan for 200$")
            sponsor_name[i]= name[i] 
            #short message  
            short_msg[i]= input("Enter a Short Message: ")
            #charge
            charges[i]= charges[i] + 200
        elif(sponserChoice==2):
            sponser_status[i]= 0
            print("No Problem!, It would be good to sponsor next time ") 
        else:
            sponser_status[i]= 0
            print("Wrong Choice!!!")

    elif(volunteerChoice==2):
        vol_status[i]= 0
        print ("Thank you!!!, comeback soon")
    else:
        vol_status[i]=0
        print("Wrong Choice!!!")     
    i+=1

# Task 2 
# Using the Membership Data

while True: 
    print("+--------------------------------------------------------------------------------------+")
    print("|------------------------------Search Volunteers Information---------------------------|")
    print("+--------------------------------------------------------------------------------------+")
    print("|    1: Members who have chosen to work as volunteers.                                 |")                                 
    print("|    2: Volunteers who would like to work at the pier entrance gate.                   |")
    print("|    3: Volunteers who would like to work in the gift shop.                            |")
    print("|    4: Volunteers who would like to help with painting and decorating tasks.          |")
    print("|    5: Members whose membership has expired (they have not re-joined this year).      |")
    print("|    6: Members who have not yet paid their $75 fee.                                   |")
    print("|    7: Members who sponsor for Wooden Planks of 200$                                  |")
    print("|    8: Exit                                                                           |")
    print("+--------------------------------------------------------------------------------------+")

    search = int(input("Enter Choice: "))
    if (search==1):
            print("Members who have chosen to work as volunteers::")
            i = 0
            while (i < len(vol_status)) :
                if (vol_status[i] == 1) :
                    print(str(i + 1) + " : " + name[i])
                i += 1
    elif(search==2):
                print("Volunteers who would like to work at the pier entrance gate::")
                i = 0
                while (i < len(vol_status)) :
                    if (area_status[i] == 1) :
                        print(str(i + 1) + " : " + name[i])
                    i += 1
    elif(search==3):
                print("Volunteers who would like to work in the gift shop::")
                i = 0
                while (i < len(vol_status)) :
                    if (area_status[i] == 2) :
                        print(str(i + 1) + " : " + name[i])
                    i += 1
    elif(search==4):
                print("Volunteers who would like to help with painting and decorating tasks::")
                i = 0
                while (i < len(vol_status)) :
                    if (area_status[i] == 3) :
                        print(str(i + 1) + " : " + name[i])
                    i += 1
    elif(search==5):
                print("Members whose membership has expired (they have not re-joined this year::")
                i = 0
                while (i < len(vol_status)) :
                    if (vol_status[i] == 0) :
                        print(str(i + 1) + " : " + name[i])
                    i += 1
    elif(search==6):
                print("Members who have not yet paid their $75 fee::")
                i = 0
                while (i < len(vol_status)) :
                    if (fee_paid_status[i] == 0) :
                        print(str(i + 1) + " : " + name[i])
                    i += 1
    elif(search==7):
                print("Members who sponsor for Wooden Planks of 200$")
                i = 0
                while (i < len(vol_status)) :
                    if (sponser_status[i] == 1) :
                        print(str(i + 1) + " : " + sponsor_name[i] + " >  " + short_msg[i])
                    i += 1
    elif(search==8):
        break
    
    else:
                print("Not a valid search choice")
                