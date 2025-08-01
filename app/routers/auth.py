from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils
from . import oauth2

router = APIRouter( tags= ['Authentication'])

@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == user_credentials.username).first()

    if user == None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Invalid credentials")
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f"Invalid credentials")
    
    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return {'access_token': access_token, "token_type": "bearer"} 
    
