import logging

logging.basicConfig(

filename='shaheer.log',
filemode='w',
level = logging.DEBUG ,
format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
datefmt='%Y-%m-%d %H:%M:%S'
)


# Log messages with different severity levels

logging.debug("This is a debug message")
logging.info('This is a info message')
logging.warning("This is a warning message")
logging.error('This is a error message')
logging.critical('THis is a critical message')
logging.critical('THis is a critical message.....')