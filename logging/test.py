from logger import logging

def add(a,b):
    logging.debug('the add operation is taking place')
    return a + b

logging.debug('the add function is called')
add(2,3)