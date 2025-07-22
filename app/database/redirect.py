from app.database.db import db, Links
from sqlalchemy.exc import IntegrityError
from app.utils import short_generation


# saving original_url in database
def save_original_url(link, error=None):
    new_link = Links(original_url=link)
    try:
        db.session.add(new_link)
        db.commit()
    except IntegrityError:
        error = "Unable to add current link"

    db.session.close()
    return error


# adding short_url pair for original_url (call after function above)
def generate_and_save_short(link, error=None):
    founded_link = Links.query.filter_by(original_url=link).first()
    short_url = short_generation.generate_short_url(founded_link)

    founded_link.original_url = short_url
    db.session.commit()

    return short_url
