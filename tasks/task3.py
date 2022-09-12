
# function, sum of digits
def sum(n):
	if n == 0:
		return 0
	return(n % 10 + sum(int(n / 10)))

    # Explaination
        # take a number: 123

        # 123 % 10 = 3 + sum(int(123/10= 12))
        # 12 % 10 = 2 +  sum(int(12/10= 1))
        # 1 % 10 = 1 +  sum(int(1/10= 0))
        # 0 program stops

        # returns 

# calling function
while True:
    num = input("Enter Digit: ")

    if num.isnumeric() != True:
    
        print("please! input Numeric only. . .")
    
    else: 
        num= int(num)
        result = sum(num)
        print("Sum of",num,"is", result)