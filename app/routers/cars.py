from typing import Annotated

from fastapi import APIRouter, Depends

from app.crud.car import insert_unique_cars, get_cars, update_unique_car, \
    delete_unique_car
from app.dependencies.common import get_session, Session
from app.models.car import CarsWithUsers, CarBase
from app.schemas.cars import Car
from app.authentications.cars import get_token, pass_token

router = APIRouter(prefix='/cars')


@router.post('/token')
async def login(token: Annotated[str, Depends(get_token)]):
    return {'access_token': token, 'token_type': 'bearer'}


@router.get("/", response_model=list[CarsWithUsers], dependencies=[Depends(pass_token)])
async def get_all(session: Annotated[Session, Depends(get_session)],
                  offset: int = 0, limit: int = 100, sort: str = 'id'):
    return get_cars(session, offset=offset, limit=limit, sort=sort) 



@router.get("/{id}", response_model=CarsWithUsers)
async def get_car(id: int, session: Annotated[Session, Depends(get_session)]):
    return session.get(Car, id)


@router.post("/", response_model=CarsWithUsers)
async def create_car(user: CarsWithUsers,
                     session: Annotated[Session, Depends(get_session)]):
    return insert_unique_cars(user, session)


@router.patch("/{id}", response_model=CarsWithUsers)
async def update_car(id: int, car: CarBase,
                     session: Annotated[Session, Depends(get_session)]):
    return update_unique_car(id, car, session)


@router.delete("/{id}")
async def delete_car(session: Annotated[Session, Depends(get_session)],
                     id: int):
    return delete_unique_car(id, session)
