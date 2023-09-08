from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .Tenant import Tenant
from models.Caretaker import Caretaker
from .base import Base


class House(Base):
    __tablename__ = 'houses'
    id = Column(Integer, primary_key=True)
    house_number=Column(Integer)
    caretaker = relationship("Caretaker", back_populates="house")
    tenant = relationship("Tenant", back_populates="house")
    


    def __init__(self,house_number):
       self.house_number=house_number
    #    self.add_caretaker

    def houses(self):
       return self.houses
    

    def add_tenants(self,session):
       tenant=Tenant(first_name="April",last_name="Wanja", house_id=self.id)
       self.tenant.append(tenant)
       session.add(tenant)
       session.commit()


    def add_caretaker(self,session):
       caretaker=Caretaker(owner_name="Obare",house_id=self.id)
       self.caretaker.append(caretaker)
       session.add(caretaker)
       session.commit()


