#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
    - Your script should take 3 arguments: mysql username, mysql password
    and database name
    - uses the module SQLAlchemy
    - imports State and Base from model_state
    - script connects to a MySQL server running on localhost at port 3306
    - Results are sorted in ascending order by states.id
"""

if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    # Database connection information
    username = sys.argv[1]
    # Use an empty string if no password provided
    password = sys.argv[2] if len(sys.argv) > 2 else ''
    database = sys.argv[3]
    hostname = 'localhost'
    port = 3306

    # Create the engine

    engine = create_engine(
        'mysql+mysqldb://{}:{}@{}:{}/{}'.format(
            username, password, hostname, port, database
        )
    )

    Session = sessionmaker(bind=engine)
    s = Session()

    for row in s.query(State).order_by(State.id.asc()):
        print(row.id, end="")
        print(': ', end="")
        print(row.name)

    # Close the session
    s.close()
