
from sqlalchemy import create_engine, true
from sqlalchemy.orm import sessionmaker
from models.Caretaker import Caretaker
from models.House import House
from models.Tenant import Tenant
from models.base import Base

DATABASE_URI='sqlite:///caretaker_house_tenant.db'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(bind=engine)

# tenant1 = session.query(Tenant). filter_by(first_name="April").first()
# if not tenant1:
#     tenant1=Tenant(first_name="April", last_name="Wanja",house_id=1)


    # house1.add_caretaker(session=session)
    # print(house1.house_number)
    # print(house1.add_caretaker)
    # house1.add_tenants(session=session)

def add_house(session):
          house_number=input("Enter house number: ")
          house=House(house_number=house_number)
          session.add(house)
          session.commit()

def house1():
 house_number=input("Enter house no.")
 house1 =session.query(House). filter_by(house_number="B1").first()
 if  house1:
      house1.menu(session=session)

def results():
  while True:
    print("1.view menu")
    print("2.add house")
    print("3.exit")
    choice=int(input("Enter choice: "))
    if choice==1:
      house1()
    elif choice==2:
      add_house(session=session)
    elif choice ==3:
       break
    else:
      print("invalid choice")

results()



# caretaker1 = session.query(Caretaker). filter_by(owner_name="Obare").first()
# if not caretaker1:
#     caretaker1=Caretaker(owner_name="Obare",house_id=1)

# if tenant1 not in session:
#     session.add(tenant1)
# if house1 not in session:
#    session.add(house1)
session.commit()
# # if caretaker1 not in session:
# #     session.add(caretaker1)
#     session.commit()



session.close()