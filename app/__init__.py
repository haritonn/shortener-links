from app.database import db
from flask import Flask
from app.routes.auth import auth_bp
from app.routes.shortener import app_bp


def create_app():
    app = Flask(__name__, static_folder="static/")
    db.init_db(app)
    app.config["SECRET_KEY"] = "dev"

    # Registering blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(app_bp)

    return app
