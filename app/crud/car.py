from app.dependencies.common import Session
from sqlmodel import select
from app.schemas.cars import Car
from app.schemas.users import User
from app.models.car import CarsWithUsers, CarBase


def get_cars(session: Session, offset: int = None, limit: int = None,
             sort: str = ''):
    cars = session.exec(select(Car).offset(offset).limit(limit).order_by(
        getattr(Car, sort))).all()
    return cars


def insert_unique_cars(car: CarsWithUsers, session: Session):
    # noinspection PyTypeChecker
    car_db = session.exec(
        select(Car).where(Car.name == car.name,
                          Car.brand == car.brand,
                          Car.year == car.year)).one_or_none()
    if car_db:
        for user in car.users:
            # noinspection PyTypeChecker
            user_db = session.exec(
                select(User).where(User.email == user.email)).one_or_none()
            if not user_db:
                new_user = User.model_validate(user)
                car_db.users.append(new_user)
                session.add(car_db)
                session.commit()
                session.refresh(car_db)
        return car_db
    else:
        new_car = Car.model_validate(car)
        new_car.users = []
        session.add(new_car)
        session.commit()
        session.refresh(new_car)
        for user in car.users:
            # noinspection PyTypeChecker
            user_db = session.exec(
                select(User).where(User.email == user.email)).one_or_none()
            if user_db:
                new_car.users.append(user_db)
                session.add(new_car)
                session.commit()
                session.refresh(new_car)
            else:
                user = User.model_validate(user)
                new_car.users.append(user)
                session.add(new_car)
                session.commit()
        return new_car


def update_unique_car(id: int, car: CarBase, session: Session):
    car_db = session.get(Car, id)
    data = car.model_dump(exclude_unset=True)
    car_db.sqlmodel_update(data)
    session.add(car_db)
    session.commit()
    session.refresh(car_db)
    return car_db

def delete_unique_car(id: int, session: Session):
    car = session.get(Car, id)
    car.users = []
    session.delete(car)
    session.commit()
    return {'status': 'ok'}