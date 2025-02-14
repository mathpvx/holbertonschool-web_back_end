#!/usr/bin/env python3
""" Basic authentication module """
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
                authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[6:]  # Extract everything after "Basic "
