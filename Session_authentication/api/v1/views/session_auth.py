#!/usr/bin/env python3
""" Session authentication routes """
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login():
    """ Handles user login using session authentication """
    from api.v1.app import auth

    email = request.form.get("email")
    password = request.form.get("password")

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    # Find user by email
    users = User.search({"email": email})
    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    # Validate password
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Create session ID for the user
    session_id = auth.create_session(user.id)

    # Prepare response
    response = jsonify(user.to_json())

    # Set session cookie
    session_name = os.getenv("SESSION_NAME", "_my_session_id")
    response.set_cookie(session_name, session_id)

    return response
