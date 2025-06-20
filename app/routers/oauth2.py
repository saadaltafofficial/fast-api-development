import jwt
from datetime import datetime, timedelta

SECRET_KEY = "woi52u3059203jhpiaejp0o2tju351029erw3ret2q4562346tgdu4573547357357gdhffyw34623466ju"
ALGORITHM = "HS256"
EXPIRATION_TIME = 30
#secret key
#algorithm
#expiration time
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=EXPIRATION_TIME)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt