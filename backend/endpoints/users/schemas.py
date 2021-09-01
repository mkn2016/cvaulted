from marshmallow import fields, pre_dump
from marshmallow.exceptions import ValidationError

from extensions import ma
from endpoints.roles.schemas import RoleSchema
from endpoints.users.models import Account, User, Profile

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model=User
        fields=(
            "id",
            "username",
            "email",
            "is_active",
            "roles",
            "created",
            "updated",
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
        

class AccountSchema(ma.SQLAlchemySchema):
    class Meta:
        model=Account
        fields=(
            "id",
            "card_no",
            "account_number",
            "account_name",
            "expiration_date",
            "created",
            "updated",
        )
        ordered = True
    username = fields.Nested(UserSchema, many=True, only=["username"])