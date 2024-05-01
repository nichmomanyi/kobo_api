from fastapi import FastAPI, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import post_data

app = FastAPI()

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)



app.include_router(post_data.router)



# @app.post("/new_data", status_code=status.HTTP_200_OK)
# def create_user(post: schemas.Data, db: Session = Depends(get_db)):
#     new_data = models.Post(**post.dict())
#     db.add(new_data)
#     db.commit()
#     db.refresh(new_data)
#     return new_data  

