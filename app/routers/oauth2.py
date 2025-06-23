from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, status
from .. import schemas, database, models, config
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
SECRET_KEY =f"{config.settings.secret_key}"
ALGORITHM = f"{config.settings.algorithm}"
EXPIRATION_TIME = f"{config.settings.access_token_expires_minutes}"
#secret key
#algorithm
#expiration time
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=int(EXPIRATION_TIME))
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception

        token_data = schemas.TokenData(id=f'{id}')
        return token_data
    
    except JWTError:
        raise credentials_exception
    


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    
    token_id = verify_access_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.id == token_id.id).first()

    return user
