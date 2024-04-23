from .database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class Post(Base):
    __tablename__ ="post_data"
    
    id = Column(Integer, primary_key=True, nullable=False)
    What_is_your_gender = Column(String, nullable=False)
    How_old_are_you = Column(Integer, nullable=False)
    What_do_you_own = Column(String, nullable=False)
    Are_you_married = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    

