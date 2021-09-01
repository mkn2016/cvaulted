from extensions import ma
from endpoints.roles.models import Role


class RoleSchema(ma.SQLAlchemySchema):
    class Meta:
        model=Role
        fields=(
            "id",
            "name",
            "created",
            "updated"
        )