from flask import jsonify, request
from flask_restx import Resource, Namespace
from flask_restx.cors import crossdomain
from flask_praetorian.exceptions import AuthenticationError
from flask_limiter.errors import RateLimitExceeded
from sqlalchemy.exc import IntegrityError

from extensions import security, db, limiter, cors
from endpoints.users.models import User


auth_namespace = Namespace("auth", description="Authentication and Authorization Operations", path="/auth")


@auth_namespace.errorhandler(AuthenticationError)
def handle_error(e):
    return {"message": str(e)}

@auth_namespace.errorhandler(IntegrityError)
def handle_error(e):
    return {"message": f"Duplicate entries forbidden: {str(e)}"}

@auth_namespace.errorhandler(RateLimitExceeded)
def handle_error(e):
    return {"message": "Login attempts exceeded. 5 attempts per minute"}

@auth_namespace.route("/login")
class AuthResource(Resource):
    decorators = [limiter.limit("5/minute")]

    @auth_namespace.doc("Login")
    @auth_namespace.response(200, 'Success')
    @auth_namespace.response(429, 'RateLimitExceeded')
    @auth_namespace.response(500, 'AuthenticationError')
    def post(self):
        data = request.get_json(force=True)

        username = data.get("username", None)
        password = data.get("password", None)

        print(username, password)

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

                    return jsonify({"data": token}, 200)
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
        email = data.get("email", None)
        password = data.get("password", None)

        if username and email and password:
            user = User(
                username=username,
                email=email,
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
                    "message": "Username or email or password is required"
                },
                400
            )

@auth_namespace.route("/logout")
class AuthLogoutResource(Resource):
    @auth_namespace.doc("Logout")
    @auth_namespace.response(500, 'Failed')
    @auth_namespace.response(200, 'Success')
    def post(self):
        try:
            security.encode_jwt_token(is_reset_token=True)
        except:
            return jsonify({"message": "Logged out failed"}, 500)
        else:
            return jsonify({"data": "Logged out successfully"}, 200)