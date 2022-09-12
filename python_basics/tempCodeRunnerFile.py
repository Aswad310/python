rows= range(1, 6)
for x in rows:
    for y in range(x+1):
        print('*', end=" ") # end is used to Print the next line in current line
    print() # prints the new line 