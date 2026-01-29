import logging

logging.basicConfig(
     level=logging.DEBUG,
                    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[
                        logging.FileHandler("app1.log"),
                        logging.StreamHandler()

                    ]
                )

logger = logging.getLogger('arthimetic logs')

def add(a,b):
    res = a+b
    logger.debug(f"the sum of {a} and {b} are {res}")
    return res
def sub(a,b):
    res = a-b
    logger.debug(f"the diffrence of {a} and {b} are {res}")
    return res
def mul(a,b):
    res = a*b
    logger.debug(f"the sum of {a} and {b} are {res}")
    return res
def div(a,b):
    try:
        res = a/b
        logger.debug(f"the sum of {a} and {b} are {res}")
        return res
    except ZeroDivisionError:
        logger.error("division by zero error")
        return None
    
add(4,5)
sub(8,5)
mul(8,4)
div(10,0)




    