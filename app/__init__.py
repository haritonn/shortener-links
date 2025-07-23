from app.database import db
from flask import Flask
from flask_login import LoginManager
from app.routes.auth import auth_bp
from app.routes.shortener import app_bp
import dotenv
import os


def create_app():
    dotenv.load_dotenv()
    app = Flask(__name__, static_folder="static/")
    db.init_db(app)
    app.config["SECRET_KEY"] = os.getenv("DEV_KEY")

    # Registering blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(app_bp)

    # For login-required pages
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def get_user(user_id):
        if not user_id or user_id == "None":
            return None
        try:
            return db.User.query.get(int(user_id))
        except ValueError:
            return None

    return app
