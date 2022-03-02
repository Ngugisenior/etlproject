import imp
from commit import cmd
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base

engine = create_engine(
    "sqlite:///Racing.db"
)

session = Session(engine)
Base = declarative_base()
os.system(cmd)