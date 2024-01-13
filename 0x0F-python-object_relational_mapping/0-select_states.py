#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    mysql_username = args[1]
    mysql_password = args[2]
    database_name = args[3]

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
