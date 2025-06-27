from .database import engine
from . import models, config
from fastapi import FastAPI
from .routers import posts, users, auth, vote
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Welcome to my first complete backend project and I'm so happy to deploy it and share it with you, let me know if you think I have to add something. I will definately consider it. Thanks"} 
