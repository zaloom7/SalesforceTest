import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C:\\selenium browser drivers\\logs\\automation.txt", filemode='a', format= '%(asctime)s: %(levelname)s: %(message)s' , datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
