
from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Ivan", "age": 20},
    {"id": 2, "name": "Anna", "age": 22},
    {"id": 3, "name": "Alex", "age": 21}
]


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Users service is working"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
