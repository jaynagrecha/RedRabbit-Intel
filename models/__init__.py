from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class IOC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    indicator = db.Column(db.String(128), unique=True, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    source = db.Column(db.String(128))
    
    def serialize(self):
        return {
            'id': self.id,
            'indicator': self.indicator,
            'type': self.type,
            'source': self.source
        }
