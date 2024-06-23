#!/usr/bin/python3
"""List all states"""

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
    mycursor.execute("SELECT * FROM states ORDER BY states.id")
    query = mycursor.fetchall()
    for row in query:
        print(row)
    mycursor.close()
    db.close()
