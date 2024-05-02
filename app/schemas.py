from pydantic import BaseModel



class BaseData(BaseModel):
    What_is_your_gender: str
    How_old_are_you: int 
    What_do_you_own: str 
    Are_you_married: str 
    
class Data(BaseData):
    class Config():
        orm_mode = True
        
class all_data(BaseData):
    class Config():
        orm_mode = True