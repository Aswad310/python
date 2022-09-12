def smart_div(func):
    def inner(x, y):
        if  y==0:
            print("try again! this is Infinity")
            exit()
        else:
            return x/y
    return inner

@smart_div
def div(a, b):
    return a/b

# calling function
print(div(2,0))