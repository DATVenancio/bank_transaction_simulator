import requests
class Terminal:
    def __init__(self,bankAccount):
        self.bankAccount=bankAccount

    def start_transaction(self,card_number,amount):
        if(self._check_information(card_number)):
            self.__make_transaction(card_number,amount)
        


    def _check_information(self,card_number):
        #validade,pin,
        return True
    
    def __make_transaction(self,card_number,amount):
        url = f"http://localhost:5000/make_transaction"
        parameters = {"card_number": card_number,
                      "amount":amount}
        response = requests.post(url,json=parameters)
        if response.status_code == 200:
            data = response.json()
            #print(data)
        else:
            print(f"Error (Terminal): {response.status_code}")