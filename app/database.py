from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@ipaddress/hostname"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:nichdee254@localhost/kobo_data_api"



engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()