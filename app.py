from Book_Recommender_System.logger.log import logging

logging.info("Starting the Book Recommender System application...")
from Book_Recommender_System.exception.exception_handler import AppException
import sys

try:
    a = 1 / 0
except Exception as e:
    raise AppException(e, sys)

