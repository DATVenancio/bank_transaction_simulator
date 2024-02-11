#public db
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

#opposition_cards
db_cursor.execute("DELETE FROM opposition_cards")
db_cursor.execute("INSERT INTO opposition_cards (card_number) VALUES (%s)",("3131000000000006",))
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
db_cursor.execute("DELETE FROM bank_network")
db_cursor.execute("INSERT INTO bank_network (name,code,url) VALUES (%s,%s,%s)",("American Express","3","http://localhost:5011"))
db_cursor.execute("INSERT INTO bank_network (name,code,url) VALUES (%s,%s,%s)",("Visa","4","http://localhost:5012"))
db_cursor.execute("INSERT INTO bank_network (name,code,url) VALUES (%s,%s,%s)",("Mastercard","5","http://localhost:5013"))
#user
db_cursor.execute("DELETE FROM user")
db_cursor.execute("INSERT INTO user (name,age) VALUES (%s,%s)",("Daniel",22))


#account
db_cursor.execute("""
INSERT INTO account (id_user, balance, account_number,cvv)
VALUES (
    (SELECT id_user FROM user WHERE name = 'Daniel' ORDER BY id_user DESC LIMIT 1),
    100,
    '111111111119',
    '111'
)
""")

db.commit()


#___________________________________________________________________________

#credit mutuel
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="daniel",
    passwd="daniel",
    database="credit_mutuel"
)
db_cursor = db.cursor()

#bank
db_cursor.execute("DELETE FROM bank")
db_cursor.execute("INSERT INTO bank (id_bank,name,url) VALUES (%s,%s,%s)",("131","Crédit Agricole","http://localhost:5001"))
db_cursor.execute("INSERT INTO bank (id_bank,name,url) VALUES (%s,%s,%s)",("132","Crédit Mutuel","http://localhost:5002"))
db_cursor.execute("INSERT INTO bank (id_bank,name,url) VALUES (%s,%s,%s)",("970","La Banque Postale","http://localhost:5003"))


#issuer
db_cursor.execute("DELETE FROM bank_network")
db_cursor.execute("INSERT INTO bank_network (name,code,url) VALUES (%s,%s,%s)",("American Express","3","http://localhost:5011"))
db_cursor.execute("INSERT INTO bank_network (name,code,url) VALUES (%s,%s,%s)",("Visa","4","http://localhost:5012"))
db_cursor.execute("INSERT INTO bank_network (name,code,url) VALUES (%s,%s,%s)",("Mastercard","5","http://localhost:5013"))
#user
db_cursor.execute("DELETE FROM user")
db_cursor.execute("INSERT INTO user (name,age) VALUES (%s,%s)",("Fernando",22))

#account

db_cursor.execute("""
INSERT INTO account (id_user, balance, account_number,cvv)
VALUES (
    (SELECT id_user FROM user WHERE name = 'Fernando' ORDER BY id_user DESC LIMIT 1),
    100,
    '222222222229',
    '222'
)
""")




db.commit()