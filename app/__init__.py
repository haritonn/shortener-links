from database import db 
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    db.init_db(app)

    return app 