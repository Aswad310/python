# 1) LIST, to convert it to the Tuple, Set and Dictionary.
def lists(d):
    print("Conversation of LIST: ", d)
    print("to Tuples: ",tuple(d))
    print("to Sets: ",set(d))
    
    mydict= dict()
    for index, values in enumerate(d):
        mydict[index]= values
    print("to Dictionary: ",mydict)

# 2) TUPLE, to convert it to the List, Set and Dictionary.
def tuples(d):
    print("Conversation of Tuple: ", d)
    print("to List: ",list(d))
    print("to Sets: ",set(d))
    
    mydict= dict()
    for index, values in enumerate(d):
        mydict[index]= values
    print("to Dictionary: ",mydict)

# 3) DICTIONARY, to convert it to the Set, List and Tuple.
def dictionary(d):
    print("Conversation of Dictioanry: ", d)

    ## to list
    my_list= list((k, v) for k, v in d.items())
    print("to List",my_list)

    ## to tuple
    my_tuple= tuple((k, v) for k, v in d.items())
    print("to Tuple",my_tuple)

    ## to sets 
    my_sets= set((k, v) for k, v in d.items())
    print("to Sets: ",my_sets)    

# 4) SET, to convert it to the List, Tuple and Dictionary.
def sets(d):
    print("Conversation of sets: ", d)
    print("to List: ",list(d))
    print("to Tuple: ",tuple(d))
    
    mydict= dict()
    for index, values in enumerate(d):
        mydict[index]= values
    print("to Dictionary: ",mydict)


## main
lenght= input("Enter Lenght: ")

if lenght.isnumeric() == False:
    print("Lenght can't be Empty or String!")
    exit()

lenght= int(lenght)
flag= True
# user input LIST
data_list=[]
for i in range(0, lenght):
    data= input("Enter Data: ")
    if data=="" or data.isspace() == True:
        print("Data can't be Empty!")
        flag= False
        break
    else:    
        data_list.append(data)

if flag==False:
    exit()
else:
    # user input TUPLE
    data_tuple=tuple(data_list)

    # user input TUPLE
    data_sets=set(data_list)

    # user input Dictionary
    data_dictionary=dict()
    for k, v in enumerate(data_list):
        data_dictionary[k]= v

    # calling function
    lists(data_list)
    print()
    tuples(data_tuple)
    print()
    dictionary(data_dictionary)
    print()
    sets(data_sets)