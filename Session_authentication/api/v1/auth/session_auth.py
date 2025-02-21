#!/usr/bin/env python3
""" Session Authentication module """
from api.v1.auth.auth import Auth


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
