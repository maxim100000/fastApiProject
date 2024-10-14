from app.dependencies.common import Session
from sqlmodel import select
from app.schemas.cars import Car
from app.schemas.users import User
from app.models.user import UserWithCars, UserBase


def get_users(session: Session, offset: int = None, limit: int = None,
                  sort: str = ''):
    users = session.exec(select(User).offset(offset).limit(limit).order_by(
        getattr(User, sort))).all()
    return users


def insert_unique_user(user: UserWithCars, session: Session):
    # noinspection PyTypeChecker
    user_db = session.exec(
        select(User).where(User.email == user.email)).one_or_none()
    if user_db:
        for car in user.cars:
            # noinspection PyTypeChecker
            car_db = session.exec(select(Car).where(Car.name == car.name,
                                                    Car.brand == car.brand,
                                                    Car.year == car.year)).one_or_none()
            if not car_db:
                new_car = Car.model_validate(car)
                user_db.cars.append(new_car)
                session.add(user_db)
                session.commit()
                session.refresh(user_db)
        return user_db
    else:
        new_user = User.model_validate(user)
        new_user.cars = []
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        for car in user.cars:
            # noinspection PyTypeChecker
            car_db = session.exec(select(Car).where(Car.name == car.name,
                                                    Car.brand == car.brand,
                                                    Car.year == car.year)).one_or_none()
            if car_db:
                new_user.cars.append(car_db)
                session.add(new_user)
                session.commit()
                session.refresh(new_user)
            else:
                car = Car.model_validate(car)
                new_user.cars.append(car)
                session.add(new_user)
                session.commit()
                session.refresh(new_user)
        return new_user


def update_unique_user(id: int, user: UserBase, session: Session):
    user_db = session.get(User, id)
    data = user.model_dump(exclude_unset=True)
    user_db.sqlmodel_update(data)
    session.add(user_db)
    session.commit()
    session.refresh(user_db)
    return user_db

def delete_unique_user(id: int, session: Session):
    user = session.get(User, id)
    user.cars = []
    session.delete(user)
    session.commit()
    return {'status': 'ok'}