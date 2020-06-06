import os
import pymysql

#Get username from Cloud9 workspace
# modify this variable if runnin on another environment

username = os.getenv('C9_USER')

#Connect to the dabase
connection = pymysql.connect(host='localhost', 
                             user=username,
                             password='',
                             db='Chinook')

try:
    #run a query
    with connection.cursor() as cursor:
        sql = 'SELECT * From Artist limit 5;'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #close the connection, regardless of whetter the above was succesfull
    connection.close()
