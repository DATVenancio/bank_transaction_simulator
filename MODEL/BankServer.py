from crypt import methods
from flask import Flask,jsonify
from flask import request as request_receiver
import requests as request_sender


#db
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="daniel",
    passwd="daniel",
    database="bank_system"
)
db_cursor = db.cursor()


#internal functions
def _check_valid_debit(account_number,amount):
    db_cursor.execute("SELECT balance FROM account WHERE account_number=(%s)",(account_number,))
    result = db_cursor.fetchone()
    if result[0]>=amount:
        return True
    return False



#api
app = Flask(__name__)
@app.route("/make_transaction",methods=["POST"])
def make_transaction():
    url = f"http://localhost:5010/treat_transaction"
    response = request_sender.post(url,json=request_receiver.json)
    if response.status_code == 200:
        data = response.json()
        #print(data)
    else:
        print(f"Error (BS): {response.status_code}")

    return(request_receiver.json)


@app.route("/debit",methods=["POST"])
def debit():
    account_number=request_receiver.json["account_number"]
    amount = request_receiver.json["amount"]
    if(_check_valid_debit(account_number,amount)):
        print("aceito")
    else:
        print("recusado")
    
    return ("True")



app.run(port=5000,host="localhost",debug=True)