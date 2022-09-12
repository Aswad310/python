# open file
f= open("list.txt", "w")

# write LIST data
list= ["Aswad\n", "Abad\n", "Ahmer\n", "Hassan"]
f.writelines(list)

#close file
f.close()