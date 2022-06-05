import hashlib


def hash_unicode(password_string):
    """
    Hash a password using sha 256.
    :param password_string: string
    :return: string
    """
    return hashlib.sha256(password_string.encode('utf-8')).hexdigest()
