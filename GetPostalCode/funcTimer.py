from time import time
from logger import logging

def funcTimer(func):
    def f(*args, **kwargs):
        start = time()
        logging.info(f'Function: {func} >>>>>> START')
        res = func(*args, **kwargs)
        end = time()
        logging.info(f'Function: {func} >> DONE!! >> Elapsed Time: {(end - start):.3f} secs')
        logging.info(f'')
        return res
    return f

if __name__ == '__main__':
    pass