import os

# getcwd() -> returns the address of your currently working directory 
cwd= os.getcwd()
print("Current Working Directory is", cwd)

# mkdir() -> creates the new folder in currently working directory
os.mkdir("testing")
print("New folder created")

# mkdir() -> creates the new folder in currently working directory
os.makedirs("sub1/sub2/sub3")
print("Multiple New folder created")

# rmdir() -> removes the diven directory
os.rmdir("sub1/sub2/sub3")
print("sub1 deleted!")

# removedirs() -> remove all directories
os.removedirs("sub1/sub2")