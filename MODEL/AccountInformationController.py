from AccountInformation import AccountInformation
from AccountInformationFrontend import AccountInformationFrontend
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
    
