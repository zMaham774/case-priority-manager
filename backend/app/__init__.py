"""Flask application factory."""
from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    # TODO: load config, init database, build in-memory structures, register blueprints
    @app.get("/api/health")
    def health():
        return {"status": "ok"}
    return app
