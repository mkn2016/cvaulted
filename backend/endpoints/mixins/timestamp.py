from datetime import datetime

from extensions import db

class TimestampMixin(object):
    created = db.Column(
        db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)