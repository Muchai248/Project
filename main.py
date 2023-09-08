from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.Caretaker import Caretaker
from models.House import House
from models.Tenant import Tenant
from models.base import Base
import argparse
DATABASE_URI='sqlite:///caretaker_house_tenant.db'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(bind=engine)

# tenant1 = session.query(Tenant). filter_by(first_name="April").first()
# if not tenant1:
#     tenant1=Tenant(first_name="April", last_name="Wanja",house_id=1)

house1 =session.query(House). filter_by(house_number="B1").first()
#  if not house1:
#     house1=House(house_number="B1")
#     session.add(house1)
#     session.commit()
#     house1.add_caretaker(session=session)
#     print(house1.house_number)
    
#     # print(house1.add_caretaker)

#     house1.add_tenants(session=session)

parser = argparse.ArgumentParser(description="Simple tenant List Manager")
parser.add_argument("-u", "--add", help="Add a tenant to the tenant list")
parser.add_argument("-l", "--list", action="store_true", help="List all tenants")
args = parser.parse_args()


#  test cases.
if args.add:
    house1.add_tenants(args.add)
elif args.list:
    print(house1.house_number())
else: 
    print("No valid command issued.")


# caretaker1 = session.query(Caretaker). filter_by(owner_name="Obare").first()
# if not caretaker1:
#     caretaker1=Caretaker(owner_name="Obare",house_id=1)

# if tenant1 not in session:
#     session.add(tenant1)
if house1 not in session:
   session.add(house1)
# # if caretaker1 not in session:
# #     session.add(caretaker1)
#     session.commit()



session.close()