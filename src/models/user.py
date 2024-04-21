from sqlalchemy.orm import Mapped, mapped_column, validates
from src.base import Base
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True,
                                    nullable=False, unique=True)
    
    nickname: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(unique=False)
    
    
    def set_hash_password(self, password):
        self.hashed_password = generate_password_hash(password=password)
        
    def check_hash_password(self, password):
        return check_password_hash(self.hashed_password, password=password)
