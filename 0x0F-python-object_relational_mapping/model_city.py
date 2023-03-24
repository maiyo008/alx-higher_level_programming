#!/usr/bin/python3
"""This file contains the class definition of
a City and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """Inherits from Base
    Links to the cities table
    Initializes attributes
        id: maps id column in cities table
        name: maps name column in cities table
        state_id: maps state_id column in cities table
        and is a foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
