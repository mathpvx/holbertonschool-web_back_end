#!/usr/bin/env python3
"""
Filtered Logger module.
"""

import logging
import re
from typing import List

# define fields that contain personally identifiable information
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """obfuscates fields in a log message using regex."""
    return re.sub(fr'({"|".join(map(re.escape, fields))})=[^{separator}]*', 
                  rf'\1={redaction}', message)


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
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """returns a logger named 'user_data' with a redacting formatter"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False  # prevent logs from propagating to parent loggers
    
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    
    logger.addHandler(stream_handler)
    return logger
