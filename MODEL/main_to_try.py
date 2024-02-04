import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="daniel",
    passwd="daniel",
    database="bank_system"
)
db_cursor = db.cursor()
db_cursor.execute("SELECT id_account FROM account WHERE account_number=(%s)",(account_number,))
result = db_cursor.fetchone()
print(result[0])

