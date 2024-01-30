import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="daniel",
    passwd="daniel",
    database="bank_system"
)
db_cursor = db.cursor()
db_cursor.execute("SELECT balance FROM account WHERE account_number=(%s)",("222222222222",))
result = db_cursor.fetchone()
print(result[0])



teste="123456789012"
print(teste[4:])