#from logger import logging
from logger2 import logging
def calculator(a,b):
    logging.info("Parameter received!")
    try:
        if a<b:
            logging.warning("a is less than b")
        else:
            res=a/b
            logging.info(f'result is {res}')
            return res
    except Exception as e:
        logging.error(f"Error {e} occured ")

calculator(10,2) 