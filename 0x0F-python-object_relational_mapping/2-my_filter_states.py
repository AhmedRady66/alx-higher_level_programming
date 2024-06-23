#!/usr/bin/python3
"""List all states"""

import MySQLdb
from sys import argv


if __name__ == "__main__":

    script = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )

    mycursor = script.cursor()
    searched = argv[4]

    sql = "SELECT * FROM states WHERE states.name LIKE %s ORDER BY states.id"
    mycursor.execute(sql, (searched,))
    query = mycursor.fetchall()
    for row in query:
        print(row)
    mycursor.close()
    script.close()
