# LIST
l= ["aswad", "ali", "abad", "hassan", "aswad" ,"usama"]

## Accessing LIST using while LOOP
i= 0
while i<len(l):
    # print(l[i])
    i+=1

## Lenght of LIST
# print(len(l))

## Count 
# print(l.count("aswad"))

## Append
l.append("mohsin")
# print(l)

## Insert
l.insert(0, "Basharat")
# print(l)

## extend
x= [658, 313, 890, 131, 998]
y= ["hello", "there", "how", "are", "you"]

# x.extend(y)
# print(x)

y.extend(x)
# print(y)

## remove
l.remove("usama")
# print(l)

## pop
print(l.pop(0))
# print(l)

## reverse
p=[313, 434, 213, 343]
p.reverse()
print(p)

## sort
p.sort()
print(p)