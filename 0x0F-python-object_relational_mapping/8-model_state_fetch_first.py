#!/usr/bin/python3
"""
list the first State object from a database
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State



if __name__ == "__main__":
    import sys
    # Database connection information
    username = sys.argv[1]
    password = sys.argv[2] if len(sys.argv) > 2 else '' # Use an empty string if no password provided
    database = sys.argv[3]
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
    first_state = session.query(State).order_by(State.id).first()
    if first_state is not None:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
    session.close()
