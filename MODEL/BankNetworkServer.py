#requests
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
def _get_bank_id(card_number):
    return card_number[1:4]

def _get_account_number(card_number):
    return card_number[4:]

def _get_bank_url(id_bank):
    db_cursor.execute("SELECT url FROM bank WHERE id_bank=(%s)",(id_bank,))
    for result in db_cursor:
        bank_url=result[0]
        return bank_url

def _debit(bank_url,account_number,amount):
    data={"account_number":account_number,"amount":amount}
    bank_url = f"http://localhost:5000/debit"
    response = request_sender.post(bank_url,json=data)
    if response.status_code != 200:
        print(f"Error (debit): {response.status_code}")
        
    



#api
app = Flask(__name__)
@app.route('/treat_transaction',methods=["POST"])
def treat_transaction():
    card_number = request_receiver.json["card_number"]
    amount = request_receiver.json["amount"]

    id_bank =_get_bank_id(card_number)
    account_number = _get_account_number(card_number)
    bank_url = _get_bank_url(id_bank)

    _debit(bank_url,account_number,amount)



    return jsonify(bank_url)





app.run(port=5010,host="localhost",debug=True)
    