from sqlalchemy.engine import URL
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from src.base import Base
from src.models.user import UserModel

from src.config import postgres_url


engine = create_engine(
    url=postgres_url,
    echo=True
)

session = Session(bind=engine)

def create_all_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

