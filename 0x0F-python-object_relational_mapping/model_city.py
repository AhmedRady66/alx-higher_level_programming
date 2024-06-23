#!/usr/bin/python3
"""the class definition of a City and an instance Base = declarative_base()"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Define city table

    Attributes:
    id: integer
    name: string
    state_id: integer refer to the state table
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
