#!/usr/bin/env python3
""" Session Authentication module """
import uuid
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """ Session-based authentication class """

    user_id_by_session_id = {}  # Stores session -> user_id mappings

    def create_session(self, user_id: str = None) -> str:
        """ Creates a new session ID for a given user_id """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Gets user ID linked to a session ID """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def destroy_session(self, request=None) -> bool:
        """ Deletes a user session (logs out) """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        if session_id not in self.user_id_by_session_id:
            return False

        del self.user_id_by_session_id[session_id]
        return True
