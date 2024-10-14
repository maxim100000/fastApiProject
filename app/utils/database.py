from sqlmodel import create_engine
from .settings import Settings
import os

settings = Settings()

engine = create_engine(settings.url)



