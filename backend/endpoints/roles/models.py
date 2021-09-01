from extensions import db
from endpoints.mixins.timestamp import TimestampMixin


class Role(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_role_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def get_all_roles_by_name(cls):
        return cls.query.order_by(Role.name).all()
    
    @classmethod
    def get_role_by_name(cls, name):
        return cls.query.filter(Role.name==name).first()
    
    @classmethod
    def count(cls):
        return cls.query.count()
