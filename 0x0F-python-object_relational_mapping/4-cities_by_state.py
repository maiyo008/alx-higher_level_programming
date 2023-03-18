#!/usr/bin/python3
"""This script lists all cities from the database by states
"""
import MySQLdb
import sys


def cities_by_states():
    """
    This function connects to mysql database and lists all cities by states
    """
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db = sys.argv[3]
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_user,
        password=mysql_password,
        database=mysql_db)
    c = db.cursor()
    query = "SELECT cities.id, cities.name, states.name\
    FROM cities\
    JOIN states ON cities.state_id = states.id\
    ORDER BY cities.id ASC;"
    c.execute(query)
    rows = c.fetchall()
    for row in rows:
        print(row)
    db.close()


if __name__ == "__main__":
    cities_by_states()
