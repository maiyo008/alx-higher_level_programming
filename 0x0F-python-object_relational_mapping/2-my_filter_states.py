#!/usr/bin/python3
"""This script takes in an argument and displays all the values in the states
table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys


def my_filter_states():
    """
    This function shows states that match the state provided as an input arg
    """
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db = sys.argv[3]
    query_name = sys.argv[4]
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_user,
        password=mysql_password,
        database=mysql_db)
    c = db.cursor()
    c.execute(
        "SELECT * FROM states WHERE name LIKE BINARY \
        '{}' ORDER BY id ASC".format(query_name)
    )
    rows = c.fetchall()
    for row in rows:
        print(row)
    db.close()


if __name__ == "__main__":
    my_filter_states()
