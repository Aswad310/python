# create file
f= open("xyz.txt", "w")

print("File Name:", f.name)
print("File Mode:", f.mode)
print("Is file Readable:", f.readable())
print("Is file Writeable:", f.writable())
print("Is file close:", f.closed)

f.close()

print("Is file afte close 2.0:", f.closed)