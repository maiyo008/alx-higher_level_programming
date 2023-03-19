#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Create an engine to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create a configured class Session
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the first State object
    state = session.query(State).order_by(State.id).first()

    # Print the result or "Nothing" if the table is empty
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
