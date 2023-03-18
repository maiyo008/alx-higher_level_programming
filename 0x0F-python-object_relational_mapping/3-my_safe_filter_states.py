#!/usr/bin/python3
"""This script takes in an argument and displays all the values in the states
table of hbtn_0e_0_usa where name matches the argument
but safe from SQL injection
"""
import MySQLdb
import sys


def my_safe_filter_states():
    """
    This function shows states that match the state provided as an input arg
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
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    c.execute(query, (state_name + "%", ))
    rows = c.fetchall()
    for row in rows:
        print(row)
    db.close()


if __name__ == "__main__":
    my_safe_filter_states()
