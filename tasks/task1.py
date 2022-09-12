while True:
    # takes a number from the user and then convert into the int datatype
    num= input("Enter Number: ")

    if num.isnumeric() == True:
        
        num2= int(num)
        # sets the sum to the '0' 
        sum= 0

        # starts the Interation from the 12
        i=12
        while i>=0: # condition remains true if 'i' is greater than or equal to the '0'
            # 'num' is user input and multiplies by the Iteration & assign to the 'ans' 
            # e.g. 2 * 12 = 24. . . 2 * 11 =22
            ans= num2 * i 
            # print the answer in the form ' 2 * 12 = 24. . . untill condition remains true'           
            print(str(num2) + "*" + str(i) + "=" + str(ans))
            # at every Iteration ans is added to the sum e.g sum= 0+24, sum= 24+22. . .
            sum= sum+ans
            i-=1 # Iteration is decermented by '1' untill condition remains true

        print() # prints the next line

        print("Sum of All Results: " + str(sum)) # prints the sum

        # str() is used to convert integer to the string so then we concatenate the 'string' with the int after
        # converting it in to the (string)

    else:
        print("Please! enter only Integer!")