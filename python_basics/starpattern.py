# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
rows= range(1, 6)
for x in rows:
    for y in range(x):
        print('* ', end=" ") # end is used to Print the next line in current line
    print() # prints the new line 

print()
# *  *  *  *  *  
# *  *  *  *
# *  *  *
# *  *
# *
rows= range(1, 6)
for x in rows:
    for y in range(6-x):
        print("* ", end=" ")
    print()