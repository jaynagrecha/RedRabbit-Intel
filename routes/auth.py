from flask import Blueprint, request, jsonify
from models.auth import User, db
from flask_jwt_extended import create_access_token
from datetime import timedelta

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'User already exists'}), 409
    user = User(username=data['username'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'})

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.username, expires_delta=timedelta(hours=6))
        return jsonify(access_token=access_token)
    return jsonify({'message': 'Invalid credentials'}), 401
