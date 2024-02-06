#credit agricole
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="daniel",
    passwd="daniel",
    database="public_database"
)
db_cursor = db.cursor()

#bank
db_cursor.execute("DELETE FROM bank")
db_cursor.execute("INSERT INTO bank (id_bank,name,url) VALUES (%s,%s,%s)",("131","Crédit Agricole","http://localhost:5001"))
db_cursor.execute("INSERT INTO bank (id_bank,name,url) VALUES (%s,%s,%s)",("132","Crédit Mutuel","http://localhost:5002"))
db_cursor.execute("INSERT INTO bank (id_bank,name,url) VALUES (%s,%s,%s)",("970","La Banque Postale","http://localhost:5003"))
db.commit()

#___________________________________________________________________________

#credit agricole
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="daniel",
    passwd="daniel",
    database="credit_agricole"
)
db_cursor = db.cursor()

#bank
db_cursor.execute("DELETE FROM bank")
db_cursor.execute("INSERT INTO bank (id_bank,name,url) VALUES (%s,%s,%s)",("131","Crédit Agricole","http://localhost:5001"))
db_cursor.execute("INSERT INTO bank (id_bank,name,url) VALUES (%s,%s,%s)",("132","Crédit Mutuel","http://localhost:5002"))
db_cursor.execute("INSERT INTO bank (id_bank,name,url) VALUES (%s,%s,%s)",("970","La Banque Postale","http://localhost:5003"))


#issuer
db_cursor.execute("DELETE FROM issuer")
db_cursor.execute("INSERT INTO issuer (name,code) VALUES (%s,%s)",("American Express","3"))
db_cursor.execute("INSERT INTO issuer (name,code) VALUES (%s,%s)",("Visa","4"))
db_cursor.execute("INSERT INTO issuer (name,code) VALUES (%s,%s)",("Mastercard","3"))

#user
db_cursor.execute("DELETE FROM user")
db_cursor.execute("INSERT INTO user (name,age) VALUES (%s,%s)",("Daniel",22))
db_cursor.execute("INSERT INTO user (name,age) VALUES (%s,%s)",("Fernando",22))

#account
db_cursor.execute("""
INSERT INTO account (id_user, balance, account_number)
VALUES (
    (SELECT id_user FROM user WHERE name = 'Daniel' ORDER BY id_user DESC LIMIT 1),
    100,
    '11111111'
)
""")
db_cursor.execute("""
INSERT INTO account (id_user, balance, account_number)
VALUES (
    (SELECT id_user FROM user WHERE name = 'Fernando' ORDER BY id_user DESC LIMIT 1),
    100,
    '22222222'
)
""")

db.commit()