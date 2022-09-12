import logging

logging.basicConfig(filename='C:/Users/Aswad/Desktop/softsolutions/Logging/sample2_logging.txt', 
                    level=logging.DEBUG)

print("Logging Started")

logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')


print('Logging end')