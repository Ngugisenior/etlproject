import os
from sqlalchemy import create_engine, Column, Integer, String, Date
from engine import Base
from commit import cmd

class Driver(Base):
    __tablename__ = 'driver'
    driverId = Column(String(255), primary_key=True)
    url = Column(String(255))
    givenName = Column(String(255))
    familyName = Column(String(255))
    dateOfBirth = Column(Date)
    nationality = Column(String(255))

os.system(cmd)