from sqlalchemy import Integer, String, Column
from database import Base

class Trip(Base):
  __tablename__ = 'trip'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True)
  price_confort = Column(String, index=True)
  price_economy = Column(String, index=True)
  city = Column(String, index=True)
  duration = Column(String, index=True)
  seat = Column(String, index=True)
  bed = Column(String, index=True)