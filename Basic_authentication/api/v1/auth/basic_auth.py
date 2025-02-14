#!/usr/bin/env python3
""" Basic authentication module """
import base64
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User


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

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        Extracts the user email and password from the decoded Base64 string.

        Returns:
            - (None, None) if input is None, not a string, or missing ':'.
            - Tuple (email, password) otherwise.
        """
        if decoded_base64_authorization_header is None or not isinstance(
            decoded_base64_authorization_header, str
        ):
            return None, None

        if ":" not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(":", 1)
        return email, password

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar("User"):
        """
        Retrieves a User instance based on email and password.

        Returns:
            - None if user_email or user_pwd is None or not strings.
            - None if no User instance is found with the given email.
            - None if password is incorrect.
            - The User instance otherwise.
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        users = User.search({"email": user_email})
        if not users or len(users) == 0:
            return None

        user = users[0]  # Assuming only one user per email
        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Retrieves the User instance for a request.

        Uses:
            - authorization_header
            - extract_base64_authorization_header
            - decode_base64_authorization_header
            - extract_user_credentials
            - user_object_from_credentials

        Returns:
            - None if authentication fails.
            - The authenticated User instance otherwise.
        """
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        base64_auth = self.extract_base64_authorization_header(auth_header)
        if base64_auth is None:
            return None

        decoded_auth = self.decode_base64_authorization_header(base64_auth)
        if decoded_auth is None:
            return None

        email, password = self.extract_user_credentials(decoded_auth)
        if email is None or password is None:
            return None

        return self.user_object_from_credentials(email, password)
