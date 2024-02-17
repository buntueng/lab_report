import logging
import os

logging_file_name = 'debugging.log'
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
if not os.path.exists(logging_file_name):
    open(logging_file_name, 'w').close()

log_file_handler = logging.FileHandler(logging_file_name)
log_file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_file_handler.setFormatter(formatter)
logger.addHandler(log_file_handler)
