import mysql.connector
from config.config import *
from utils.logger import logging


def get_connection():

    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

        logging.info("Connected to MySQL database.")

        return connection

    except mysql.connector.Error as err:

        logging.error(f"MySQL Error: {err}")

        print(f"MySQL Error: {err}")

        return None