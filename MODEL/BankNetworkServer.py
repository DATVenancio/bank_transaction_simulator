#requests
from flask import Flask,jsonify
from flask import request as request_receiver
import requests as request_sender

#db
import mysql.connector


class BankNetworkServer:
    def __init__(self):
        self._set_server_values_as_none()
        self.result_to_return = {"result_message":" ",}
    def _connect_db(self):
        self.db = mysql.connector.connect(
            host=self.db_host,
            user=self.db_user,
            passwd=self.db_passwd,
            database=self.db_name
        )
        self.db_cursor = self.db.cursor()

    def _create_api_routes(self):
        app = Flask(__name__)
        @app.route('/treat_transaction',methods=["POST"])
        def treat_transaction():
            terminal_id_bank = request_receiver.json["terminal_id_bank"]
            terminal_account_number = request_receiver.json["terminal_account_number"]
            card_number = request_receiver.json["card_number"]
            amount = request_receiver.json["amount"]
            cvv = request_receiver.json["cvv"]

            user_id_bank =self._get_bank_id(card_number)
            user_account_number = self._get_account_number(card_number)
            user_bank_url = self._get_bank_url(user_id_bank)

            terminal_bank_url = self._get_bank_url(terminal_id_bank)

            if(self._debit(user_bank_url,user_account_number,amount,cvv)):
                self._credit(terminal_bank_url,terminal_account_number,amount)
                self.result_to_return["result_message"]="transaction accepted"
            else:
                self.result_to_return["result_message"]="transaction refused"
            
            return jsonify(self.result_to_return)

        app.run(port=self.api_port,host="localhost",debug=True)
    def _initial_server_configuration():
        raise NotImplementedError
    
    def _set_server_values_as_none(self):
        self.db_host = None
        self.db_user = None
        self.db_passwd = None
        self.db_name = None

        self.api_port = None
        self.api_host = None

    def _get_bank_id(self,card_number):
        return card_number[1:4]

    def _get_account_number(self,card_number):
        return card_number[4:]

    def _get_bank_url(self,id_bank):
        self.db_cursor.execute("SELECT url FROM bank WHERE id_bank=(%s)",(id_bank,))
        for result in self.db_cursor:
            bank_url=result[0]
            return bank_url

    def _debit(self,bank_url,account_number,amount,cvv):
        data={"account_number":account_number,"amount":amount,"cvv":cvv}
        response = request_sender.post(bank_url+"/debit",json=data)
        if response.status_code != 200:
            print(f"Error (debit): {response.status_code}")
            return False
        return response.json()

    def _credit(self,bank_url,account_number,amount):
        data={"account_number":account_number,"amount":amount}
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


    