def squares():
    x= 1
    while x<=10:
        yield x * x
        x+=1

# calling function

for i in squares():
    print(i)