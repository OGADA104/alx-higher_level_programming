#!/usr/bin/python3
import MySQLdb
import sys
"""print states from db"""


def select_states(mysql_username, mysql_password, database_name):
    """select states function"""
    try:
        db = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=mysql_username,
                passwd=mysql_password,
                db=database_name,
                charset="utf8")
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY states.id ASC")
        states = cur.fetchall()
        return states
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
    finally:
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    """run if main script"""
    args = sys.argv
    mysql_username = args[1]
    mysql_password = args[2]
    database_name = args[3]
    states = select_states(mysql_username, mysql_password, database_name)
    for state in states:
        print(state)
