from bcrypt import hashpw, checkpw, gensalt


def verify_password(plain_password, hashed_password):
    return checkpw(password=plain_password.encode('utf-8')
                   , hashed_password=hashed_password)


def get_password_hash(password):
    return hashpw(password=password.encode('utf-8')
                  , salt=gensalt())
