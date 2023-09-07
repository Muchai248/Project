from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.Caretaker import Caretaker
from models.House import House
from models.Tenant import Tenant
from models.base import Base

DATABASE_URI='sqlite:///caretaker_house_tetant.db'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(bind=engine)

tenant1 = session.query(Tenant). filter_by(first_name="April").first()
if not tenant1:
    tenant1=Tenant(first_name="April", last_name="Wanja")
