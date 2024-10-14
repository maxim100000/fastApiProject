from typing import Annotated

from fastapi import APIRouter, Depends

from app.crud.user import get_users, insert_unique_user, update_unique_user, \
    delete_unique_user
from app.dependencies.common import get_session, Session
from app.schemas.users import User
from app.models.user import UserWithCars, UserBase
from app.authentications.users import pass_basic_credentials

router = APIRouter(prefix='/users')


@router.get("/", response_model=list[UserWithCars])
async def get_all(session: Annotated[Session, Depends(get_session)],
                  credentials_ok: Annotated[
                      bool, Depends(pass_basic_credentials)],
                  offset: int = 0, limit: int = 100, sort: str = 'id'):
    return get_users(session, offset=offset, sort=sort,
                     limit=limit) if credentials_ok else None


@router.get("/{id}", response_model=UserWithCars)
async def get_user(id: int, session: Annotated[Session, Depends(get_session)]):
    return session.get(User, id)


@router.post("/", response_model=UserWithCars)
async def create_user(user: UserWithCars,
                      session: Annotated[Session, Depends(get_session)]):
    return insert_unique_user(user, session)


@router.patch("/{id}", response_model=UserWithCars)
async def update_user(id: int, user: UserBase,
                      session: Annotated[Session, Depends(get_session)]):
    return update_unique_user(id, user, session)


@router.delete("/{id}")
async def delete_car(session: Annotated[Session, Depends(get_session)],
                     id: int):
    return delete_unique_user(id, session)
