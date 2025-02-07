#!/usr/bin/env python3
""" Auth module for API authentication """
from flask import request
from typing import List, TypeVar


class Auth:
    """ Authentication class template """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.
        Currently, always returns False.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the request.
        Currently, always returns None.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user from the request.
        Currently, always returns None.
        """
        return None
