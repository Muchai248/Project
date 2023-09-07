from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.Caretaker import caretaker
from .base import Base


class House(Base):
    __tablename__ = 'houses'
    id = Column(Integer, primary_key=True)
    house_number=Column(Integer)
    caretaker = relationship("Caretaker", back_populates="house")


def __init__(self,house_number):
    self.house_number=house_number

def houses(self):
      return self.houses

def caretakers(self):
      return self.caretakers


