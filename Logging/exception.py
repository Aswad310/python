import logging

logging.basicConfig(filename='C:/Users/Aswad/Desktop/softsolutions/Logging/demo.txt', 
                    level=logging.DEBUG, 
                    format='%(asctime)s:%(levelname)s:%(message)s', 
                    datefmt='%d/%m/%Y%I:%M:%S %p')
logging.info("A new Request came")

try:
    x= int(input("Enter Value 1: "))
    y= int(input("Enter Value 2: "))
    print("Result: ", x/y)
except ZeroDivisionError as msg:
    print("Cannot Divide with zero")
    logging.exception(msg)
except ValueError as msg:
    print("Please provide int value only")
    logging.exception(msg)

print("Request Processing Completed")