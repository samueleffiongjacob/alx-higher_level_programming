#!/usr/bin/python3
"""
changes the name of the State object where id=2 to New Mexico from a database
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    # Database connection information
    username = argv[1]
    password = argv[2] if len(argv) > 2 else '' # Use an empty string if no password provided
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
    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()
    session.close()
