from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from models import create_user, verify_user

auth_bp = Blueprint("auth", __name__)

# Register
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    create_user(data["username"], data["password"])
    return jsonify({"msg": "User created"}), 201

# Login
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    if verify_user(data["username"], data["password"]):
        token = create_access_token(identity=data["username"])
        return jsonify(access_token=token), 200

    return jsonify({"msg": "Invalid credentials"}), 401

# Protected route
@auth_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    return jsonify({"msg": "You accessed a protected route!"})