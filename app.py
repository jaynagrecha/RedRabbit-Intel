from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS  # Import the CORS module
from routes.root import root_bp

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    jwt.init_app(app)

    # Enable CORS for all routes (optional: configure it more precisely if needed)
    CORS(app)

    from routes.ioc import ioc_bp
    app.register_blueprint(root_bp)
    app.register_blueprint(ioc_bp, url_prefix='/api/ioc')

    return app