import logging


def log():
    logging.basicConfig(filename="a_generating_logs/Logs/logfile.log", format='%(asctime)s: %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    return logging.getLogger()


logger = log()
logger.info("This is a new log")
logger.error("This is a new log")


