from .database import engine
from . import models, config
from fastapi import FastAPI
from .routers import posts, users, auth, vote



models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "welcome to my this api"} 
