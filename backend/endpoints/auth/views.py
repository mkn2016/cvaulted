from flask import Blueprint, jsonify, request

from extensions import security

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json(force=True)

    username = data.get("username", None)
    password = data.get("password", None)

    user = security.authenticate(
        username,
        password
    )

    token = security.encode_jwt_token(user)

    ret = {
        "access_token": token
    }

    return (
        jsonify(ret),
        200
    )