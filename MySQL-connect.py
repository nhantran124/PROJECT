import mysql.connector
from psutil import users
mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    passwd = "12345"
)

my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE our_users")
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)




