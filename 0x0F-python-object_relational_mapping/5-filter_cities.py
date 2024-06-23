#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities"""

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
    mycursor.execute("SELECT cities.id, cities.name FROM cities\
                     JOIN states ON cities.state_id = states.id\
                     WHERE states.name = %s", [argv[4]])
    query = mycursor.fetchall()
    empty_list = []
    for row in query:
        empty_list.append(row[1])
    print(", ".join(empty_list))
    mycursor.close()
    db.close()
