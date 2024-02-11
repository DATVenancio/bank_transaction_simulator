import requests
import mysql.connector
class Terminal:
    def __init__(self,id_bank,account_number):
        self.id_bank = id_bank
        self.account_number=account_number
        self.result_message=""
        self._access_public_database()
        
    
    def make_transaction(self,card_number,amount,cvv):
        if(self._check_information(card_number)):
            self._start_transaction(card_number,amount,cvv)
            
        return self.result_message
        


    def _check_information(self,card_number):
        if(self._luhn_validation(card_number)):
            if(self._in_opposition(card_number)==False):
                return True
        return False
    
    def _luhn_validation(self,card_number):
        if len(card_number) != 16 or not card_number.isdigit():
            self.result_message = "invalid card number"
            return False
        digits = [int(digit) for digit in card_number]
        for i in range(len(digits) - 2, -1, -2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9
        total = sum(digits)
        if(total % 10 == 0):
            return True
        self.result_message = "invalid card number"
        return False
        
    def _in_opposition(self,card_number):
        self.db_cursor.execute("SELECT * FROM opposition_cards WHERE card_number=(%s)",(card_number,))
        result=self.db_cursor.fetchone()
        if(result==None):
            return False
        self.result_message = "card in opposition"
        return True

    def _start_transaction(self,card_number,amount,cvv):
        card_id_bank =  self._get_bank_id(card_number)
        url = self._get_bank_url(card_id_bank)+"/start_transaction"
        parameters = {"terminal_id_bank":self.id_bank,
                      "terminal_account_number": self.account_number,
                      "card_number": card_number,
                      "amount":amount,
                      "cvv":cvv}
        response = requests.post(url,json=parameters)
        if response.status_code == 200:
            self.result_message=response.json()["result_message"]
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



