import inspect
import logging

class BaseClass:
    def getLogger(self):
        loggername = inspect.stack()[1][3] # Gets the name of the class / method from where this method is called i.e. test_editProfile in test_fixturesData.py
        logger = logging.getLogger(loggername)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  #filehandler object

        logger.setLevel(logging.INFO)
        return  logger

