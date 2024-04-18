from sqlalchemy.orm import Mapped, mapped_column, validates
from base import Base


class UserModel(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True,
                                    nullable=False, unique=True)
    
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False, unique=False)
    
    @validates("email")
    def validate_email(self, key, value):
        if "@" not in value:
            raise ValueError("Введите корректный email")
        if "." not in value:
            raise ValueError("Введите корректный email")
