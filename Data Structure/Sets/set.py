## Sets
s= {40, 21, 433, 12, 321}
x= {"aswad", "ali"}
print(s)

## add
s.add(80)
print(s)

## Update
s.update(x)
print(s)

## copy
s1= s.copy()
print(s1)

## pop
print(s.pop())

## remove (GIVES ERROR IF VALUES NOT PRESENT)
y={1,3,4,2}
y.remove(1)
print(y)

## discard (DIDN'T GIVE ERROR IF VALUES NOT PRESENT)
y.discard(123)
print(y)

## clear
y.clear()
print(y)