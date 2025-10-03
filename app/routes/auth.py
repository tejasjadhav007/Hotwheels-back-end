from flask import Blueprint, request, jsonify
from .. import db
from ..models import User
from flask_jwt_extended import create_access_token


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json or {}
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({'msg': 'email and password required'}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({'msg': 'user exists'}), 400
    user = User(email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'msg': 'created'}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json or {}
    email = data.get('email')
    password = data.get('password')
    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({'msg': 'bad credentials'}), 401
    access_token = create_access_token(identity={'id': user.id, 'email': user.email, 'is_admin': user.is_admin})
    return jsonify({'access_token': access_token, 'user': {'id': user.id, 'email': user.email, 'is_admin': user.is_admin}})