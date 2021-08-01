from datetime import datetime

from flask import jsonify, request
from flask_praetorian.exceptions import (
    AuthenticationError,
    ExpiredAccessError,
    MissingRoleError
)
from sqlalchemy.exc import IntegrityError
from flask_restx import Resource, Namespace
from flask_praetorian.decorators import auth_required, roles_required

from extensions import db
from endpoints.users.schemas import RoleSchema
from endpoints.roles.models import Role


role_namespace = Namespace("roles", description="Authentication and Authorization Operations", path="/roles")


@role_namespace.errorhandler(MissingRoleError)
def handle_error(e):
    return {"message": str(e)}

@role_namespace.errorhandler(IntegrityError)
def handle_error(e):
    return {"message": f"Duplicate entries forbidden: {str(e)}"}

@role_namespace.errorhandler(AuthenticationError)
def handle_error(e):
    return {"message": str(e)}

@role_namespace.errorhandler(ExpiredAccessError)
def handle_error(e):
    return {"message": str(e)}

@role_namespace.route("/")
class RolesResource(Resource):
    @role_namespace.doc("List_Roles")
    @role_namespace.response(200, 'Success')
    @role_namespace.response(500, 'MissingRoleError')
    @role_namespace.response(500, 'AuthenticationError')
    @role_namespace.response(500, 'ExpiredAccessError')
    @auth_required
    @roles_required("superuser", "admin")
    def get(self):
        roles = Role.get_all()

        serializer = RoleSchema(many=True)
        data=serializer.dump(roles)
        return {"data": data}
    
    @role_namespace.doc("Create_Role")
    @role_namespace.response(200, 'Success')
    @role_namespace.response(500, 'MissingRoleError')
    @role_namespace.response(500, 'AuthenticationError')
    @role_namespace.response(500, 'ExpiredAccessError')
    @auth_required
    @roles_required("superuser", "admin")
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


@role_namespace.route("/<int:id>")
class RoleResource(Resource):
    @role_namespace.doc("Get_Role")
    @role_namespace.response(200, 'Success')
    @role_namespace.response(404, 'Role not found')
    @role_namespace.response(500, 'MissingRoleError')
    @role_namespace.response(500, 'AuthenticationError')
    @role_namespace.response(500, 'ExpiredAccessError')
    @auth_required
    @roles_required("superuser", "admin")
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

    @role_namespace.doc("Update_Role")
    @role_namespace.response(200, 'Success')
    @role_namespace.response(404, 'Role not found')
    @role_namespace.response(500, 'MissingRoleError')
    @role_namespace.response(500, 'AuthenticationError')
    @role_namespace.response(500, 'ExpiredAccessError')
    @auth_required
    @roles_required("superuser", "admin")
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
    
    @role_namespace.doc("Delete_Role")
    @role_namespace.response(200, 'Success')
    @role_namespace.response(500, 'MissingRoleError')
    @role_namespace.response(500, 'AuthenticationError')
    @role_namespace.response(500, 'ExpiredAccessError')
    @auth_required
    @roles_required("superuser", "admin")
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
    