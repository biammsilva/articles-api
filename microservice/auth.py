import hashlib
from datetime import datetime

from microservice.models import User, UserAuth

def new_user_authentication(user):
    if UserAuth.objects(user=user, logged_in=1, date=datetime.today()).order_by('-id').first():
        return False
    hash = hashlib.sha224((user.email + user.password + str(datetime.now())).encode("utf-8")).hexdigest()
    user_auth = UserAuth(user = user, date = datetime.now(), logged_in = 1, hash = hash).save()
    return user_auth.hash

def authenticate_user(auth_hash):
    user_auth = UserAuth.objects(hash=auth_hash).first()
    if user_auth:
        return datetime.now().date() == user_auth.date.date() and bool(user_auth.logged_in)
    return False

def logout(auth_hash):
    user_auth = UserAuth.objects(hash=auth_hash).order_by('-id').first()
    if user_auth:
        user_auth.logout()
        return True
    return False
