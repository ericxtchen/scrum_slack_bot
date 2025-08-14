from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv
import os
import logging

load_dotenv()

try:
    engine = create_engine(os.environ.get("DB_STRING", ""))
except OperationalError as e:
    logging.critical("CANNOT CONNECT TO DATABASE")
    