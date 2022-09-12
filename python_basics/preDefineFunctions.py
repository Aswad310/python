## strip
#  rstrip
#  lstrip
name= "    Hello "
print("Lenght before strip: ", len(name))

x= name.lstrip()

print("Lenght after strip: ", len(x))

# find
# index
name2= "My name is Aswad!"
print(name2.find("s"))
print(name2.index("name"))

# count
name3= "I love pakistan, Python"
print("count: " , name3.count("Python"))