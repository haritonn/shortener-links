from database import db 
from flask import Flask

database = db.init_db()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    database.init_app(app)

    return app
