import string
import random

ASCII_MAPPING = string.ascii_lowercase + string.digits
LENGTH = 7


def generate_short_url(original_url):
    short_url = "".join(random.choice(ASCII_MAPPING) for _ in range(LENGTH))
    return short_url
