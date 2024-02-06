import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="daniel",
    passwd="daniel"
)
db_cursor = db.cursor()
#credit agricole
db_cursor.execute("DROP DATABASE IF EXISTS credit_agricole")
db_cursor.execute("CREATE DATABASE credit_agricole")

db_cursor.execute("DROP DATABASE IF EXISTS public_database")
db_cursor.execute("CREATE DATABASE public_database")


db.commit()
