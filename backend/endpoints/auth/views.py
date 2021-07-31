from flask import Blueprint, jsonify, request
from flask_restx import Api, Resource
from flask_praetorian.exceptions import AuthenticationError
from sqlalchemy.exc import IntegrityError

from extensions import security, db, limiter
from endpoints.users.models import User


auth_blueprint = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)
auth_api = Api(auth_blueprint)


@auth_api.errorhandler(AuthenticationError)
def handle_error(e):
    return {"message": str(e)}

@auth_api.errorhandler(IntegrityError)
def handle_error(e):
    return {"message": "Registration failed. Please use a different username"}


@auth_api.route("/login")
class AuthResource(Resource):
    decorators = [limiter.limit("5/minute")]

    @auth_api.doc("Login")
    @auth_api.response(200, 'Success')
    @auth_api.response(500, 'AuthenticationError')
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


@auth_api.route("/register")
class AuthRegisterResource(Resource):
    @auth_api.doc("Register")
    @auth_api.response(200, 'Success')
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