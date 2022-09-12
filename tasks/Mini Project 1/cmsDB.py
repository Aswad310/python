from asyncio.windows_events import NULL
from audioop import add
import mysql.connector

############ Database Connection ############
try:
  contact = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin",
    database="contact"
  )
  print("Successfully Connected to Database!")
except Exception as e:
  print("Error! Connectiing to Database",e)
  
mycursor = contact.cursor()
  
############ Create Database ############ 
# mycursor.execute("CREATE DATABASE contact")
# print("Database Created!")

############ CREATE Table ############  
# mycursor.execute("CREATE TABLE diary (name VARCHAR(255), phone INT(11) PRIMARY KEY)")
# print("Table Created!")

# mycursor.execute("ALTER TABLE diary MODIFY COLUMN phone VARCHAR(14)")
# contact.commit()
# print("Changes had been made!")

############ INSERT ############  
def insert():
  try:
    addflag = True
    name = input("Enter Name :")
    mobile_no = input("Enter Mobile_no :")
      
    # lenght of mobile_no
    if len(mobile_no) != 11:
      print("Error! Phone Number Lenght must be 11 & Numeric!")
    else:
      query = "INSERT INTO diary (name, phone) VALUES(%s, %s)"
      val = (name, mobile_no)
      mycursor.execute(query, val) # insert 1 field
      contact.commit()
      print("Successfully Phone Number Inserted!")   
  except Exception as e:
    print("Something went wrong!",e)

############ SELECT ############  
def select():
  query= "SELECT * FROM diary" 
  mycursor.execute(query)
  res = mycursor.fetchall() # prints all data
    
  if not res:
    # if data is empty
    print("Contact Diary is Empty!")
  else:
    for data in res:
      print("\tName:",data[0])
      print("\tMobile No:",data[1])
      print("")

############ SEARCH ############  
def search():
  print("\t[1] Search by Name\n\t[2] Search by Phone No.\n\t[3] Back\n\t[0] Exit") 
    
  try:
    choice = int(input("\tEnter Choice: "))
  except Exception as e:
    print("That is not true.",e)
  finally:
      print("")
    
  # SEARCH by Name
  if choice == 1:
    try:
      name = input("Enter Name you want to Search: ")
    except Exception as e:
      print("That is not true.",e)
    finally:
      print("")
        
    query = "SELECT * FROM diary WHERE name = %s"
    val= (name,)
    mycursor.execute(query, val)
      
    res = mycursor.fetchall() # prints all data
    
    if not res:
      # if data is empty
      print("Contact Diary is Empty!")
    else:
      for data in res:
        print("\tName:",data[0])
        print("\tMobile No:",data[1])
        print("")
    
  # SEARCH by Phone
  elif choice == 2:
    try:
      phone = int(input("Enter Phone No. you want to Search: "))
    except Exception as e:
      print("That is not true.",e)
    finally:
      print("")
        
    query = "SELECT * FROM diary WHERE phone = %s"
    val= (phone,)
    mycursor.execute(query, val)
      
    res = mycursor.fetchall() # prints all data
    
    if not res:
      # if data is empty
      print("Not found!")
    else:
      for data in res:
        print("\tName:",data[0])
        print("\tMobile No:",data[1])
        print("")
  elif choice == 3:
    pass   
  elif choice == 0:
    quit()
  else:
    print("Invalid Choice") 

############ UPDATE ############  
def update():
  addflag= True
  try:
    phone = int(input("Enter Phone No. you want to Update: "))
  except Exception as e:
    print("That is not true.",e)
  finally:
    print("")
        
  query1 = "SELECT * FROM diary WHERE phone = %s"
  val= (phone,)
  mycursor.execute(query1, val)
      
  res = mycursor.fetchall() # prints all data
    
  if not res:
    # if data is empty
    print("Data not found!")
    addflag= False
  else:
    for data in res:
      print("\tPresent Name:",data[0])
      print("\tPresent Mobile No:",data[1])
      print("") 
    
  if addflag == True:
    try:
      print("[1] Edit Name\n[2] Edit Phone No.\n[3] Edit Both\n[4] Back\n[0] Exit")
      choice = int(input("Enter Choice: "))
    except Exception as e:
      print("This is not true.",e)
    finally:
      print("")
      
    # edit name
    if choice == 1:
      try:
        name2= input("Enter new Name: ")   
        query2 = "UPDATE diary SET name = %s WHERE phone = %s"
        val = (name2, phone)
          
        mycursor.execute(query2, val)
        contact.commit()
          
        print("Name Updated")
          
      except Exception as e:
        print("This is not true.",e)
      finally:
        print("")
          
    # edit phone
    elif choice == 2:
      try:
        phone2= input("Enter new Phone No.: ") 
          
        # lenght of phone2
        if len(phone2) != 11:
          print("Error! Phone No. Lenght must be 11 OR\nMust be Numeric!")
          addflag= False
          
        if addflag == True:
          query2 = "UPDATE diary SET phone = %s WHERE phone = %s"
          val = (phone2, phone)
            
          mycursor.execute(query2, val)
          contact.commit()
            
          print("Phone No. Updated")
          
      except Exception as e:
        print("This is not true.",e)
      finally:
        print("")
      
    elif choice == 3:
      addflag= True
      try:
        name2 = input("Enter new Name: ")
        phone2= input("Enter new Phone No.: ") 
          
        # lenght of phone2
        if len(phone2) != 11:
          print("Error! Phone No. Lenght must be 11 OR\nMust be Numeric!")
          addflag= False
          
        if addflag == True:
          query2 = "UPDATE diary SET name = %s, phone = %s WHERE phone = %s"
          val = (name2, phone2, phone)
            
          mycursor.execute(query2, val)
          contact.commit()
            
          print("Name and Phone No. Updated")
          
      except Exception as e:
        print("This is not true.",e)
      finally:
        print("")
      
    elif choice == 4:
      pass
      
    elif choice == 0:
      quit()
          
    else:
      print("Invalid Choice")

############ DELETE ############  
def delete():
  try:
    name = input("Enter Name you want to Delete: ")
  except Exception as e:
    print("That is not true.",e)
  finally:
    print("")
        
  query = "DELETE FROM diary WHERE name = %s"
  val= (name,)
  mycursor.execute(query, val)
  contact.commit()

  print(mycursor.rowcount, "rows deleted") 
      
#main
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
    choice = None
    choice = int(input("\tEnter the choice: "))
  except Exception as e:
    print("That is not true.",e)
  finally:
    print("")
  
  if choice == 1:
    insert()
  elif choice == 2:
    select()
  elif choice == 3:
    search()
  elif choice == 4:
    update()
  elif choice == 5:
    delete()
  elif choice == 0:
    quit()     
  else:
    print("Invalid Choice! Try again")