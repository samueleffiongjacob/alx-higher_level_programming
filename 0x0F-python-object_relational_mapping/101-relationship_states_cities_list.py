#!/usr/bin/python3
"""
Script that lists all `State` objects, and corresponding
`City` objects, contained in the database `hbtn_0e_101_usa`.
Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.engine.url import URL
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    mySQL_u = sys.argv[1]
    mySQL_p = sys.argv[2]
    db_name = sys.argv[3]
    port = 3306  # Specify the port

    # Construct the engine URL without using the URL constructor
    url = f"mysql+mysqldb://{mySQL_u}:{mySQL_p}@localhost:3306/{db_name}"

    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    states = session.query(State)

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
