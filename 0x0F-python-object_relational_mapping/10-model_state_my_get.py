#!/usr/bin/python3
"""
Script that prints the State object with
the name passed as argument from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == '__main__':
    # create the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()

    # query the database for the state with the given name
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # if the state exists, print its id
    if state:
        print(state.id)
    else:
        print("Not found")
