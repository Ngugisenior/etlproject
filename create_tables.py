from engine import Base, engine
from constructors import Constructor

if __name__ == "__main__":
    Base.metadata.create_all(engine)
