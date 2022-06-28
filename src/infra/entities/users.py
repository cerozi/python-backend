from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.infra.config import Base

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    pets = relationship("Pets", back_populates="owner")

    def __repr__(self):
        return f'User <{self.name}>'