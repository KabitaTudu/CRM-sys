import mysql.connector
from decouple import config

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = config('DBPWD'),
    auth_plugin = 'mysql_native_password'
  )

# cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE CRMDB")

print("CRMDB created!")