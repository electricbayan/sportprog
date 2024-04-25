from sqlalchemy.orm import Mapped, mapped_column, validates
from src.base import Base


class TaskModel(Base):
    __tablename__ = "tasks"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False, unique=True)
    
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    desc: Mapped[str] = mapped_column(unique=True, nullable=False)
    time: Mapped[str] = mapped_column(nullable=True, unique=False)
    
    input: Mapped[str] = mapped_column(nullable=False, unique=True)
    output: Mapped[str] = mapped_column(nullable=False, unique=True)
    
    examplein: Mapped[str] = mapped_column(nullable=False, unique=False)
    exampleout: Mapped[str] = mapped_column(nullable=False, unique=True)
    
    rating_level: Mapped[int] = mapped_column(nullable=False, unique=False)
