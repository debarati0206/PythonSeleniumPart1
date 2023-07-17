# import logging
#
#
# def test_LoggingDemo():
#     logger = logging.getLogger(__name__) #__name__ is testcase name which is created while creating object using getLogger()
#
#     fileHandler = logging.FileHandler("logfile.log") #write logs details in this file : fileHandler is object
#
#     Formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)")
#     fileHandler.setFormatter(Formatter) #connecting formatter and fileHandler
#     logger.addHandler(fileHandler) # can pass only fileHandler to logger.addHandler
#     logger.setLevel(logging.ERROR)
#     logger.debug("Debug")
#     logger.info("Info")
#     logger.warning("Warning")
#     logger.error("ERROR")
#     logger.critical("CRITICAL")



import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  #filehandler object

    logger.setLevel(logging.CRITICAL)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.debug("A debug statement is executed")
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happend")
    logger.critical("Critical issue")
