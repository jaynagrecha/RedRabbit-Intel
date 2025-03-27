from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class APIKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(100), unique=True, nullable=False)
    key = db.Column(db.String(512), nullable=False)

class SourceToggle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(100), unique=True, nullable=False)
    enabled = db.Column(db.Boolean, default=True)
    
class IOC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    indicator = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    source = db.Column(db.String(100), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "indicator": self.indicator,
            "type": self.type,
            "source": self.source
        }
