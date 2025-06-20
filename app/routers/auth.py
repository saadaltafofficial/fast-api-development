from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils
from . import oauth2

router = APIRouter( tags= ['Authentication'])

@router.post('/login')
def login(user_credentials: schemas.UserLogin, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == user_credentials.username).first()

    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials")
    
    #create token
    #return token
    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return {'access_token': access_token, "token_type": "bearer"}
    
