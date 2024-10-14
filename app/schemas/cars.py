from sqlmodel import Field, SQLModel, Relationship, UniqueConstraint

from .links import CarsUsers
from .users import User

class Car(SQLModel, table=True):
    __table_args__ = (UniqueConstraint('name', 'brand', 'year'),)
    id: int|None = Field(default=None, primary_key=True)
    name: str
    brand: str
    year: int
    users: list[User] = Relationship(back_populates="cars",
                                      link_model=CarsUsers)