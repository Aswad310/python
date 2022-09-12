## Lambda 
from cProfile import label
from functools import reduce


mul = lambda x, y : x * y
# print("Muliplication:",mul(3, 3))

## filter()
data= [31, 44, 51, 242, 122, 13]
x= list(filter(lambda x : x % 2 !=0 , data))
print("Filter:" , x)

## map()
y= list(map(lambda x : x * x, x))
print("Maping:" , y)

## reduce()
z= reduce(lambda x,y : x + y, y)
print("Reduce:", z)