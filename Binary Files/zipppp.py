# zip
from zipfile import *
f= ZipFile("files.zip", "w", ZIP_DEFLATED)
f.write("aswad.txt")
f.close()

# unzip
from zipfile import *
f= ZipFile("files.zip", 'r', ZIP_STORED)
names=f.namelist()
for name in names:
   print( "File Name: ",name)