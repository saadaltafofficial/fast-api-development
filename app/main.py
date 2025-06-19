from fastapi import FastAPI, HTTPException, status, Response, Depends
import psycopg
import time
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:
    try:
        conn = psycopg.connect(host='localhost', dbname='fastapi', user='postgres', password='Beenco.@123')
        cursor = conn.cursor()
        print("Database connection was sucessfull!")
        break
    except Exception as error:
        print("Connection issue with database")
        print('Error: ',error)
        time.sleep(6)


@app.get("/")
def root():
    return {"message": "welcome to my this api"}


@app.get("/posts", response_model=List[schemas.PostResponse])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts


@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model= schemas.PostResponse)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@app.get("/posts/{id}", response_model=schemas.PostResponse)
def get_post(id: int, db: Session = Depends(get_db)):
    
    post = db.query(models.Post).filter(models.Post.id == id).first()
 
    if not post:
       raise HTTPException(status_code=404, detail=f"post with id:{id} was not found")
    return post


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):

    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:
        raise HTTPException(status_code=404, detail=f"post with id:{id} was not found")
    
    post.delete(synchronize_session=False)
    db.commit()
   
    return Response(status_code=status.HTTP_204_NO_CONTENT) 


@app.put("/posts/{id}", response_model=schemas.PostResponse)
def update_post(id: int, updated_post: schemas.PostBase, db: Session = Depends(get_db)):       
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=404, detail=f"post with id:{id} was not found")
    
    post_query.update(updated_post.model_dump(),  synchronize_session=False)
    db.commit()


    return post_query.first()



@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(db: Session = Depends(get_db)):
    pass



