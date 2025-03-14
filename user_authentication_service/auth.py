#!/usr/bin/env python3
""" authentification methods
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """ method that takes in a password string arg and returns bytes"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
