from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required

from models import create_user, verify_user

auth_bp = Blueprint("auth", __name__)


def _credentials():
    data = request.get_json(silent=True) or {}
    username = (data.get("username") or "").strip()
    password = data.get("password")
    return username, password


@auth_bp.route("/register", methods=["POST"])
def register():
    username, password = _credentials()
    if not username or not password:
        return jsonify({"msg": "username and password required"}), 400
    if not create_user(username, password):
        return jsonify({"msg": "Username already exists"}), 409
    return jsonify({"msg": "User created"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    username, password = _credentials()
    if not username or not password:
        return jsonify({"msg": "username and password required"}), 400
    if verify_user(username, password):
        token = create_access_token(identity=username)
        return jsonify(access_token=token), 200
    return jsonify({"msg": "Invalid credentials"}), 401


@auth_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    return jsonify({"msg": "You accessed a protected route!"})
