#!/usr/bin/env python3

from flask import Flask
from flask import jsonify
from flask import request
import json
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
    JWTManager,
)

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "pouetpouet"
# définir la clef hors du code dans une variable d'environnement
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if username in users and check_password_hash(user["password"], password):
        return username


@app.route("/basic-protected")
@auth.login_required
def access_granted():
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def index():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user_info = users.get(username)
    # Si mauvais utilisateur ou mauvais mot de passe → 401
    if not user_info or not check_password_hash(user_info["password"],
                                                password):
        return jsonify({"msg": "Bad credentials"}), 401
    # Sinon on génère le token
    access_token = create_access_token(
        identity=json.dumps({"username": username, "role": user_info["role"]})
    )
    return jsonify(access_token=access_token)


@app.route("/admin-only")
@jwt_required()
def admin_access():
    current_user = json.loads(get_jwt_identity())
    if current_user["role"] == "admin":
        return "Admin Access: Granted"
    else:
        return jsonify({"error": "Admin access required"}), 403


@app.route("/jwt-protected")
@jwt_required()
def protected():
    get_jwt_identity()
    return "JWT Auth: Access Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run(debug=True)
