# open file
f= open("welcome.txt", "r")

# read file
data= f.read() # read - all
data= f.read(9) # read(n)
line1= f.readline() # read line1 by line
line2= f.readline() # read line2 by line

# 'readlines' using FOR loop
data= f.readlines()
for d in data:
    print(d)

print(line1, end="")
print(line2, end="")

# close file
f.close()