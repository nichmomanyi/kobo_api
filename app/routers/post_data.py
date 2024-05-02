from fastapi import FastAPI, status, Depends, APIRouter
from .. import models, schemas
from ..database import engine, get_db
from sqlalchemy.orm import Session



router = APIRouter(
    tags=["Data upload"]
)



@router.post("/new_data", status_code=status.HTTP_201_CREATED)
def create_user(post: schemas.Data, db: Session = Depends(get_db)):
    new_data = models.Post(**post.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data 

@router.get("/data", status_code=status.HTTP_200_OK)
def get_data(get: schemas.all_data, db: Session = Depends(get_db)):
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data 