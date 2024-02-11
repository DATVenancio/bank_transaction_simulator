import mysql.connector


#public database
db = mysql.connector.connect(
    host="localhost",
    user="daniel",
    passwd="daniel",
    database="public_database"
)
db_cursor = db.cursor()
db_cursor.execute("DROP TABLE IF EXISTS bank,opposition_cards")
db_cursor.execute("CREATE TABLE bank(id_bank VARCHAR(50) PRIMARY KEY, name VARCHAR(50), url VARCHAR(100))")
db_cursor.execute("CREATE TABLE opposition_cards(card_number VARCHAR(16) PRIMARY KEY)")

db.commit()

#credit agricole
db = mysql.connector.connect(
    host="localhost",
    user="daniel",
    passwd="daniel",
    database="credit_agricole"
)
db_cursor = db.cursor()
db_cursor.execute("DROP TABLE IF EXISTS bank,bank_network,user,account")
db_cursor.execute("CREATE TABLE bank(id_bank VARCHAR(50) PRIMARY KEY, name VARCHAR(50), url VARCHAR(100))")
db_cursor.execute("CREATE TABLE bank_network(id_bank_network int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), code VARCHAR(1) UNIQUE, url VARCHAR(100))")
db_cursor.execute("CREATE TABLE user(id_user int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), age INT)")
db_cursor.execute("CREATE TABLE account(id_account int PRIMARY KEY AUTO_INCREMENT, id_user int, balance FLOAT, account_number VARCHAR(12) UNIQUE, cvv VARCHAR(3), FOREIGN KEY (id_user) REFERENCES user(id_user))")
db.commit()

#credit mutuel
db = mysql.connector.connect(
    host="localhost",
    user="daniel",
    passwd="daniel",
    database="credit_mutuel"
)
db_cursor = db.cursor()
db_cursor.execute("DROP TABLE IF EXISTS bank,bank_network,user,account")
db_cursor.execute("CREATE TABLE bank(id_bank VARCHAR(50) PRIMARY KEY, name VARCHAR(50), url VARCHAR(100))")
db_cursor.execute("CREATE TABLE bank_network(id_bank_network int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), code VARCHAR(1) UNIQUE, url VARCHAR(100))")
db_cursor.execute("CREATE TABLE user(id_user int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), age INT)")
db_cursor.execute("CREATE TABLE account(id_account int PRIMARY KEY AUTO_INCREMENT, id_user int, balance FLOAT, account_number VARCHAR(12) UNIQUE, cvv VARCHAR(3), FOREIGN KEY (id_user) REFERENCES user(id_user))")
db.commit()

