import psycopg
import time
from .database import engine
from . import models
from fastapi import FastAPI
from .routers import posts, users, auth


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


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "welcome to my this api"}
