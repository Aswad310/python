candymachine= 5 # capacity is 5

customers= int(input("Enter number of user: "))

for x in range(customers):
    
    if customers >= candymachine:
        print("out of stock!")
        break

    print("Candy Given")

print("Bye")