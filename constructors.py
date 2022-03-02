from copyreg import constructor
from sqlalchemy import create_engine, Column, Integer, String, Date
from engine import Base

class Constructor(Base):
    __tablename__ = 'constructor'
    constructorId = Column(String(255), primary_key=True)
    url = Column(String(255))
    name = Column(String(255))
    nationality = Column(String(255))