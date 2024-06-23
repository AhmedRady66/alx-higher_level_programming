#!/usr/bin/python3
"""List all states where name matches the argument safe from MySQL injections!"""

import MySQLdb
from sys import argv


if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )

    mycursor = db.cursor()

    sql = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    mycursor.execute(sql)
    query = mycursor.fetchall()
    for row in query:
        print(row)
    mycursor.close()
    db.close()
