from flask import Flask, jsonify
import os

def create_app():
    app = Flask(__name__)

    @app.route("/hello", methods=["GET"])
    def hello():
        # dummy route returns JSON
        return jsonify({"message": "hello, world!"}), 200

    return app


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    api_key = os.environ.get("API_KEY")
    env = os.environ.get("FLASK_ENV")
    app = create_app()
    app.run(host="0.0.0.0", port=port, debug=True)
