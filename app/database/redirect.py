from app.database.db import db, Links
from sqlalchemy.exc import IntegrityError
from app.utils import url_utils

# def save_original_url(link):
#    new_link = Links(original_url=link)
#    try:
#        db.session.add(new_link)
#        db.commit()
