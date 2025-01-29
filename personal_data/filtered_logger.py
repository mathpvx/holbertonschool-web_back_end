#!/usr/bin/env python3
"""
Filtered Logger module.
"""

import logging
import re
import os
import mysql.connector
from typing import List

# define fields that contain personally identifiable information
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """obfuscates fields in a log message using regex."""
    for f in fields:
        pattern = f"{re.escape(f)}=.*?{re.escape(separator)}"
        message = re.sub(pattern, f"{f}={redaction}{separator}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """custom formatter that redacts sensitive fields in log messages"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """initializes the formatter with fields to redact"""
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """redacts sensitive fields from log messages"""
        record.msg = filter_datum(self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """returns a logger named 'user_data' with a redacting formatter"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False  # prevent logs from propagating to parent loggers

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))  # convert tuple to list

    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """returns a connector to a MySQL database"""
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name
    )


def main() -> None:
    """retrieves user data from the db and logs it with redacted fields"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")  # get all users
    field_names = [desc[0] for desc in cursor.description]  # get column names

    logger = get_logger()

    for row in cursor:
        row_str = "; ".join(f"{field}={value}" for field, value in zip(field_names, row))
        logger.info(row_str)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
