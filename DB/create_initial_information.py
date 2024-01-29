import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="daniel",
    passwd="daniel",
    database="bank_system"
)
db_cursor = db.cursor()

#bank
db_cursor.execute("DELETE FROM bank")
db_cursor.execute("INSERT INTO bank (name,identifier) VALUES (%s,%s)",("Crédit Agricole","131"))
db_cursor.execute("INSERT INTO bank (name,identifier) VALUES (%s,%s)",("Crédit Mutuel","132"))
db_cursor.execute("INSERT INTO bank (name,identifier) VALUES (%s,%s)",("La Banque Postale","970"))
db_cursor.execute("INSERT INTO bank (name,identifier) VALUES (%s,%s)",("LCL","972"))
db_cursor.execute("INSERT INTO bank (name,identifier) VALUES (%s,%s)",("Société Générale","973"))
db_cursor.execute("INSERT INTO bank (name,identifier) VALUES (%s,%s)",("BNP","974"))
db_cursor.execute("INSERT INTO bank (name,identifier) VALUES (%s,%s)",("Caisse d'Épargne","978"))
db_cursor.execute("INSERT INTO bank (name,identifier) VALUES (%s,%s)",("La BRED","975"))

#issuer
db_cursor.execute("DELETE FROM issuer")
db_cursor.execute("INSERT INTO issuer (name,code) VALUES (%s,%s)",("American Express","3"))
db_cursor.execute("INSERT INTO issuer (name,code) VALUES (%s,%s)",("Visa","4"))
db_cursor.execute("INSERT INTO issuer (name,code) VALUES (%s,%s)",("Mastercard","3"))

#user
db_cursor.execute("DELETE FROM user")
db_cursor.execute("INSERT INTO user (name,age) VALUES (%s,%s)",("Daniel",22))
db_cursor.execute("INSERT INTO user (name,age) VALUES (%s,%s)",("Fernando",22))


db.commit()