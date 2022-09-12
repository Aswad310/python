## union
x= {2, 4, 6, 8, 10}
y= [1, 3, 5, 7, 9, 10]

print(x.union(y))

## intersection
print(x.intersection(y)) 

## difference
print(x.difference(y))

## semetric difference
print(x.symmetric_difference(y))

## frozen sets
z= {'a', 'e', 'i', 'o', 'u'}
vowels= frozenset(z)
print(vowels)
