#!/usr/bin/env python3
""" Basic authentication module """
import base64
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class that inherits from Auth """

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """
        Extracts the Base64 part of the Authorization header.

        Returns:
            - None if authorization_header is None or not a string.
            - None if authorization_header doesn't start with "Basic ".
            - The Base64 part of the Authorization header otherwise.
        """
        if authorization_header is None or not isinstance(
            authorization_header, str
        ):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[6:]  # Extract everything after "Basic "

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        Decodes a Base64 string.

        Returns:
            - None if base64_authorization_header is None or not a string.
            - None if base64_authorization_header is not a valid Base64 string.
            - The decoded UTF-8 string otherwise.
        """
        if base64_authorization_header is None or not isinstance(
            base64_authorization_header, str
        ):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode("utf-8")
        except Exception:
            return None
