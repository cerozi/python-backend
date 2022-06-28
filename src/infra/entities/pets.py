import enum
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

from src.infra.config import Base

class AnimalTypes(enum.Enum):
    """ defining animal types """

    dog = "dog",
    cat = "cat",
    fish = "fish",
    turtle = "turtle"

class Pets(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    specie = Column(Enum(AnimalTypes), nullable=False)
    age = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("Users", back_populates="pets")

    def __repr__(self):
        return f'Pet <{self.name}> from <{self.owner}>'