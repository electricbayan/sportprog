from sqlalchemy.engine import URL
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from base import Base
from models.user import UserModel

from config import postgres_url


engine = create_engine(
    url=postgres_url,
    echo=True
)


session = sessionmaker(engine)

def create_all_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

