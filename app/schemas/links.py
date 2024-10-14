from sqlmodel import Field, SQLModel 

class CarsUsers(SQLModel, table=True):
    id: int = Field(primary_key=True)
    car_id: int = Field(foreign_key="car.id")
    user_id: int = Field(foreign_key="user.id")