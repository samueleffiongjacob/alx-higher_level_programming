#!/usr/bin/python3
"""
Script that lists all `cities` in the `cities` table of `hbtn_0e_4_usa`
where the city's state matches the argument `state name`.
Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
    state name (str)
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        sys.exit(1)

    mySQL_u = sys.argv[1]
    mySQL_p = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    try:
        db = MySQLdb.connect(user=mySQL_u, passwd=mySQL_p, db=db_name, host='localhost', port=3306)
    except MySQLdb.Error as e:
        print("MySQL connection error:", e)
        sys.exit(1)

    # Create a cursor object
    cur = db.cursor()

    # Prepare the SQL query with parameterized values
    query = "SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"

    # Execute the query with the provided state name
    cur.execute(query, (state_name,))

    # Fetch all rows and print the city names
    rows = cur.fetchall()

    # print vertical
    # for row in rows:
    #     print(row[0])

    # Concatenate city names into a single string separated by commas
    city_names = ", ".join(row[0] for row in rows)
    print(city_names)
    # Close cursor and connection
    cur.close()
    db.close()
