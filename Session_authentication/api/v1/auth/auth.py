#!/usr/bin/env python3
""" Auth module for API authentication """
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """ Authentication class template """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.
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
        """
        Retrieves the Authorization header from the request.
        Returns None if request is None or Authorization header is missing.
        """
        if request is None:
            return None

        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieves the current user from the request. """
        return None

    def session_cookie(self, request=None):
        """Returns a cookie value from a request"""
        if request is None:
            return None

        session_name = os.getenv("SESSION_NAME", "_my_session_id")
        return request.cookies.get(session_name)
