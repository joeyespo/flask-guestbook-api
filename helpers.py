import hashlib


def gravatar_for(email):
    email_hash = hashlib.md5(email.lower()).hexdigest()
    return 'http://www.gravatar.com/avatar/' + email_hash
