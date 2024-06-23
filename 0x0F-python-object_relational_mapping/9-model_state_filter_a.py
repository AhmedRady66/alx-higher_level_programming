#!/usr/bin/python3
"""lists all State objects that contain the letter a"""

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
    result = session.query(State).order_by(State.id).filter(
        State.name.like('%a%'))
    for i in result:
        print(f"{i.id}: {i.name}")
    session.close()
