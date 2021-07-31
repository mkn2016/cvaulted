from extensions import db

from endpoints.roles.models import Role
from endpoints.mixins.timestamp import TimestampMixin


roles = db.Table('user_roles',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)


class User(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    is_active = db.Column(db.Boolean, default=False, server_default="false")

    profile = db.relationship('Profile', backref='user', uselist=False)
    account = db.relationship('Account', backref='user', uselist=False)
    roles = db.relationship('Role', secondary=roles, lazy='dynamic', backref=db.backref('users', lazy=True))

    def __str__(self) -> str:
        return self.username
    
    @classmethod
    def get_all(cls):
        return cls.query.all()

    @property
    def identity(self):
        return self.id
    
    @property
    def rolenames(self):

        user_roles = ""

        for idx, role in enumerate(self.roles.all()):
            if idx == 0:
                user_roles += role.name
            else:
                user_roles += "," + role.name
        
        if user_roles:
            return user_roles.split(",")
        else:
            return []

    @classmethod
    def lookup(cls, username:str):
        return cls.query.filter_by(username=username).one_or_none()
    
    @classmethod
    def identify(cls, id:int):
        return cls.query.get(id)

    def is_valid(self):
        return self.is_active


class Profile(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=True)
    middle_name = db.Column(db.String(100), nullable=True)
    surname = db.Column(db.String(100), nullable=True)
    gender = db.Column(db.String(20), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_profile_by_user_id(cls, user_id):
        return cls.query.filter(Profile.user_id==user_id).first()
    
    @classmethod
    def get_profile_by_id(cls, id):
        return cls.query.get(id)


class Account(db.Model, TimestampMixin):
    # Mask 12 digits of 16 digits of card number
    id = db.Column(db.Integer, primary_key=True)
    card_no = db.Column(db.Integer, unique=True, nullable=False)
    expiration_date = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_acccount_by_id(cls, id):
        return cls.query.get(id)
