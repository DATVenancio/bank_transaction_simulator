import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="daniel",
    passwd="daniel",
    database="bank_system"
)
db_cursor = db.cursor()
db_cursor.execute("DROP TABLE IF EXISTS bank,issuer,user,account")
db_cursor.execute("CREATE TABLE bank(id_bank VARCHAR(50) PRIMARY KEY, name VARCHAR(50), url VARCHAR(100))")
db_cursor.execute("CREATE TABLE issuer(id_issuer int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), code VARCHAR(1))")
db_cursor.execute("CREATE TABLE user(id_user int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), age INT)")
db_cursor.execute("CREATE TABLE account(id_account int PRIMARY KEY AUTO_INCREMENT, id_user int, balance DECIMAL, account_number VARCHAR(12) UNIQUE, FOREIGN KEY (id_user) REFERENCES user(id_user))")
db.commit()
