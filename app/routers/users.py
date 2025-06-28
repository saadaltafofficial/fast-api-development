from .. import models, schemas, utils
from sqlalchemy.orm import Session
from fastapi import  HTTPException, status, Depends, APIRouter
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    find_user = db.query(models.User).filter(models.User.email == user.email or models.User.username == user.username)

    if find_user.first() != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user already exists")

    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.id == id).first()

    if user == None:
        raise HTTPException(status_code=404, detail=f"user with id:{id} was not found")
    
    return user 