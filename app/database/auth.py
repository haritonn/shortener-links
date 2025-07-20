from app.database.db import db, User
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

# returns false if username is not found
def login_username(user):
    query = User.query.filter_by(username=user).first()
    if query is None:
        return True 

    return False


# check if password correct (should be used after checking username)
def login_password(user, password):
    query = User.query.filter_by(username=user).first()
    if not query:
        return False 
    
    return check_password_hash(query.password, password)

# registration of new user (True -> redirect to application page, False -> this user already exists)
def registration_user(user, password, error=None):
    new_user = User(username=user, password=generate_password_hash(password)) 
    
    try:
        db.session.add(new_user)
        db.session.commit()

    except IntegrityError:
        db.session.rollback()
        error = f'User {user} already exists'
    
    return error