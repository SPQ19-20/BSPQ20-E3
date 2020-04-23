"""Simple module for logging"""

import logging, sys


logger = None
logger_handler = None
logger_level = None
log_format = None


def startup_logger():

    """
    Description
    -----------
    Function to initialize all relevant parameters of the logger: filename, level and message format.

    """

    global logger, log_format

    log_format = "%(levelname)s - %(asctime)s - %(funcName)s - %(message)s"

    # setup logger AND allow it to print to console if needed
    logging.basicConfig(
        filename = f"logs/log_file.log",
        level = logging.INFO,
        format = log_format
    )
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

    # assign root logger
    logger = logging.getLogger()

def change_logger(nlevel=logging.INFO, nformat="%(levelname)s - %(asctime)s - %(funcName)s - %(message)s"):

    """
    Description
    -----------
    Function to setup the logger's level and format to one's content.

    Attributes
    ----------
    nlevel: logging.{LEVEL}, any integer in [0, 10, 20, 30, 40, 50]

      Level         Numeric value
      -----------------------------
      CRITICAL      50
      ERROR         40
      WARNING       30
      INFO          20
      DEBUG         10
      NOTSET        0

      default value: logging.INFO

    nformat: str
      format for the new messages to follow
      default value: %(levelname)s - %(asctime)s - %(funcName)s - %(message)s

    """

    global logger, log_format

    log_format = nformat

    if logger is None:
        startup_logger()

    # logger_handler = logging.StreamHandler()
    # logger.addHandler(logger_handler)

    # # First, generic formatter:
    # logger_handler.setFormatter(logging.Formatter('%(message)s'))

    logger.setLevel(nlevel)


def get_logger():

    """
    Description
    -----------
    Simple function to use same logger across project (singleton pattern...)

    Available funtions to be used with this method include:

      - .debug(message) - default logger level is INFO, will not show unless default logger level is changed
      - .info(message)
      - .warning(message)
      - .error(message)
      - .critical(message)

    """

    global logger

    if logger is None:
        startup_logger()

    return logger
