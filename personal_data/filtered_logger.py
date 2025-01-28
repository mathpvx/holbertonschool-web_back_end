#!/usr/bin/env python3
import re


def filter_datum(fields, redaction, message, separator):

    for field in fields:
        # defines pattern as 'anything but special characters in field' =
        # 'anything but the separator'
        pattern = fr"{re.escape(field)}=([^({separator})]+)"
        message = re.sub(pattern, f"{field}={redaction}", message)

        return message
