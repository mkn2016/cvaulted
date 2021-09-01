from enum import unique
from operator import index
from extensions import db

from endpoints.roles.models import Role
from endpoints.mixins.timestamp import TimestampMixin
from flask_praetorian import current_user_id


roles = db.Table('user_roles',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)


class User(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_active = db.Column(db.Boolean, default=True, server_default="true")

    profile = db.relationship('Profile', backref='user', uselist=False)
    account = db.relationship('Account', backref='user', uselist=False)
    roles = db.relationship('Role', secondary=roles, lazy='dynamic', backref=db.backref('users', lazy=True))

    def __str__(self) -> str:
        return self.username
    
    @classmethod
    def get_all(cls):
        return cls.query.filter(User.id!=current_user_id())

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
    
    @classmethod
    def count(cls):
        return cls.query.count()


class Profile(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100), nullable=True)
    surname = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(20), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True, unique=True)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_profile_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def get_profile_by_user_id(cls, user_id):
        return cls.query.filter(Profile.user_id==user_id).first()

class Account(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    card_no = db.Column(db.String(150), unique=True, nullable=False)
    account_number = db.Column(db.String(150), nullable=False)
    account_name = db.Column(db.String(150), nullable=False)
    expiration_date = db.Column(db.String(150), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True, unique=False)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def count(cls):
        return cls.query.count()

    @classmethod
    def get_acccount_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def get_account_by_user_id(cls, user_id):
        return cls.query.filter(Account.user_id==user_id).first()
