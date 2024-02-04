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
def _check_valid_credit(account_number):
    db_cursor.execute("SELECT id_account FROM account WHERE account_number=(%s)",(account_number,))
    result = db_cursor.fetchone()

    if result != None:
        return True
    return False

def _debit(account_number,amount):
    db_cursor.execute("SELECT balance FROM account WHERE account_number=(%s)",(account_number,))
    current_balance = db_cursor.fetchone()
    new_balance = current_balance[0]-amount
    db_cursor.execute("UPDATE account SET balance =(%s) WHERE account_number=(%s)",(new_balance,account_number))
    db.commit()

def _credit(account_number,amount):
    db_cursor.execute("SELECT balance FROM account WHERE account_number=(%s)",(account_number,))
    current_balance = db_cursor.fetchone()
    new_balance = current_balance[0]+amount
    db_cursor.execute("UPDATE account SET balance =(%s) WHERE account_number=(%s)",(new_balance,account_number))
    db.commit()


#api
app = Flask(__name__)
@app.route("/start_transaction",methods=["POST"])
def start_transaction():
    url = f"http://localhost:5010/treat_transaction"
    response = request_sender.post(url,json=request_receiver.json)
    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error (BS): {response.status_code}")

    return(request_receiver.json)


@app.route("/debit",methods=["POST"])
def debit():
    account_number=request_receiver.json["account_number"]
    amount = request_receiver.json["amount"]
    if(_check_valid_debit(account_number,amount)):
        _debit(account_number,amount)
        return jsonify(True)
    else:
        return jsonify(False)

@app.route("/credit",methods=["POST"])
def credit():
    account_number=request_receiver.json["account_number"]
    amount = request_receiver.json["amount"]
    if(_check_valid_credit(account_number)):
        _credit(account_number,amount)
        return jsonify(True)
    else:
        return jsonify(False)


app.run(port=5000,host="localhost",debug=True)