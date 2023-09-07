from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Tenant(Base):
    __tablename__ = "tenants"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    house_id = Column(Integer, ForeignKey("houses.id"))
    house =relationship("House", back_populates="tenant")

def __init__(self, first_name, last_name,house_id):
        self.first_name = first_name
        self.last_name = last_name
        self.house_id=house_id
        


def houses(self):
      return self.houses

def caretakers(self):
      return self.caretakers
       

      

def __repr__(self):
      return f"Tenant('{self.first_name}', '{self.last_name}')"

    