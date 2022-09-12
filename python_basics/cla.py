# Command line arguments

from sys import argv
first_name = argv[1]
last_name=argv[2]
print("First name is: ", first_name)
print("Last name is: ", last_name)
print("Type of first name is", type(first_name))
print("Type of last name is", type(last_name))