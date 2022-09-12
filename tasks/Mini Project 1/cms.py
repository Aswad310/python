import os

# variables used anywhere in program
global data, main_data

# file name
filename = "C:/Users/Aswad/Desktop/softsolutions/tasks/Mini Project 1/contact.csv"


with open(filename, 'r') as f:
    main_data = f.read()
    main_data = main_data.split('\n')
    main_data = (list(filter(None, main_data)))

# Contact System Class
class contact_system():
    # constructor
    def __init__(self, name='', moile_no=0):
        self.name = name
        self.moile_no = moile_no

    # write file class
    def write_file(self, list_data):
        f = open(filename, "w")
        all_data = str()

        for data in list_data:
            all_data += data+'\n'

        f.write(all_data)
        f.close()
        return True

    # display contact
    def show_contact(self):
        if os.stat(filename).st_size == 0:
            print('Contact Diary is Empty!')
        else:
            with open(filename, 'r') as f:
                data = f.read()
                split_data = data.split(',')
                print("Name :",split_data[0])
                print("Name :",split_data[1])
    # add contact
    def add_contact(self):

        for data in main_data:
            split_data= data.split(',')

        addflag = True
        try:
            name = input("Enter Name :")
            mobile_no = input("Enter Mobile_no :")
        except Exception as e:
            print("That is not true.", e)
            addflag= False
        finally:
            print("")

        # mobile number lenght
        if len(mobile_no) != 11 or mobile_no.isnumeric() == False:
            print("Phone Number must be 11 Digit OR \nMust be Numeric")
            addflag= False

        if addflag == True:
            for data in main_data:
                split_data= data.split(',')
                if mobile_no == split_data[1]:
                        print(split_data)
                        print("Mobile No. already exist try again!")
                        addflag= False
                        break
        if addflag == True:
            data = name+','+mobile_no+','+'\n'

            f = open(filename, "a")
            f.write(data)
            f.close()

            print("Contact Added Succeffully")

    # search
    def search(self, choice):
        addflag = True
        if choice == 1:
            try:
                name= input("Enter Name you want to Search: ")
            except Exception as e:
                print("That is not true.", e)
                addflag= False
            finally:
                print("")

            if addflag == True:
                for data in main_data:
                    split_data = data.split(',')
                    if name == split_data[0]:
                        print("Name :", split_data[0])
                        print("Mobile_no :", split_data[1])
                        addflag = False
                    # else:
                    #     print("Wrong Name")
                if addflag == True:
                    print("No search data available")

        elif choice == 2:
            try:
                phone = input("Enter Phone Number you want to Search: ")
            except Exception as e:
                print("That is not true.", e)
                addflag = False
            finally:
                print("")

            if addflag == True:
                # phone= str(phone)
                for data in main_data:
                    split_data = data.split(',')
                    if str(phone) == split_data[1]:
                        print("Name :", split_data[0])
                        print("Mobile_no :", split_data[1])
                        addflag = False
                if addflag == True:
                    print("No search data available")

        elif choice == 3:
            quit()
        else:
            print("Invalid Choice")

    # update contact
    def edit_contact(self, no):
        addflag= True
        print("Old Mobile #:", no)

        for data in main_data:
            split_data = data.split(',')

            if(no == split_data[1]):
                print(split_data)
                print("")

                new_mobileNo = input("Enter New Mobile # :")

                if len(new_mobileNo) != 11 or new_mobileNo.isnumeric() == False:
                    print("Phone No. contains 11 Digit OR \nMust be Numeric")
                    addflag = False

                if addflag == True:
                    for data2 in main_data:
                        split_data2 = data2.split(',')
                        if new_mobileNo == split_data2[1]:
                            print("Sorry This Number already exist!")
                            addflag= False

                    if addflag == True:
                        # moile_no = input("Enter Mobile_no :")
                        new_value = split_data[0]+','+str(new_mobileNo)

                        main_data[main_data.index(data)] = new_value
                        self.write_file(main_data)
                        print("Successfully Updated")
                        return True
        print("Try Again!!")

    # remove contact 
    def remove_contact(self, nam):
        cnt = 0
        for data in main_data:
            split_data = data.split(',')

            if nam == split_data[0]:
                print(nam)
                # print(main_data)

        if (self.write_file(main_data)):
            print("Successfully Deleted !")
        else:
            print("Try Again!! ")

    # search name
    def search_name(self, no):
        for data in main_data:
            split_data = data.split(',')
            if no == split_data[0]:
                return True
        return False
    # search phone#
    def search_phone(self, no):
        for data in main_data:
            split_data = data.split(',')
            if no == split_data[1]:
                return True
        return False

my_class = contact_system()
while True:
        print('\n'
              """ **** Welcome To Contact Management System ****
                
                MAIN MENU
        =========================
        [1] Add a new Contact
        [2] List all Contacts
        [3] Search for contact
        [4] Edit a Contact
        [5] Delete a Contact
        [0] Exit
        ================== """)

        try:
            user_input= None
            user_input = int(input("\tEnter the choice: "))
        except Exception as e:
            print("That is not true.", e)
        finally:
            print("")

        if user_input == 1:
            my_class.add_contact()

        elif user_input == 2:
            my_class.show_contact()

        elif user_input == 3:
            addflag= True
            print("\t[1] Search by Name\n\t[2] Search by Phone No.\n\t[3] Exit")
            try:
                choice= int(input("Enter Search Choice: "))
            except Exception as e:
                print("Choice is not correct")
                addflag= False
            finally:
                print("")
            if addflag == True:
                my_class.search(choice)

        elif user_input == 4:
            addflag= True
            try:
                mobile_No = input("Enter Phone# for edit :")
            except Exception as e:
                print("Please enter Valid Value")
                addflag= False
            finally:
                print("")

            if addflag == True:
                if my_class.search_phone(mobile_No):
                    my_class.edit_contact(mobile_No)
                else:
                    print("Incorrect Mobile No!!")

        elif user_input == 5:
            name = input("Enter User Name for delete :")

            if my_class.search_name(name):
                my_class.remove_contact(name)
            else:
                print("Incorrect User Name!!")

        elif user_input == 0:
            print("Thankyou for Using Our Contact Management System")
            quit()

        else:
            print("Invalid Input!!")