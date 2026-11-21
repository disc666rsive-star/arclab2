
import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

USERS_URL = os.getenv("USERS_URL", "http://localhost:5001")
PRODUCTS_URL = os.getenv("PRODUCTS_URL", "http://localhost:5002")


@app.route("/")
def home():
    return jsonify({
        "message": "Main application is working",
        "endpoints": ["/users", "/products", "/all"]
    })


@app.route("/users")
def users():
    response = requests.get(f"{USERS_URL}/users", timeout=5)
    response.raise_for_status()
    return jsonify(response.json())


@app.route("/products")
def products():
    response = requests.get(f"{PRODUCTS_URL}/products", timeout=5)
    response.raise_for_status()
    return jsonify(response.json())


@app.route("/all")
def all_data():
    users_response = requests.get(f"{USERS_URL}/users", timeout=5)
    products_response = requests.get(f"{PRODUCTS_URL}/products", timeout=5)

    users_response.raise_for_status()
    products_response.raise_for_status()

    return jsonify({
        "users": users_response.json(),
        "products": products_response.json()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
