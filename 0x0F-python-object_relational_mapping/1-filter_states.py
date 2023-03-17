#!/usr/bin/python3
"""This script lists all states with the name
starting with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def filter_states():
    """
    This function filters the states to show only states that begin with N
    """
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db = sys.argv[3]
    db = MySQLdb.connect(
        user=mysql_user,
        password=mysql_password,
        database=mysql_db)
    c = db.cursor()
    c.execute("SELECT * FROM states  WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)
    db.close()


if __name__ == "__main__":
    filter_states()
