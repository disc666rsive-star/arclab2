
from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mouse", "price": 1500},
    {"id": 3, "name": "Keyboard", "price": 3000}
]


@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Products service is working"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
