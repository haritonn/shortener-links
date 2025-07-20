from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base 
import dotenv 
import os 

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(40), unique=False, nullable=False)

dotenv.load_dotenv()
USR = os.getenv('USERNAME')
PWD = os.getenv('PASSWORD')
DB_NAME = os.getenv('DATABASE')

CON_URL = f'mysql+pymysql://{USR}:{PWD}@localhost/{DB_NAME}'
engine = create_engine(CON_URL)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

