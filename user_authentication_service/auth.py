#!/usr/bin/env python3
""" authentification methods
"""
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound
import bcrypt


class Auth:
    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """ method that takes in a password string arg and returns bytes"""
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def register_user(self, email: str, password: str) -> User:
        """method that checks if the user already exists
        and creates one if not the case"""
        try:
            existing_user = self._db.find_user_by(email=email)
            if existing_user:
                raise ValueError("User {} already exists".format(email))

        except NoResultFound:
            hashed_password = self._hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user
