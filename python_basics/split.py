sentence= "Hello there, how are you"
x= sentence.split()

print("Normal Split")
for y in x:
    print(y)

print()

z= sentence.split(",")
print("Comma ',' Split")
for y in z:
    print(y)
