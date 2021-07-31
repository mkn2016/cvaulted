from passlib.context import CryptContext
from flask_sqlalchemy import SQLAlchemy
from flask_praetorian import Praetorian
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


ctx = CryptContext(schemes=["sha512_crypt"])
security = Praetorian()
security.pwd_ctx = ctx


db = SQLAlchemy()
ma = Marshmallow()
cors = CORS()
limiter = Limiter(key_func=get_remote_address)