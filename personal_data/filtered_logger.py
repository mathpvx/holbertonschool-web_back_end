#!/usr/bin/env python3
"""
Function that returns the log message obfuscated
"""

import re
from typing import List
import logging


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """Function that returns the log message obfuscated"""

    for field in fields:
        # defines pattern as 'anything but special characters in field' =
        # 'anything but the separator'
        pattern = fr"{re.escape(field)}=[^{re.escape(separator)}]*"
        message = re.sub(pattern, f"{field}={redaction}", message)

    return message


class RedactingFormatter(logging.Formatter):
    """ custom class that inherits from logging lib
    that defines how log messages should be formatted
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)
