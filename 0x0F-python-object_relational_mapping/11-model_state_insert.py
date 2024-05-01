#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
    - script takes 3 arguments: mysql username, mysql password and databasename
    - uses the module SQLAlchemy
    - imports State and Base from model_state
    - script should connect to a MySQL server running on localhost at port 3306
    Print the new states.id after creation
"""

if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    # Database connection information
    username = argv[1]
    password = argv[2] if len(argv) > 2 else '' # Use an empty string if no password provided
    database = argv[3]
    hostname = 'localhost'
    port = 3306


    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database, hostname, port))
    Session = sessionmaker(bind=engine)
    s = Session()

    new_state = State(name="Louisiana")
    s.add(new_state)
    s.commit()
    print(new_state.id)
