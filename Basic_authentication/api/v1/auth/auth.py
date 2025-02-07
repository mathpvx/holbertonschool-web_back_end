#!/usr/bin/env python3
""" Auth module for API authentication """
from flask import request
from typing import List, TypeVar


class Auth:
    """ Authentication class template """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.

        Returns:
        - True if path is None or excluded_paths is None/empty.
        - False if path is in excluded_paths.
        - Handles slash tolerance for paths.
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        # Normalize paths to always end with '/'
        if path[-1] != "/":
            path += "/"

        normalized_excluded = [
            p if p[-1] == "/" else p + "/" for p in excluded_paths
        ]

        return path not in normalized_excluded

    def authorization_header(self, request=None) -> str:
        """ Retrieves the Authorization header from the request. """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieves the current user from the request. """
        return None
