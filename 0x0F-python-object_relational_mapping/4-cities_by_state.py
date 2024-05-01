#!/usr/bin/python3
"""
Script that lists all `cities` from the database `hbtn_0e_4_usa`.
Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""

import sys
import MySQLdb

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)
    
    mySQL_u = sys.argv[1]
    mySQL_p = sys.argv[2] if len(sys.argv) > 2 else ''  # Use an empty string if no password provided
    db_name = sys.argv[3]

    # By default, it will connect to localhost:3306
    db = MySQLdb.connect(user=mySQL_u, passwd=mySQL_p, db=db_name, host='localhost', port=3306)
    cur = db.cursor()

    cur.execute("SELECT c.id, c.name, s.name \
                 FROM cities c INNER JOIN states s \
                 ON c.state_id = s.id \
                 ORDER BY c.id")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
