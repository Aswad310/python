import logging

# logging.basicConfig()

## if we want only to print levelname's e.g. debug, info. . .
logging.basicConfig(format='%(levelname)s')

## if we want only to print levelname's and msg too e.g. debug, info. .
logging.basicConfig(format='%(levelname)s:%(message)s')

## show timestamp
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s')

## change timestamp 
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', 
                    datefmt='%d/%m/%Y %I:%M:%S %p')

print("Logging Started")

logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')

print('Logging end')