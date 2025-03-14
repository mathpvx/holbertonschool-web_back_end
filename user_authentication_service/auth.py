#!/usr/bin/env python3
""" authentification methods """

from db import DB
from user import User
from sqlalchemy.exc import NoResultFound
import bcrypt
import uuid


def _hash_password(password: str) -> str:
    """method that takes in a password string arg and returns a hashed string"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")


def _generate_uuid() -> str:
    """method that returns a string representation of a new uuid"""
    return str(uuid.uuid4())


class Auth:
    """auth class to interact with the authentication database"""

    def __init__(self):
        """initialize auth instance"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """method that checks if the user already exists and creates one
        if not the case"""
        try:
            existing_user = self._db.find_user_by(email=email)
            if existing_user:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """check if the email and password provided match a registered user"""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode("utf-8"),
                                  user.hashed_password.encode("utf-8"))
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """finds the user by email, generates a session id, updates the user
        session_id in the database and returns the session id"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """returns the user corresponding to the given session id
        or none if session id is none or no user is found"""
        if session_id is None:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """updates the corresponding user’s session id to none"""
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            pass

    def get_reset_password_token(self, email: str) -> str:
        """finds the user by email, generates a password reset token,
        updates the user reset_token in the database and returns the token"""
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
        except NoResultFound:
            raise ValueError("User not found")

    def update_password(self, reset_token: str, password: str) -> None:
        """uses reset token to find user and updates the password"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            self._db.update_user(user.id, hashed_password=hashed_password,
                                 reset_token=None)
        except NoResultFound:
            raise ValueError("Invalid reset token")
