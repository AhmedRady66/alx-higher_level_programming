#!/usr/bin/python3
"""lists all State objects that contain the letter a"""

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    result = session.query(State, City).join(City).\
        filter(State.id == City.state_id).order_by(City.id)
    for state, city in result:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
