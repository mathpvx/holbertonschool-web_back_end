#!/usr/bin/env python3
"""
Password Hashing Module.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt and returns the hashed password as a byte string.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks if a given password matches the stored hashed password.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
