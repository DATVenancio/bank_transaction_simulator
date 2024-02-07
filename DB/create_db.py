import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="daniel",
    passwd="daniel"
)
db_cursor = db.cursor()
#public database
db_cursor.execute("DROP DATABASE IF EXISTS public_database")
db_cursor.execute("CREATE DATABASE public_database")

#credit agricole
db_cursor.execute("DROP DATABASE IF EXISTS credit_agricole")
db_cursor.execute("CREATE DATABASE credit_agricole")

#credit mutuel
db_cursor.execute("DROP DATABASE IF EXISTS credit_mutuel")
db_cursor.execute("CREATE DATABASE credit_mutuel")

#credit mutuel
db_cursor.execute("DROP DATABASE IF EXISTS american_express")
db_cursor.execute("CREATE DATABASE american_express")


db.commit()
