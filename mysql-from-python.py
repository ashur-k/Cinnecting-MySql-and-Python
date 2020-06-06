import os
import datetime
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

    #with connection.cursor() as cursor:
        # sql = 'SELECT * From Artist limit 5;'
        # cursor.execute(sql)
        # result = cursor.fetchall()
        # print(result)

    #run a query to get output in dict

    #with connection.cursor(pymysql.cursors.DictCursor) as cursor:  # pymysql.cursors.DictCursor following in arguments converts return output to dictionar, its handy as dict format is similar to json
        #sql = "SELECT * from Genre;"
        #cursor.execute(sql)
        #for row in cursor:
            #print (row)
        
    #Create the table

    #with connection.cursor() as cursor:
        #cursor.execute('''CREATE TABLE IF NOT EXISTS
                        #Friends(name char(20), age int, DOB datetime);''')

    #Insert data to table
    
    #with connection.cursor() as cursor:
        #row = ("Bob", 21, "1990-02-06 23:04:56")
        #cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s)", row)
        #connection.commit()
    
    #Insert many rows

    #with connection.cursor() as cursor:
        #rows = [("Bob", 23, "1990-02-06 23:04:56"),
                #("Jim", 24, "1955-05-12 13:12:45"),
               #("Fred", 25, "1911-09-12 01:01:01")]
        #cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s)", rows)
        #connection.commit()

     #Update rows

    #with connection.cursor() as cursor:
        #cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'Bob';")
        #connection.commit()

    #Alternative Update rows method

    #with connection.cursor() as cursor:
        #cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;", (23, 'Bob'))
        #connection.commit()

    #Update Many rows

   #with connection.cursor() as cursor:
        #rows = [(24, 'Bob'),
                #(25, 'JIM'),
                #(26, 'Fred')]
        #cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;", rows)
        #connection.commit()

    #Delete Rows

    #with connection.cursor() as cursor:
        #rows = cursor.execute("DELETE FROM Friends WHERE name = 'Bob';")
        #connection.commit()

    
    #Alternate Delete Rows using String Interpolation

    #with connection.cursor() as cursor:
        #rows = cursor.execute("DELETE FROM Friends WHERE name = %s;", 'Fred')
        #connection.commit()

    #Delete Many Rows

    #with connection.cursor() as cursor:
        #rows = cursor.executemany("DELETE FROM Friends WHERE name = %s;", ['Bob', 'Jim'])
        #connection.commit()

    #Delete Where

    #with connection.cursor() as cursor:
        #rows = cursor.execute("DELETE FROM Friends WHERE name in ('Jim', 'Bob')")
        #connection.commit()

    #Delete Multiple rows where

    #with connection.cursor() as cursor:
        #names = ['Jim', 'Bob']
        #rows = cursor.execute("DELETE FROM Friends WHERE name in (%s, %s)", names)
        #connection.commit()

    #Power of Python(i have executes some commands at python terminal)

    with connection.cursor() as cursor:
        list_of_names = ['fred','Fred']
        # Prepare a string with the same number of placeholders as in list_of_names
        format_strings = ",".join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({})".format(format_strings), list_of_names)
        connection.commit()


finally:
    #close the connection, regardless of whetter the above was succesfull
    connection.close()
