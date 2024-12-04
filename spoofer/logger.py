import logging

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,  # Change to DEBUG for more detailed logs
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("spoofer.log"),  # Log to a file
        logging.StreamHandler()             # Log to the console
    ]
)

def log_message(message: str, level: str = "info"):
    """
    Log a message at the specified level.
    :param message: Message to log
    :param level: Severity level ('info', 'warning', 'error', 'debug')
    """
    if level == "info":
        logging.info(message)
    elif level == "debug":
        logging.debug(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)
