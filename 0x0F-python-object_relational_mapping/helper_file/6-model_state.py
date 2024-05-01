#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
# mySQL_p = sys.argv[2] if len(sys.argv) > 2 else ''  # Use an empty string if no password provided

from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else '' , sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

