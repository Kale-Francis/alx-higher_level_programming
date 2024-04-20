#!/usr/bin/python3

"""Module that lists all states from the hbtn_0e_0_usa database."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials and state name from command-line arguments
    # and Connect to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    # Execute the SQL query to retrieve cities in the specified state
    query = ("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    c.execute(query)

    # Fetch all rows and filter cities by the specified state
    # and Print the cities separated by commas
    print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == sys.argv[4]]))


