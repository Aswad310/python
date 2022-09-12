# in , not in 

string1= input("Enter any Sentence: ")
subString= input("Enter Substring from your sentence: ")

for x in string1:
    if subString in x:
        print("Yes find it!", subString)
        break
else:
    print("Given SUBSTRING not available")