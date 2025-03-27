from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    indicator = db.Column(db.String(128), nullable=False)
    severity = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
