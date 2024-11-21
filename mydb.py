# refer to logs in notion under HOA OC DATABASE CRM APP tab !
# logs from video as reference
#	- install mysql on pc
#	- pip install mysql
#	- pip install mysql-connector
#	- pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'wh3ret#eyw8765.',

	)

# cursor object
cursorObject = dataBase.cursor()

# creation of database
cursorObject.execute("CREATE DATABASE hoa_oc_db")

print("yippee!")
