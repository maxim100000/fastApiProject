from sqlmodel import SQLModel
from app.schemas.cars import Car

class UserBase(SQLModel):
    id: int|None = None
    name: str|None = None
    email: str|None = None
    
class UserWithCars(UserBase):    
    cars: list[Car] = []
    
    