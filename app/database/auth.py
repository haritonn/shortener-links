from db import Session, User
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

# returns false if username is not found
def login_username(user):
    session = Session()
    results = session.query(User).filter(User.name==user).all()
    if len(results) == 0:
        session.close()
        return False 
    
    session.close()
    return True 

# check if password correct (should be used after checking username)
def login_password(user, password):
    session = Session()
    results = session.query(User).filter(User.name == user).all()
    
    if check_password_hash(results[0], password):
        session.close()
        return True 
    
    session.close()
    return False 

# registration of new user (True -> redirect to application page, False -> this user already exists)
def registration_user(user, password, error=None):
    new_user = User(username=user, password=generate_password_hash(password))
    try:
        with Session() as session:
            session.add(new_user)
            session.commit()
        
    except IntegrityError:
        session.rollback()
        error = f'User {user} already exists'
    
    return error