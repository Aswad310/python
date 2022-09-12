
def factorial(f):
    if f==0:
        result= 1
    else:
        result= f * factorial(f-1)
    
    return result    

# call function
res= factorial(0)
print(res)