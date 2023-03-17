#!/usr/bin/python3
"""Script to list all states by their order of id"""
import MySQLdb
import sys


def list_states():
    """
    Function to list all the states by the order of their ids
    """
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db = sys.argv[3]
    db = MySQLdb.connect(
        user=mysql_user,
        password=mysql_password,
        database=mysql_db)
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)
    db.close()


if __name__ == "__main__":
    list_states()
