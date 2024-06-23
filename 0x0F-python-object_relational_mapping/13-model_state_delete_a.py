#!/usr/bin/python3
"""deletes all State objects with a name containing the letter a"""


from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    delete_state = session.query(State).filter(State.name.like('%a%')).all()
    for state in delete_state:
        session.delete(state)
    session.commit()
    session.close()
