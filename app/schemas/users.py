from sqlmodel import Field, SQLModel, Relationship, UniqueConstraint 

from .links import CarsUsers


class User(SQLModel, table=True):
    __table_args__ = (UniqueConstraint('email'),) 
    id: int|None = Field(default=None, primary_key=True)
    name: str 
    email: str
    cars: list['Car'] = Relationship(back_populates="users",
                                     link_model=CarsUsers)