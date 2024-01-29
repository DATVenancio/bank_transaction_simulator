import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="daniel",
    passwd="daniel"
)
db_cursor = db.cursor()
db_cursor.execute("CREATE DATABASE bank_system")
