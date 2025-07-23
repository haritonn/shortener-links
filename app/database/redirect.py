from app.database.db import db, Links, redis_client
from app.utils import short_generation
import logging

# basic config to logger
logging.basicConfig(level=logging.INFO)


# trying to find in cache/mysql, else generating new and returning itself
def generate_and_save_pair(link, error=None):
    short_url = None

    # 1. searching in cache
    if redis_client.get(link) is not None:
        short_url = redis_client.get(link)
        logging.info("Using redis cache")
        return short_url, error

    # 2. searching in database
    if (
        db.session.query(Links.shorter_url).filter_by(original_url=link).first()
        is not None
    ):
        short_url = (
            db.session.query(Links.shorter_url).filter_by(original_url=link).first()[0]
        )
        logging.info("Not found in cache, found in mysql")

        # again adding in redis cache
        redis_client.set(link, short_url, ex=600)

        return short_url, error

    # 3. adding in cache & database
    short_url = short_generation.generate_short_url(link)
    logging.info("Not found, generating new...")

    try:
        # db
        new_link = Links(
            original_url=link, shorter_url=short_url, user_id=1
        )  # user_id=1 as placeholder, should be fixed further
        db.session.add(new_link)
        db.session.commit()

        # cache
        redis_client.set(link, short_url, ex=600)  # will hold in cache for 10 minutes

    except Exception as e:
        logging.warning(f"Some error occured: {e}")
        error = "Unknown error occured, please try later"

    return short_url, error
