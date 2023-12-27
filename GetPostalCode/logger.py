import logging, os, sys
from datetime import datetime

CURRENTDATETIME = datetime.now().strftime('%Y%m%d%H%M%S')
LOGS_FOLDER = './GENERATED_LOGS/'
LOGS_FILE = LOGS_FOLDER + 'LOGS_' + CURRENTDATETIME + '.log'


if not os.path.isdir(LOGS_FOLDER):
    os.mkdir(LOGS_FOLDER)
    print('Created new logs folder: {}'.format(LOGS_FOLDER))
    
else:
    print('Found log files folder.')    
    
    
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s ^ %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(LOGS_FILE),
        logging.StreamHandler()
    ]
)


    
def exit_log(msg : str):
    logging.info(msg)
    input('Press [Enter] key to exit..')
    sys.exit()
    
    
if __name__ == '__main__':
    pass