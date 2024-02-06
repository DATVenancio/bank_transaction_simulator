from Terminal import Terminal
from TerminalFrontend import TerminalFrontend
class TerminalController:
    def __init__(self,bank_code,account_number):
        self.terminal = Terminal(bank_code,account_number)
        self.terminal_frontend = TerminalFrontend(self,bank_code,account_number)
    
    def start_screen(self):
        self.terminal_frontend.mainloop()
    
    def receive_form_information(self,card_number,amount,pin):
        self.terminal.start_transaction(card_number,amount)
