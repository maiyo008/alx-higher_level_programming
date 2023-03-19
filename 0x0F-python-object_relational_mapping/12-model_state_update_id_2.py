#!/usr/bin/python3
"""Changes the name of a State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Create a new Engine instance
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Get the State object with id = 2
    state = session.query(State).filter_by(id=2).first()

    # If the state exists, update its name
    if state:
        state.name = 'New Mexico'
        session.commit()

    # Close the session
    session.close()
