
import logging


def test_logsDemo():
    logger = logging.getLogger(__name__)

    file_Handler = logging.FileHandler('logfile.log')
    file_Formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

    file_Handler.setFormatter(file_Formatter)
    logger.addHandler(file_Handler)  # file_handler => file location

    logger.setLevel(logging.DEBUG)  # To set level where logs will start from below levels

    logger.debug("A debug statement is executed")
    logger.info("Info statement")
    logger.warning("Warning")
    logger.error("Major error")
    logger.critical("Critical error")
    logger.exception("IOException")

