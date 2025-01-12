from flask import Blueprint, jsonify, request, make_response
from repository.userService import UserService
from config.config import SECRET_KEY
import datetime
import jwt

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = UserService.register(first_names=data.get('first_names'), last_names=data.get('last_names'), username=data.get('username'), email=data.get('email'), password=data.get('password'))
    return jsonify({'message': 'successful', 'user': new_user}), 201

@user_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    result = UserService.login(email=data.get('email'), password=data.get('password'))
    
    if result['boolean']:
        response = make_response(jsonify({'message': 'login successful'}), 200)
        expires = datetime.datetime.now() + datetime.timedelta(hours=1)
        
        payload = {
            'id': str(result['id']),
            'iat': datetime.datetime.now(),
            'exp': expires
        }
        
        token = jwt.encode(payload=payload, key=SECRET_KEY, algorithm='HS256')
        
        response.set_cookie(
            'auth_token',
            token,
            httponly=True,
            samesite='Lax',
            expires=expires
        )
        
        return response
    else:
        return jsonify({'message': 'the password or the email no match'}), 400