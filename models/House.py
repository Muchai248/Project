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
       first_name= input("Enter firstname: " )
       last_name=input("Enter lastname: ")
       tenant=Tenant(first_name=first_name,last_name=last_name, house_id=self.id)
       self.tenant.append(tenant)
       session.add(tenant)
       session.commit()


    def add_caretaker(self,session):
       owner_name=input("Enter name: ")
       caretaker=Caretaker(owner_name=owner_name,house_id=self.id)
       self.caretaker.append(caretaker)
       session.add(caretaker)
       session.commit()

    def delete_tenant(self,session):
        id=int(input("Enter id: "))
        for tenant in self.tenant:
            if tenant.id==id:
              session.delete(tenant)
              session.commit()

    def update_tenant(self,session):
        house_number=input("Enter House no. : ")
        for tenant in self.tenant:
            if tenant.house_number==house_number:
              first_name=input("Enter firstname: ")
              last_name=input("Enter lastname: ")
              tenant.first_name=first_name
              tenant.last_name=last_name
              session.update(tenant)
              session.commit()


    def list_tenants(self):
       for tenant in self.tenant:
           print(tenant.first_name,tenant.last_name)
     
    def list_caretaker(self):
       for caretaker in self.caretaker:
           print(caretaker.owner_name)

    def list_house(self,session):
      houses=session.query(House)
      for house in houses:
          print(house.house_number)

    def menu(self,session):
     while True:
      print("1.add tenant")
      print("2.add caretaker")
      print("3.list tenant")
      print("4.list house")
      print("5.list caretaker")
      print("6.delete tenant")
      print("7.update tenant")
      print("8.exit")
      choice=int(input("Enter choice:"))
      if choice==1:
           self.add_tenants(session=session)
      elif choice==2:
           self.add_caretaker(session=session)
      elif choice==3:
           self.list_tenants()
      elif choice==4:
           self.list_house(session=session)
      elif choice==5:
           self.list_caretaker()
      elif choice==6:
           self.delete_tenant(session=session)
      elif choice==7:
          self.update_tenant(session=session)
      elif choice==8:
          break
      else:
          print("Invalid choice")
      


         


