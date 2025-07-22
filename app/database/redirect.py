from app.database.db import db, Links
from sqlalchemy.exc import IntegrityError
from app.utils import short_generation
import logging


# generate and save original_url - short_url pair
def generate_and_save_pair(link, error=None):
    short_url = None

    try:
        short_url = short_generation.generate_short_url(link)
        new_link = Links(
            original_url=link, shorter_url=short_url, user_id=1
        )  # user_id=1 is filler value, should be changed further
        db.session.add(new_link)
        db.session.commit()

    except IntegrityError:
        logging.warning("IntegrityError: this link already exists in database")
        short_url = (
            db.session.query(Links.shorter_url).filter_by(original_url=link).scalar()
        )

    except Exception as e:
        error = f"Some error occured: {e}"
        logging.exception("Error in generate_and_save_pair")

    finally:
        db.session.close()
        return short_url, error
