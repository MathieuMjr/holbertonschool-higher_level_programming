#!/usr/bin/env python3

from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/status/")
def status():
    return "OK"


@app.route("/add_user", methods=['POST'])
def add_user():
    global users
    new_user = request.get_json()
    if "username" not in new_user:
        return jsonify("{'error' : 'username is required'}")
    user_info = {}
    for key, value in new_user.items():
        if key != "username":
            user_info[key] = value
    users[new_user["username"]] = user_info
    return jsonify({"message": f"User {new_user['username']} added",
                    "user": user_info}), 201


@app.route("/users/<username>")
def get_user(username):
    global users
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


@app.route("/data")
def usernames():
    global users
    users_list = []
    for key in users:
        users_list.append(key)
    return jsonify(users_list)


if __name__ == "__main__":
    app.run()
