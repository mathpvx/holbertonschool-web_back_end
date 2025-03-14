#!/usr/bin/env python3
""" authentification methods """

from db import DB
from user import User
from sqlalchemy.exc import NoResultFound
import bcrypt
import uuid


def _hash_password(password: str) -> bytes:
    """method that takes in a password string arg and returns bytes"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt)


def _generate_uuid() -> str:
    """method that returns a string representation of a new uuid"""
    return str(uuid.uuid4())


class Auth:
    """auth class to interact with the authentication database"""

    def __init__(self):
        """initialize auth instance"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """method that checks if the
        user already exists and creates one if not the case"""
        try:
            existing_user = self._db.find_user_by(email=email)
            if existing_user:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed_password = _hash_password(password).decode("utf-8")
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """check if the email and password provided match a registered user"""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                password.encode("utf-8"),
                user.hashed_password.encode("utf-8")
            )
        except NoResultFound:
            return False
