while True:
    # takes a string from the user
    string= input("Enter String: ")

    if string.isalpha() == True:

        # gets the lenght of the String
        lenght= len(string)

        # SO, what I do is that sort() function only sort the lists so I break the 
        # given string in the list by getting string INDEX 
        list= [string[i] for i in range(0, lenght)]
        print(list) # prints the List for better understanding

        ## Accending Order
        list.sort() # sort() function sort the list then. . .

        print("Sorted String ( Asending Order ) : ", end="")

        for i in list: # . . .then list is thrown in 'i' & prints them one by one
            print( i , end="") # end="" is used to print next char in current line

        print() # prints the blank line

        ## Decending Order
        list.sort(reverse=True) # just Reverse the sort list 

        print("Sorted String ( Desending Order ) : ", end="")

        for j in list:
            print( j , end="")

        print() # prints the blank line

        print("String Lenght: " + str(lenght)) # prints the lenght of the given String

    else:
        print("Please! enter only String!")