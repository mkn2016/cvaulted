from marshmallow import fields

from extensions import ma
from endpoints.roles.schemas import RoleSchema
from endpoints.users.models import User, Profile


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model=User
        fields=(
            "username",
            "is_active",
            "roles",
            "created",
            "updated"
        )
        ordered = True
    roles = fields.Nested(RoleSchema, many=True, only=["name"])

class ProfileSchema(ma.SQLAlchemySchema):
    class Meta:
        model=Profile
        fields=(
            "first_name",
            "middle_name",
            "surname",
            "gender"
        )
        ordered = True