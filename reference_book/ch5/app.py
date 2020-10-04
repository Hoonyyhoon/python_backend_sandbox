from flask import Flask, jsonify, request, abort
from flask.json import JSONEncoder

import sys

class CustomJSONEncoder(JSONEncoder):
    """Override JSONEncoder to handle set instance."""
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)

        return JSONEncoder.default(self, obj)

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
app.id_count = 1
app.users = {}
app.tweets = []

@app.route("/ping", methods=["GET"])
def ping():
    "Endpoint ping for test"
    return "pong"

@app.route("/sign-up", methods=["POST"])
def sign_up():
    "Endpoint sign up"
    app.logger.info(f"? {request.json}")
    new_user = request.json
    new_user["id"] = app.id_count
    app.users[app.id_count] = new_user
    app.id_count = app.id_count + 1

    return jsonify(new_user)

@app.route("/tweet", methods=["POST"])
def tweet():
    "Endpoint tweet"
    d = request.json
    tweet = d["tweet"]
    user = int(d["id"])

    if len(tweet)>300:
        return "Tweet exceed 300", 400

    if user not in app.users:
        return "Invalid user id", 400

    app.tweets.append({"user_id": user,
                       "tweet": tweet})

    return '', 200

@app.route("/follow", methods=["POST"])
def follow():
    """Endpoint follow."""
    d = request.json
    user = d["id"]
    user_to_follow = d["follow"]
    if user not in app.users:
        return "Invalid user", 400
    if user_to_follow not in app.users:
        return "Invalid user to follow", 400

    app.users[user].setdefault("follow", set()).add(user_to_follow)

    return jsonify(user)

@app.route("/unfollow", methods=["POST"])
def unfollow():
    """Endpoint unfollow."""
    d = request.json
    user = d["id"]
    user_to_unfollow = d["unfollow"]
    if user not in app.users:
        return "Invalid user", 400
    if user_to_unfollow not in app.users:
        return "Invalid user to unfollow", 400

    app.users[user].setdefault("follow", set()).discard(user_to_unfollow)

    return jsonify(user)

@app.route("/timeline/<int:user_id>", methods=["GET"])
def timeline(user_id):
    if user_id not in app.users:
        return "User not exist", 400
    follow_ids = app.users[user_id].get("follow", set())
    follow_ids.add(user_id)
    timeline = [t for t in app.tweets if t["user_id"] in follow_ids]

    return jsonify({"user_id": user_id,
                    "timeline": timeline})
