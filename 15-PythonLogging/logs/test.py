from logger import logging
def add(a,b):
    logging.debug("The addition operation is taking place")
    return a + b
add(10,15)
logging.debug("The additon function run")
