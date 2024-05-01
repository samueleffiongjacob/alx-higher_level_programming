#!/usr/bin/python3
"""
list all State objects that contain the letter a from a database
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":

    # Database connection information
    username = argv[1]
    # Use an empty string if no password provided
    password = argv[2] if len(argv) > 2 else ''
    database = argv[3]
    hostname = 'localhost'
    port = 3306

    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username,
                                                                    password,
                                                                    database,
                                                                    hostname,
                                                                    port))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    s = '%a%'
    states = session.query(State).filter(State.name.like(s)).order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
