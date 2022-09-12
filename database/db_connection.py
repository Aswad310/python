import mysql.connector

############ Database Connection ############  
mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin",
  database="mydatabase"
)

mycursor = mydb.cursor()

############ Create Database ############ 
# mycursor.execute("CREATE DATABASE mydatabase")

############ CREATE Table ############  
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

############ CREATE Primary key on an existing table ############  
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

############ INSERT into Table ############  
# sql= "INSERT INTO customers (name, address) VALUES(%s, %s)"

# val= ("Abad", "Gulshan-e-Ravi")

# val = [ # insert many data
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331')
# ]

# mycursor.execute(sql, val) # insert 1 field 
# mycursor.executemany(sql, val) # inserts many fiels
# mydb.commit() # must required to make the changes

## counts the row inserted
# print(mycursor.rowcount, "record inserted")

## count the last row inserted
# print("1 record inserted, ID:", mycursor.lastrowid)

############ SELECT & WHERE & ORDER BY from Table ############
# mycursor.execute("SELECT *FROM customers")
# mycursor.execute("SELECT name, address FROM customers")
# mycursor.execute("SELECT * FROM customers WHERE id=8")
# mycursor.execute("SELECT * FROM customers WHERE address LIKE '%gre%' ") # WILDCARD
# mycursor.execute("SELECT *FROM customers ORDER BY name")
# mycursor.execute("SELECT *FROM customers ORDER BY name DESC")


# res= mycursor.fetchall() # prints all data
# for r in res:
#     print(r)

# res= mycursor.fetchone() # prints the 1st row
# print(res)


############ DELETE from Table ############
# mycursor.execute("DELETE FROM customers WHERE id= 7")

# mydb.commit()

# print(mycursor.rowcount, "rows deleted")

############ DROP from Table ############
# sql = "DROP TABLE customers"
# sql = "DROP TABLE IF EXISTS customers" # drop only if exists

# mycursor.execute(sql)

############ UPDATE Table ############
# sql= "UPDATE customers SET address= 'Ravi' WHERE id= 1"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) affected")




## check if table exits 
# mycursor.execute("SHOW TABLES")

## prints the available Tables
# for table in mycursor:
#     print(table)
