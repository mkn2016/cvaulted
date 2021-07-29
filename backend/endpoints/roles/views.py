from datetime import datetime

from flask import Blueprint, jsonify, request
from flask_praetorian.exceptions import (
    AuthenticationError,
    ExpiredAccessError,
    MissingRoleError
)

from sqlalchemy.exc import IntegrityError

from flask_restx import Api, Resource
from flask_praetorian.decorators import auth_required, roles_required

from extensions import db
from endpoints.users.schemas import RoleSchema
from endpoints.roles.models import Role

roles_blueprint = Blueprint("roles", __name__)
roles_api = Api(roles_blueprint)


@roles_api.errorhandler(MissingRoleError)
def handle_error(e):
    return {"message": str(e)}

@roles_api.errorhandler(IntegrityError)
def handle_error(e):
    return {"message": "Could not create role. A role with that name already exists"}

@roles_api.errorhandler(AuthenticationError)
def handle_error(e):
    return {"message": str(e)}

@roles_api.errorhandler(ExpiredAccessError)
def handle_error(e):
    return {"message": str(e)}

@roles_api.route("/roles")
class RolesResource(Resource):
    @roles_api.doc("List_Roles")
    @roles_api.response(200, 'Success')
    @roles_api.response(500, 'MissingRoleError')
    @roles_api.response(500, 'AuthenticationError')
    @roles_api.response(500, 'ExpiredAccessError')
    @auth_required
    @roles_required("superuser", "manager")
    def get(self):
        roles = Role.get_all()

        serializer = RoleSchema(many=True)
        data=serializer.dump(roles)
        return {"data": data}
    
    @roles_api.doc("Create_Role")
    @roles_api.response(200, 'Success')
    @roles_api.response(500, 'MissingRoleError')
    @roles_api.response(500, 'AuthenticationError')
    @roles_api.response(500, 'ExpiredAccessError')
    @auth_required
    @roles_required("superuser", "manager")
    def post(self):
        data = request.get_json(force=True)

        print(data)

        role = Role(
            name=data.get("name")
        )

        try:
            db.session.add(role)
        except:
            pass
        else:
            db.session.commit()
            return jsonify({"message": "role saved successfully"})


@roles_api.route("/roles/<int:id>")
class RoleResource(Resource):
    @roles_api.doc("Get_Role")
    @roles_api.response(200, 'Success')
    @roles_api.response(404, 'Role not found')
    @roles_api.response(500, 'MissingRoleError')
    @roles_api.response(500, 'AuthenticationError')
    @roles_api.response(500, 'ExpiredAccessError')
    @auth_required
    @roles_required("superuser", "manager")
    def get(self, id):
        user = Role.get_role_by_id(id)

        if user:
            serializer = RoleSchema()
            data=serializer.dump(user)
            return {"data": data}
        else:
            return jsonify(
                {
                    "error": "User not found"
                }, 
                404
            )

    @roles_api.doc("Update_Role")
    @roles_api.response(200, 'Success')
    @roles_api.response(404, 'Role not found')
    @roles_api.response(500, 'MissingRoleError')
    @roles_api.response(500, 'AuthenticationError')
    @roles_api.response(500, 'ExpiredAccessError')
    @auth_required
    @roles_required("superuser", "manager")
    def put(self, id):
        role = Role.get_role_by_id(id)
        
        if role:
            data = request.get_json(force=True)

            if role.name == data.get("name"):
                return jsonify({"message": "Skipping updating role. Role is the same as the one in the database"}, 200)
            else:
                role.name = data.get("name")
                role.updated = datetime.now()

                try:
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    return jsonify({"error": e}, 500)
                else:
                    return jsonify({"message": "Role updated successfully"}, 200)
        else:
            return jsonify(
                {
                    "error": "Role not found"
                },
                404
            )
    
    @roles_api.doc("Delete_Role")
    @roles_api.response(200, 'Success')
    @roles_api.response(500, 'MissingRoleError')
    @roles_api.response(500, 'AuthenticationError')
    @roles_api.response(500, 'ExpiredAccessError')
    @auth_required
    @roles_required("superuser", "manager")
    def delete(self, id):
        role = Role.get_role_by_id(id)

        if role:
            try:
                db.session.delete(role)
            except:
                pass
            else:
                db.session.commit()
                return jsonify(
                    {"message": "Role deleted successfully"
                    },
                    204
                )
        else:
            return jsonify(
                {"message": "Role not found. Skipping deletion"},
                404
            )
    