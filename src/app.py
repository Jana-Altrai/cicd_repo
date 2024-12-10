from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 201


# The new endpoint you’re adding on the feature branch
@app.route("/users", methods=["GET"])
def get_users():
    # In a real scenario, you might query a database.
    # Here, return a simple static list of users.
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]
    return jsonify(users), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
