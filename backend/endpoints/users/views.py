from datetime import datetime

from flask import Blueprint, json, jsonify, request
from flask_praetorian.exceptions import (
    AuthenticationError,
    ExpiredAccessError,
    MissingRoleError
)
from flask_praetorian import current_user_id, current_user

from flask_restx import Api, Resource
from flask_praetorian.decorators import auth_required, roles_accepted, roles_required

from extensions import db
from endpoints.users.schemas import ProfileSchema, UserSchema
from endpoints.users.models import Profile, User
from endpoints.users.models import roles as roles_rel
from endpoints.roles.models import Role

users_blueprint = Blueprint(
    "users",
    __name__,
    url_prefix="/users/"
)

users_api = Api(users_blueprint)

@users_api.errorhandler(MissingRoleError)
def handle_error(e):
    return {"message": str(e)}

@users_api.errorhandler(AuthenticationError)
def handle_error(e):
    return {"message": str(e)}

@users_api.errorhandler(ExpiredAccessError)
def handle_error(e):
    return {"message": str(e)}

@users_api.route("/")
class UserListResource(Resource):
    @users_api.doc("List_Users")
    @users_api.response(200, 'Success')
    @users_api.response(500, 'MissingRoleError')
    @users_api.response(500, 'AuthenticationError')
    @users_api.response(500, 'ExpiredAccessError')
    @auth_required
    @roles_required("superuser", "manager")
    def get(self):
        users = User.get_all()

        serializer = UserSchema(many=True)
        data=serializer.dump(users)
        return {"data": data}


@users_api.route("/<int:id>")
class UserResource(Resource):
    @users_api.doc("Get_User")
    @users_api.response(200, 'Success')
    @users_api.response(404, 'User not found')
    @users_api.response(500, 'MissingRoleError')
    @users_api.response(500, 'AuthenticationError')
    @users_api.response(500, 'ExpiredAccessError')
    @auth_required
    @roles_required("superuser", "manager")
    def get(self, id):
        user = User.identify(id)

        if user:
            serializer = UserSchema()
            data=serializer.dump(user)
            return {"data": data}
        else:
            return jsonify(
                {
                    "error": "User not found"
                }, 
                404
            )
    
    @users_api.doc("Update_User")
    @users_api.response(200, 'Success')
    @users_api.response(404, 'User not found')
    @users_api.response(500, 'MissingRoleError')
    @users_api.response(500, 'AuthenticationError')
    @users_api.response(500, 'ExpiredAccessError')
    @auth_required
    @roles_required("superuser", "manager")
    def put(self, id):
        user = User.identify(id)
        
        if user:
            data = request.get_json(force=True)

            user.is_active = data.get("is_active")
            
            roles = data.get("roles")
            available_roles = Role.get_all_roles_by_name()
            role_names = [role.name for role in available_roles]
            user_roles = [user_role.name for user_role in user.roles.all()]

            if len(roles) == 1:
                if available_roles:
                    input_role = roles[0]
                    if input_role in role_names:
                        if input_role in user_roles:
                            return jsonify(
                                {
                                    "message": "User already has the neccessary roles"
                                },
                                200
                            )
                        else:
                            role = Role.get_role_by_name(input_role)
                            role.users.append(user)
                    else:
                        pass
                else:
                    return jsonify(
                        {
                            "message": "Please add the neccessary roles and permissions before proceeding..."
                        },
                        200
                    )
            else:
                if available_roles:
                    for input_role in roles:
                        if input_role in role_names:
                            if input_role in user_roles:
                                return jsonify(
                                    {
                                        "message": "User already has the neccessary roles"
                                    },
                                    200
                                )
                            else:
                                role = Role.get_role_by_name(input_role)
                                role.users.append(user)
                        else:
                            pass
                else:
                    return jsonify(
                        {
                            "message": "Please add the neccessary roles and permissions before proceeding..."
                        },
                        200
                    )

            user.updated = datetime.now()

            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return jsonify({"error": e}, 500)
            else:
                return jsonify({"message": "User updated successfully"}, 200)
        else:
            return jsonify(
                {
                    "error": "User not found"
                },
                404
            )

@users_api.route("/profiles")
class UserProfilesResource(Resource):
    @users_api.doc("Get_User_Profiles")
    @users_api.response(200, 'Success')
    @users_api.response(500, 'MissingRoleError')
    @users_api.response(500, 'AuthenticationError')
    @users_api.response(500, 'ExpiredAccessError')
    @auth_required
    @roles_accepted("superuser", "manager", "admin", "moderator")
    def get(self):
        profiles = Profile.get_all()

        serializer = ProfileSchema(many=True)
        data=serializer.dump(profiles)
        return {"data": data}


@users_api.route("/<int:id>/profile")
class UserProfileResource(Resource):
    @users_api.doc("Get_User_Profile")
    @users_api.response(200, 'Success')
    @users_api.response(404, 'User profile not found')
    @users_api.response(500, 'MissingRoleError')
    @users_api.response(500, 'AuthenticationError')
    @users_api.response(500, 'ExpiredAccessError')
    @auth_required
    @roles_required("superuser", "manager")
    def get(self, id):
        profile = Profile.get_profile_by_user_id(id)

        if profile:
            serializer = ProfileSchema()
            data=serializer.dump(profile)
            return {"data": data}
        else:
            return jsonify(
                {
                    "error": "User profile not found"
                }, 
                404
            )


@users_api.route("/profile/create")
class UserCreateProfileResource(Resource):
    @users_api.doc("Create_User_Profile")
    @users_api.response(200, 'Success')
    @users_api.response(500, 'MissingRoleError')
    @users_api.response(500, 'AuthenticationError')
    @users_api.response(500, 'ExpiredAccessError')
    @auth_required
    def post(self):
        data = request.get_json(force=True)

        profile = Profile(
            first_name=data.get("first_name"),
            middle_name=data.get("middle_name"),
            surname=data.get("surname"),
            gender=data.get("gender"),
            user_id=current_user_id()
        )

        try:
            db.session.add(profile)
        except:
            pass
        else:
            db.session.commit()
            return jsonify({"message": "profile created successfully"})


@users_api.route("/<int:id>/profile/edit")
class UserUpdateProfileResource(Resource):
    @users_api.doc("Edit_User_Profile")
    @users_api.response(200, 'Success')
    @users_api.response(404, 'User profile not found')
    @users_api.response(500, 'MissingRoleError')
    @users_api.response(500, 'AuthenticationError')
    @users_api.response(500, 'ExpiredAccessError')
    @auth_required
    def put(self, id):
        profile = Profile.get_profile_by_id(id)

        if profile:
            data = request.get_json(force=True)

            profile.first_name = data.get("first_name")
            profile.middle_name = data.get("middle_name")
            profile.surname = data.get("surname")
            profile.gender = data.get("gender")
            profile.updated = datetime.now()

            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return jsonify({"error": e}, 500)
            else:
                return jsonify({"message": "Profile updated successfully"}, 200)
        else:
            return jsonify(
                {
                    "error": "User profile not found"
                }, 
                404
            )