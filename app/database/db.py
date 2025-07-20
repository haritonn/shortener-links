from sqlalchemy import create_engine, Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
import dotenv 
import os 

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(40), unique=False, nullable=False)

def init_db(app):
    dotenv.load_dotenv()
    USR = os.getenv('USERNAME')
    PWD = os.getenv('PASSWORD')
    DB_NAME = os.getenv('DATABASE')

    CON_URI = f'mysql+pymysql://{USR}:{PWD}@localhost/{DB_NAME}'
    db.init_app(app)

    with app.app_context():
        db.create_all()