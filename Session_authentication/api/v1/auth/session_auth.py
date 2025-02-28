#!/usr/bin/env python3
""" Session Authentication module """
import uuid
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """ Session-based authentication class """

    # Class attribute: shared storage for session IDs -> user IDs
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a new session ID for a given user_id.

        Returns:
            - None if user_id is None or not a string
            - A newly generated session ID (str) otherwise
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        # Generate a unique Session ID
        session_id = str(uuid.uuid4())

        # Store session-user mapping
        SessionAuth.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Gets user ID linked to a session ID """
        if session_id is None or not isinstance(session_id, str):
            return None  # Invalid session ID

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Retrieves a User instance based on a session cookie """
        if request is None:
            return None

        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        return User.get(user_id)
