from sqlmodel import Session

def get_session() -> Session:
    from app.utils.database import engine
    with Session(engine) as session:
        yield session