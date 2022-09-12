import os, sys

fname= input("Enter file name: ")

if os.path.isfile(fname):
    print("File exists: ",fname)
    f= open(fname, "r")
else:
    print("File don't exists: ",fname)
    sys.exit(0)

lcount=wcount=ccount=0

for line in f:
    lcount= lcount + 1
    ccount= ccount + len(line)
    word= line.split()
    wcount= wcount + len(word)

print("Total Lines", lcount)
print("Total Words", wcount)
print("Total Characters", ccount)