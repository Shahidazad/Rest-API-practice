
import hmac
import user
# from user import User



def authenticate(username,password):
    user=user.User.find_by_username(username)
    if user and hmac.compare_digest(user.password, password):


        return user

def identity(payload):
    user_id=payload['identity'] 
    return user.User.find_by_id(user_id)
    