from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .Tenant import Tenant


class Caretaker(Base):
    __tablename__ = 'caretakers'
    id = Column(Integer, primary_key=True)
    owner_name = Column(String)
    # tenant_id= Column(Integer, ForeignKey("tenants.id"))
    house_id = Column(Integer, ForeignKey("houses.id"))
    house = relationship("House", back_populates="caretaker")
  


    def __init__(self,owner_name,house_id):
        self.owner_name = owner_name
        self.house_id = house_id
    

    # def add_tenant(self):
    #     self.tenant = Tenant(self.first_name)
    #     self.tenant.add_house(self.house)
    #     self.house.add_caretaker(self.tenant)
    #     return self.tenant
    
    def house_instance(self):
        return self.house
    


    

 
