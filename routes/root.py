from flask import Blueprint

root_bp = Blueprint('root_bp', __name__)

@root_bp.route('/')
def root():
    return "Red Rabbit Intelligence API is live."
