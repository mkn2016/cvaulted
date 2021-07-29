from flask_sqlalchemy import SQLAlchemy
from flask_praetorian import Praetorian
from flask_marshmallow import Marshmallow

security = Praetorian()
db = SQLAlchemy()
ma = Marshmallow()