from fastapi import FastAPI

from app.routers import users, cars
from app.utils.lifespan_events import lifespan
from app.utils.middleware import ProcessTimeMiddleware

app = FastAPI(lifespan=lifespan)

app.include_router(users.router)
app.include_router(cars.router)

app.add_middleware(ProcessTimeMiddleware)
