from sys import path
from flask import Blueprint, jsonify, request
from flask_restx import Resource, Namespace
from flask_praetorian.exceptions import AuthenticationError
from sqlalchemy.exc import IntegrityError

from extensions import security, db, limiter
from endpoints.users.models import User


auth_namespace = Namespace("auth", description="Authentication and Authorization Operations", path="/auth")


@auth_namespace.errorhandler(AuthenticationError)
def handle_error(e):
    return {"message": str(e)}

@auth_namespace.errorhandler(IntegrityError)
def handle_error(e):
    return {"message": "Registration failed. Please use a different username"}

@auth_namespace.route("/login")
class AuthResource(Resource):
    decorators = [limiter.limit("5/minute")]

    @auth_namespace.doc("Login")
    @auth_namespace.response(200, 'Success')
    @auth_namespace.response(500, 'AuthenticationError')
    def post(self):
        data = request.get_json(force=True)

        username = data.get("username", None)
        password = data.get("password", None)

        user = security.authenticate(
            username,
            password
        )

        if user.is_valid():
            if user.profile is not None:
                if user.profile.first_name and user.profile.surname:
                    token = {
                        "access_token": security.encode_jwt_token(
                            user,
                            first_name=user.profile.first_name,
                            surname=user.profile.surname,
                            member_since=user.created.strftime("%d-%m-%Y %X"),
                            roles=[user_role.name for user_role in user.roles.all()]
                        )
                    }

                    return jsonify(token, 200)
                else:
                    token = {
                        "access_token": security.encode_jwt_token(
                            user,
                            username=user.username,
                            member_since=user.created.strftime("%d-%m-%Y %X"),
                            roles=[user_role.name for user_role in user.roles.all()]
                        )
                    }

                    return jsonify(token, 200)
            else:
                token = {
                    "access_token": security.encode_jwt_token(
                        user,
                        username=user.username,
                        member_since=user.created.strftime("%d-%m-%Y %X"),
                        roles=[user_role.name for user_role in user.roles.all()]
                    )
                }

                return jsonify(token, 200)
        else:
            return jsonify(
                {
                    "error": "User is not active. Please confirm with admin for support."
                },
                403
            )

@auth_namespace.route("/register")
class AuthRegisterResource(Resource):
    @auth_namespace.doc("Register")
    @auth_namespace.response(200, 'Success')
    def post(self):
        data = request.get_json(force=True)

        username = data.get("username", None)
        password = data.get("password", None)

        if username and password:
            user = User(
                username=username,
                password=security.hash_password(password)
            )
            
            try:
                db.session.add(user)
            except:
                pass
            else:
                db.session.commit()
                return jsonify({"message": "user registered successfully"})


        else:
            return jsonify(
                {
                    "errors": "Username or password is required"
                },
                400
            )