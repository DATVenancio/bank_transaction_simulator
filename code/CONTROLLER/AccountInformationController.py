import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #put the 'code' directory in the syspath
from MODEL.AccountInformation import AccountInformation
from VIEW.AccountInformationFrontend import AccountInformationFrontend
class AccountInformationController:
    def __init__(self):
        self.account = None
        self.account_frontend = AccountInformationFrontend(self)
    
    def start_screen(self):
        self.account_frontend.mainloop()
    
    def login(self,bank_code,account_number):
        self.account = AccountInformation(bank_code,account_number)

    def get_balance(self):
        return self.account.get_balance()
    
