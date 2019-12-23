import inspect
import logging


class BaseClass:
    def getLogs(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        file_Handler = logging.FileHandler('logfile.log')
        file_Formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_Handler.setFormatter(file_Formatter)
        logger.addHandler(file_Handler)  # file_handler => file location
        logger.setLevel(logging.DEBUG)
        return logger

