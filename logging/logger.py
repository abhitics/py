import logging 
logging.basicConfig(
    level=logging.INFO,
    force=True,
    format='%(asctime)s - %(levelname)s -%(filename)s - %(lineno)s - %(message)s',
    filename='hello.log',
    filemode='a'
)


    