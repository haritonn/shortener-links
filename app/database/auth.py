from app.database.db import db, User
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user


# returns false if username is not found
def login_username(user):
    userfound = User.query.filter_by(username=user).first()
    if userfound is None:
        return False

    login_user(userfound)
    return True


# check if password correct (should be used after checking username)
def login_password(user, password):
    found = User.query.filter_by(username=user).first()
    return check_password_hash(found.password, password)


# registration of new user
def registration_user(user, password, error=None):
    new_user = User(username=user, password=generate_password_hash(password))

    try:
        db.session.add(new_user)
        db.session.commit()

    except IntegrityError:
        db.session.rollback()
        error = f"User {user} already exists"

    login_user(new_user)
    db.session.close()

    return error
