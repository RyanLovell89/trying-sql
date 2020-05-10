import os
import datetime
import pymysql

username = os.getenv('USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM Friends WHERE name in ('jim', 'bob')")
        connection.commit()
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()