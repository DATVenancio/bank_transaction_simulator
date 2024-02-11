import requests as request_sender
import mysql.connector
class AccountInformation():
    def __init__(self,id_bank,account_number):
        self.id_bank = id_bank
        self.account_number=account_number
        self._access_public_database()

    def get_balance(self):
        url = self._get_bank_url(self.id_bank) + "/account_balance"
        parameters = {"account_number": self.account_number,
                      }
        response = request_sender.post(url,json=parameters)
        if response.status_code == 200:
            current_balance = response.json()
            return current_balance
        else:
            print(f"Error (Terminal): {response.status_code}")

    def _get_bank_url(self,id_bank):
        print(id_bank)
        self.db_cursor.execute("SELECT url FROM bank WHERE id_bank=(%s)",(id_bank,))
        for result in self.db_cursor:
            bank_url=result[0]
            return bank_url
    
    def _access_public_database(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="daniel",
            passwd="daniel",
            database="public_database"
        )
        self.db_cursor = self.db.cursor()