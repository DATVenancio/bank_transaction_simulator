from Terminal import Terminal
from TerminalFrontend import TerminalFrontend
class TerminalController:
    def __init__(self):
        self.terminal_frontend = TerminalFrontend(self)
    
    def start_screen(self):
        self.terminal_frontend.mainloop()
    def login(self,bank_code,account_number):
        self.terminal = Terminal(bank_code,account_number)
    
    def receive_form_information(self,card_number,amount,cvv):
        result_message =self.terminal.make_transaction(card_number,amount,cvv)
        return result_message
