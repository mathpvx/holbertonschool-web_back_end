#!/usr/bin/env python3
"""
Function that returns the log message obfuscated
"""

import re
from typing import List


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
