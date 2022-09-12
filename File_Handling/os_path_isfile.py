import os, sys

fname= input("Enter file name: ")

if os.path.isfile(fname):
    print("File exists: ",fname)

    f= open(fname, "r")
    data= f.read()
    print(data)
else:
    print("File don't exists: ",fname)
    sys.exit(0)