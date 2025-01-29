"""
Function that returns the log message obfuscated
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Obfuscates fields in a log message using regex."""
    return re.sub(fr'({"|".join(map(re.escape, fields))})=[^{separator}]*', 
                  rf'\1={redaction}', message)
