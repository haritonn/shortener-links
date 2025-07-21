from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from flask_sqlalchemy import SQLAlchemy
import dotenv
import os

db = SQLAlchemy()


# user name <-> user password table
class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(20), unique=True, nullable=False)
    password = Column(VARCHAR(200), unique=False, nullable=False)

    rl = db.relationship("Links", backref="users", lazy=True, cascade="all, delete")


# long link <-> short link table
class Links(db.Model):
    __tablename__ = "links"
    id = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    original_url = Column(VARCHAR(250), nullable=False)
    shorter_url = Column(VARCHAR(50), nullable=True, unique=True)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )


# application initialization
def init_db(app):
    dotenv.load_dotenv()
    USR = os.getenv("USERNAME")
    PWD = os.getenv("PASSWORD")
    DB_NAME = os.getenv("DATABASE")

    # Application configuration
    CON_URI = f"mysql+pymysql://{USR}:{PWD}@localhost:3306/{DB_NAME}"
    app.config["SQLALCHEMY_DATABASE_URI"] = CON_URI
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_recycle": 28000,
        "pool_pre_ping": True,
    }

    db.init_app(app)

    with app.app_context():
        db.create_all()
