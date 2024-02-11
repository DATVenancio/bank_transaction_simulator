import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #put the 'code' directory in the syspath
from MODEL.Terminal import Terminal
from VIEW.TerminalFrontend import TerminalFrontend
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
