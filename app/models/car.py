from sqlmodel import SQLModel
from app.schemas.users import User 

class CarBase(SQLModel):
    id: int|None = None
    name: str|None = None
    brand: str|None = None
    year: int|None = None


class CarsWithUsers(CarBase):
    users: list[User] = []
    
    