"""Simple module for logging"""

import logging, sys


logger = None
logger_level = None
logger_console_format = None
logger_file_format = None
logger_handler_file = None
logger_handler_console = None


def startup_logger():

    """
    Description
    -----------
    Function to initialize all relevant parameters of the logger: filename, level and message format.

    """

    global logger, logger_handler_file, logger_handler_console, logger_level, logger_console_format, logger_file_format

    # assign to root logger
    logger = logging.getLogger()

    # constants for logger for all handlers
    logger_level = logging.INFO
    logger_console_format = "%(levelname)s - %(message)s"
    logger_file_format = "%(levelname)s - %(asctime)s - %(funcName)s - %(message)s"

    # default level of messages to be displayed at INFO
    logger.setLevel(logger_level)

    # create and add stdout handler
    logger_handler_console = logging.StreamHandler(sys.stdout)
    logger_handler_console.setFormatter(logging.Formatter(logger_console_format))
    logger.addHandler(logger_handler_console)

    # create and add file handler
    logger_handler_file = logging.FileHandler("logs/log_file.log")
    logger_handler_file.setFormatter(logging.Formatter(logger_file_format))
    logger.addHandler(logger_handler_file)


def change_logger(nlevel=logging.INFO, nfileformat="%(levelname)s - %(asctime)s - %(funcName)s - %(message)s", nconsoleformat="%(levelname)s - %(message)s"):

    """
    Description
    -----------
    Function to setup the logger's level and format to one's content. Raises "ValueErrors" for shady parameter-passing...

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

    nfileformat: str
      format for the new messages in file to follow
      default value: %(levelname)s - %(asctime)s - %(funcName)s - %(message)s

    nconsoleformat: str
      format for the new messages in stdout to follow
      default value: %(levelname)s - %(message)s

    """

    global logger, logger_level, logger_file_format, logger_console_format, logger_handler_console, logger_handler_file

    if type(nlevel) is not int:
        get_logger().error(f"Type of supposed nlevel \"{nlevel}\" introduced (\"{type(nlevel)}\") not valid")
        raise ValueError(f"Type of supposed nlevel \"{nlevel}\" introduced (\"{type(nlevel)}\") not valid")

    if nlevel not in [0, 10, 20, 30, 40, 50]:
        get_logger().error(f"Invalid {nlevel} for the logger")
        raise ValueError(f"Invalid {nlevel} for the logger")

    if type(nfileformat) is not str:
        get_logger().error(f"Type of supposed nfileformat \"{nfileformat}\" introduced (\"{type(nfileformat)}\") not valid")
        raise ValueError(f"Type of supposed nfileformat \"{nfileformat}\" introduced (\"{type(nfileformat)}\") not valid")

    if not nfileformat:
        get_logger().error(f"nfileformat \"{nfileformat}\" cannot be empty")
        raise ValueError(f"nfileformat \"{nfileformat}\" cannot be empty")

    if type(nconsoleformat) is not str:
        get_logger().error(f"Type of supposed nconsoleformat \"{nconsoleformat}\" introduced (\"{type(nconsoleformat)}\") not valid")
        raise ValueError(f"Type of supposed nconsoleformat \"{nconsoleformat}\" introduced (\"{type(nconsoleformat)}\") not valid")

    if not nconsoleformat:
        get_logger().error(f"nconsoleformat \"{nconsoleformat}\" cannot be empty")
        raise ValueError(f"nconsoleformat \"{nconsoleformat}\" cannot be empty")

    if logger is None:
        startup_logger()

    if logger_level != nlevel:
        logger_level = nlevel
        logger.setLevel(logger_level)

    if logger_console_format != nconsoleformat:
        logger.removeHandler(logger_handler_console)
        logger_console_format = nconsoleformat
        logger_handler_console = logging.StreamHandler(sys.stdout)
        logger_handler_console.setFormatter(logging.Formatter(logger_console_format))
        logger.addHandler(logger_handler_console)
        logger.info("Console handler changed")

    if logger_file_format != nfileformat:
        logger.removeHandler(logger_handler_file)
        logger_file_format = nfileformat
        logger_handler_file = logging.FileHandler("logs/log_file.log")
        logger_handler_file.setFormatter(logging.Formatter(logger_file_format))
        logger.addHandler(logger_handler_file)
        logger.info("File handler changed")


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
