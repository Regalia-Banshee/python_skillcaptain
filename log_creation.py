import logging
import time
log_format= "%(levelname)s %(asctime)s-%(message)s"
logging.basicConfig(filename='D:\\execution.log',level=logging.DEBUG,format=log_format)

print('Available level names are DEBUG,INFO,WARNING,ERROR,CRITICAL')

level_name=input("Enter level name:" )
message=input('Enter message to log: ')

available_levels={'DEBUG':logging.DEBUG, 'INFO':logging.INFO,'WARNING':logging.WARNING,'ERROR':logging.ERROR,'CRITICAL':logging.CRITICAL}

if level_name not in available_levels:
    print("Invalid input!!, Try again and use the given level names!!")
    exit()
level = available_levels[level_name]

logging.log(level, message)




