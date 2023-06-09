import logging
import time
from sys import stdout
from src import path_to_logs

class Logger:

    def __init__(self, logger, loggerlevel="INFO"):
        # create a logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(loggerlevel)
        self.datetime = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime())
        # Disable logging for imported modules
        logging.getLogger("urllib3.connectionpool").setLevel(logging.WARNING)
        
        th = logging.StreamHandler(stdout)
        th.setLevel(logging.DEBUG)
        
        fh = logging.FileHandler(f'{path_to_logs}/python-mailparser_{self.datetime}.log')
        fh.setLevel(logging.DEBUG)

        # create a formatter and set the formatter for the handler.
        fileformatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(message)s')
        fh.setFormatter(fileformatter)

        textformatter = logging.Formatter('%(message)s')
        th.setFormatter(textformatter)
        
        # add the Handler to the logger
        self.logger.addHandler(fh)
        self.logger.addHandler(th)

    def getlog(self):
        return self.logger