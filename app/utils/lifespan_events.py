from contextlib import asynccontextmanager
from time import perf_counter

@asynccontextmanager
async def lifespan(app):
    print('lifespan start')
    start = perf_counter()
    yield
    stop = perf_counter() - start
    print(f'lifespan stop: {stop}')