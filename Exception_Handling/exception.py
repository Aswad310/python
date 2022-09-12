try:
    a= int(input("Enter value1: "))
    b= int(input("Enter value2: "))
    print(a/b)
except( ZeroDivisionError, ValueError )as e:
    print("Please enter valid number only", e)
     