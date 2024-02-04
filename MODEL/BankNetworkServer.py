#requests
from flask import Flask,jsonify
from flask import request as request_receiver
import requests as request_sender

#db
import mysql.connector


class BankNetworkServer:
    def __init__(self):
        
        db = mysql.connector.connect(
            host="localhost",
            user="daniel",
            passwd="daniel",
            database="bank_system"
        )
        self.db_cursor = db.cursor()


        app = Flask(__name__)
        @app.route('/treat_transaction',methods=["POST"])
        def treat_transaction():
            terminal_id_bank = request_receiver.json["terminal_id_bank"]
            terminal_account_number = request_receiver.json["terminal_account_number"]
            card_number = request_receiver.json["card_number"]
            amount = request_receiver.json["amount"]

            user_id_bank =self._get_bank_id(card_number)
            user_account_number = self._get_account_number(card_number)
            user_bank_url = self._get_bank_url(user_id_bank)

            terminal_bank_url = self._get_bank_url(terminal_id_bank)

            if(self._debit(user_bank_url,user_account_number,amount)):
                self._credit(terminal_bank_url,terminal_account_number,amount)

            return jsonify(True)
        app.run(port=5010,host="localhost",debug=True)

    def _get_bank_id(self,card_number):
        return card_number[1:4]

    def _get_account_number(self,card_number):
        return card_number[4:]

    def _get_bank_url(self,id_bank):
        self.db_cursor.execute("SELECT url FROM bank WHERE id_bank=(%s)",(id_bank,))
        for result in self.db_cursor:
            bank_url=result[0]
            return bank_url

    def _debit(self,bank_url,account_number,amount):
        data={"account_number":account_number,"amount":amount}
        bank_url = f"http://localhost:5000"
        response = request_sender.post(bank_url+"/debit",json=data)
        if response.status_code != 200:
            print(f"Error (debit): {response.status_code}")
            return False
        
        return response.json()

    def _credit(self,bank_url,account_number,amount):
        data={"account_number":account_number,"amount":amount}
        bank_url = f"http://localhost:5000"
        response = request_sender.post(bank_url+"/credit",json=data)
        if response.status_code != 200:
            print(f"Error (credit): {response.status_code}")
            return False
        
        return response.json()


server = BankNetworkServer()












"""


#api
app = Flask(__name__)
@app.route('/treat_transaction',methods=["POST"])
def treat_transaction():
    terminal_id_bank = request_receiver.json["terminal_id_bank"]
    terminal_account_number = request_receiver.json["terminal_account_number"]
    card_number = request_receiver.json["card_number"]
    amount = request_receiver.json["amount"]

    user_id_bank =_get_bank_id(card_number)
    user_account_number = _get_account_number(card_number)
    user_bank_url = _get_bank_url(user_id_bank)

    terminal_bank_url = _get_bank_url(terminal_id_bank)

    if(_debit(user_bank_url,user_account_number,amount)):
        _credit(terminal_bank_url,terminal_account_number,amount)

    return jsonify(True)





app.run(port=5010,host="localhost",debug=True)


"""


    