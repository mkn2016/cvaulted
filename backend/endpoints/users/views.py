from datetime import datetime

from flask import Blueprint, jsonify, request
from flask_praetorian.exceptions import (
    AuthenticationError,
    ExpiredAccessError,
    MissingRoleError
)
from flask_praetorian import current_user_id

from flask_restx import Resource, Namespace
from flask_praetorian.decorators import auth_required, roles_accepted, roles_required
from sqlalchemy.exc import IntegrityError

from extensions import db
from endpoints.users.schemas import ProfileSchema, UserSchema
from endpoints.users.models import Profile, User
from endpoints.permissions.permissions import is_not_owner, is_owner
from endpoints.roles.models import Role


user_namespace = Namespace("users", description="Authentication and Authorization Operations", path="/users")


@user_namespace.errorhandler(MissingRoleError)
def handle_error(e):
    return {"message": str(e)}

@user_namespace.errorhandler(AuthenticationError)
def handle_error(e):
    return {"message": str(e)}

@user_namespace.errorhandler(ExpiredAccessError)
def handle_error(e):
    return {"message": str(e)}

@user_namespace.errorhandler(IntegrityError)
def handle_error(e):
    return {"message": f"Profile already exists. Duplicate entries forbidden"}


class UserListResource(Resource):
    @user_namespace.doc("List_Users")
    @user_namespace.response(200, 'Success')
    @user_namespace.response(500, 'MissingRoleError')
    @user_namespace.response(500, 'AuthenticationError')
    @user_namespace.response(500, 'ExpiredAccessError')
    @auth_required
    @roles_required("superuser", "admin")
    def get(self):
        users = User.get_all()

        serializer = UserSchema(many=True)
        data=serializer.dump(users)
        return {"data": data}


class UserResource(Resource):
    @user_namespace.doc("Get_User")
    @user_namespace.response(200, 'Success')
    @user_namespace.response(404, 'User not found')
    @user_namespace.response(500, 'MissingRoleError')
    @user_namespace.response(500, 'AuthenticationError')
    @user_namespace.response(500, 'ExpiredAccessError')
    @auth_required
    @roles_required("superuser", "admin")
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
    
    @user_namespace.doc("Update_User")
    @user_namespace.response(200, 'Success')
    @user_namespace.response(404, 'User not found')
    @user_namespace.response(500, 'MissingRoleError')
    @user_namespace.response(500, 'AuthenticationError')
    @user_namespace.response(500, 'ExpiredAccessError')
    @auth_required
    @roles_required("superuser", "admin")
    @is_not_owner
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


class UserProfilesResource(Resource):
    @user_namespace.doc("Get_User_Profiles")
    @user_namespace.response(200, 'Success')
    @user_namespace.response(500, 'MissingRoleError')
    @user_namespace.response(500, 'AuthenticationError')
    @user_namespace.response(500, 'ExpiredAccessError')
    @auth_required
    @roles_accepted("superuser", "manager", "admin", "moderator")
    def get(self):
        profiles = Profile.get_all()

        serializer = ProfileSchema(many=True)
        data=serializer.dump(profiles)
        return {"data": data}


class UserProfileResource(Resource):
    @user_namespace.doc("Get_User_Profile")
    @user_namespace.response(200, 'Success')
    @user_namespace.response(404, 'User profile not found')
    @user_namespace.response(500, 'AuthenticationError')
    @user_namespace.response(500, 'ExpiredAccessError')
    @auth_required
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

class UserCreateProfileResource(Resource):
    @user_namespace.doc("Create_User_Profile")
    @user_namespace.response(200, 'Success')
    @user_namespace.response(500, 'AuthenticationError')
    @user_namespace.response(500, 'ExpiredAccessError')
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


class UserUpdateProfileResource(Resource):
    @user_namespace.doc("Edit_User_Profile")
    @user_namespace.response(200, 'Success')
    @user_namespace.response(404, 'User profile not found')
    @user_namespace.response(500, 'MissingRoleError')
    @user_namespace.response(500, 'AuthenticationError')
    @user_namespace.response(500, 'ExpiredAccessError')
    @auth_required
    @is_owner
    def put(self, id):

        profile = Profile.get_profile_by_user_id(current_user_id())

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

user_namespace.add_resource(UserListResource, "/")
user_namespace.add_resource(UserResource, "/<int:id>")
user_namespace.add_resource(UserProfilesResource, "/profiles")
user_namespace.add_resource(UserProfileResource, "/<int:id>/profile")
user_namespace.add_resource(UserCreateProfileResource, "/profile/create")
user_namespace.add_resource(UserUpdateProfileResource, "/<int:id>/profile/edit")