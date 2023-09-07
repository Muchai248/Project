from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


class Caretaker(Base):
    __tablename__ = 'caretakers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    tenant_id= Column(Integer, ForeignKey("tenants.id"))
    house_id = Column(Integer, ForeignKey("houses.id"))
    tenant = relationship("tenant", back_populates="caretaker")
    house = relationship("house", back_populates="caretaker")


    def __init__(self,owner_name, tenant, house):
        self.owner_name = owner_name
        self.tenant = tenant
        self.house = house


    def tenant_instance(self):
        return self.tenant
    
    def house_instance(self):
        return self.house


    

 
