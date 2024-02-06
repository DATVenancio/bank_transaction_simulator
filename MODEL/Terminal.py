import requests
import mysql.connector
class Terminal:
    def __init__(self,id_bank,account_number):
        self.id_bank = id_bank
        self.account_number=account_number

        self._access_public_database()
        
    
    def start_transaction(self,card_number,amount):
        if(self._check_information(card_number)):
            self.__make_transaction(card_number,amount)
        


    def _check_information(self,card_number):
        #validade,pin,
        return True
    
    def __make_transaction(self,card_number,amount):
        card_id_bank =  self._get_bank_id(card_number)
        url = self._get_bank_url(card_id_bank)
        parameters = {"terminal_id_bank":self.id_bank,
                      "terminal_account_number": self.account_number,
                      "card_number": card_number,
                      "amount":amount}
        response = requests.post(url,json=parameters)
        if response.status_code == 200:
            data = response.json()
            #print(data)
        else:
            print(f"Error (Terminal): {response.status_code}")
    
    def _access_public_database(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="daniel",
            passwd="daniel",
            database="public_database"
        )
        self.db_cursor = self.db.cursor()

    def _get_bank_id(self,card_number):
        return card_number[1:4]
    
    def _get_bank_url(self,id_bank):
        self.db_cursor.execute("SELECT url FROM bank WHERE id_bank=(%s)",(id_bank,))
        for result in self.db_cursor:
            bank_url=result[0]
            return bank_url



