from fastapi import FastAPI, status, Depends
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session



models.Base.metadata.create_all(engine)


app = FastAPI()

# @app.post('/test_data')
# def create(db: Session = Depends(get_db)):
#     return {"status": "Succesfully created"}

@app.post("/new_data", status_code=status.HTTP_200_OK)
def create_user(post: schemas.Data, db: Session = Depends(get_db)):
    new_data = models.Post(**post.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data  

