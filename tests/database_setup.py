from app.main import app
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, create_engine, Session

from app.dependencies.common import get_session

engine = create_engine("sqlite:///tests/test.db")

if __name__ != '__main__':
    SQLModel.metadata.create_all(engine)

def get_temp_session():
    with Session(engine) as session:
        yield session

app.dependency_overrides[get_session] = get_temp_session

client = TestClient(app)