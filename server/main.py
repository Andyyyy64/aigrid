from src.controllers.post_chat_controller import post_chat_controller
import logging
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from src.get_env import get_env

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/chat", methods=["POST"])
def chat():
    get_message = request.json.get("message")
    logging.info("Get Message: %s", get_message)
    return post_chat_controller(get_message)


if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app.run(debug=True, host="0.0.0.0", port=port)