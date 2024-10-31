from sqlmodel import create_engine
from .settings import Settings

settings = Settings()

engine = create_engine(settings.url)



