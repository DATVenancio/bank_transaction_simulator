from crypt import methods
from flask import Flask,jsonify
from flask import request as request_receiver
import requests as request_sender


#db
import mysql.connector

class BankServer:
    def __init__(self):
        self._set_server_values_as_none()
        pass
    #abstract method to implement in child
    def _initial_server_configuration():
        raise NotImplementedError
    def _connect_db(self):
        print(self.db_host)
        print(self.db_user)
        print(self.db_passwd)
        print(self.db_name)
        self.db = mysql.connector.connect(
            host=self.db_host,
            user=self.db_user,
            passwd=self.db_passwd,
            database=self.db_name
        )
        self.db_cursor = self.db.cursor()
    def _create_api_routes(self):

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
            if(self._check_valid_debit(account_number,amount)):
                self._debit(account_number,amount)
                return jsonify(True)
            else:
                return jsonify(False)

        @app.route("/credit",methods=["POST"])
        def credit():
            account_number=request_receiver.json["account_number"]
            amount = request_receiver.json["amount"]
            if(self._check_valid_credit(account_number)):
                self._credit(account_number,amount)
                return jsonify(True)
            else:
                return jsonify(False)
        
        @app.route("/account_balance",methods=["POST"])
        def account_balance():
            account_number=request_receiver.json["account_number"]
            current_balance=self._account_balance(account_number)
            return jsonify(current_balance)

        app.run(port=self.api_port,host=self.api_host,debug=True)
  
    def _set_server_values_as_none(self):
        self.db_host = None
        self.db_user = None
        self.db_passwd = None
        self.db_name = None

        self.api_port = None
        self.api_host = None

    #internal functions
    def _check_valid_debit(self,account_number,amount):
        self.db_cursor.execute("SELECT balance FROM account WHERE account_number=(%s)",(account_number,))
        result = self.db_cursor.fetchone()
        if result[0]>=amount:
            return True
        return False
    def _check_valid_credit(self,account_number):
        self.db_cursor.execute("SELECT id_account FROM account WHERE account_number=(%s)",(account_number,))
        result = self.db_cursor.fetchone()

        if result != None:
            return True
        return False

    def _debit(self,account_number,amount):
        self.db_cursor.execute("SELECT balance FROM account WHERE account_number=(%s)",(account_number,))
        current_balance = self.db_cursor.fetchone()
        new_balance = current_balance[0]-amount
        self.db_cursor.execute("UPDATE account SET balance =(%s) WHERE account_number=(%s)",(new_balance,account_number))
        self.db.commit()

    def _credit(self,account_number,amount):
        self.db_cursor.execute("SELECT balance FROM account WHERE account_number=(%s)",(account_number,))
        current_balance = self.db_cursor.fetchone()
        new_balance = current_balance[0]+amount
        self.db_cursor.execute("UPDATE account SET balance =(%s) WHERE account_number=(%s)",(new_balance,account_number))
        self.db.commit()
    
    def _account_balance(self,account_number):
        self.db_cursor.execute("SELECT balance FROM account WHERE account_number=(%s)",(account_number,))
        current_balance = self.db_cursor.fetchone()
        return current_balance[0]


