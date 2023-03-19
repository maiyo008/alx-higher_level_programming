#!/usr/bin/python3
"""This script takes in
the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def filter_cities():
    """This function connects to the database and lists all the cities of the
    state added as an input argument by the user
    """
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_user,
        password=mysql_password,
        database=mysql_db)
    c = db.cursor()
    query = "SELECT cities.name FROM cities\
    JOIN states ON cities.state_id = states.id\
    WHERE states.name = %s\
    ORDER BY cities.id ASC;"
    num_rows = c.execute(query, (state_name,))
    rows = c.fetchall()
    i = 1
    for row in rows:
        print(row[0], end='')
        if (i < num_rows):
            print(end=', ')
        i += 1
    print()
    db.close()


if __name__ == "__main__":
    filter_cities()
