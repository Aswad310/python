## Positional Arguments
def student(id, name):
    print("Your ID is ", id, " & name is ", name)


# calling Function
# student(193329, "Aswad Ali") # valid 
# student(193329) # InValid 

## Keyword arguments
def student(id, name):
    print("Your ID is",id,"& name is",name)


# calling Function
# student(id= 193329, name="Aswad Ali")
# student(id= 193330, name="Abad Ali")
# student(name="Muzaza Ali", id= 193331)

## Default Arguments
def student(id, name= "Aswad"):
    print("Your ID is",id,"& name is",name)


# calling Function
# student(id= 193330, name="Abad") # valid 


## Variable Length Arguments
def person(id, *data):
    print(id)
    print(*data)

# calling Function
# person(1, "Jhon Doe", "Gulshan Ravi", 1233432)

###
def add(*value):
    sum=0
    for i in value:
        sum+=i
    print(sum)

# calling function
# add(4, 2, 3)

## keyword variable length argument
def cart(**data):
    print(data)

# calling function
# cart(id=1, item="Soap", price="179")

###
def cart2(**data):
    for i, j in data.items():
        print(i,":",j )

# calling function
cart2(id=1, item="Soap", price="179")