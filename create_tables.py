from commit import cmd
from engine import Base, engine
from constructors import Constructor
from drivers import Driver

if __name__ == "__main__":
    Base.metadata.create_all(engine)
