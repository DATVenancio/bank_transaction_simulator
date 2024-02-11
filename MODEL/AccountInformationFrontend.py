import tkinter as tk
class AccountInformationFrontend(tk.Tk):
    def __init__(self,account_controller):
        super().__init__()
        self.accoun_controller = account_controller
        self.bank_code = None
        self.account_number = None
        self.balance = None
        self.title("Frontend Python")
        self.geometry("400x300")
        self.current_screen = None
        
        
        self.show_login_screen()
        
        
    def show_login_screen(self):
        
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = tk.Frame(self)
        self.current_screen.pack(expand=True, fill="both")
        
        tk.Label(self.current_screen, text="Bank Code:").pack()
        self.bank_code_entry = tk.Entry(self.current_screen)
        self.bank_code_entry.pack()
        
        tk.Label(self.current_screen, text="Account Number:").pack()
        self.account_number_entry = tk.Entry(self.current_screen)
        self.account_number_entry.pack()
        
        
        tk.Button(self.current_screen, text="LOGIN", command=self.validate_entry).pack()
        extra_frame = tk.Frame(self.current_screen)
        extra_frame.pack(pady=10)  
        test_label = tk.Label(self.current_screen, text="TESTS")
        test_label.pack()

        button_frame = tk.Frame(self.current_screen)
        button_frame.pack()

        tk.Button(button_frame, text="Pattern 01",command=self.first_entry_pattern).pack(side=tk.LEFT)
        tk.Button(button_frame, text="Pattern 02",command=self.second_entry_pattern).pack(side=tk.LEFT)
    
    def show_information_screen(self):
        
        if self.current_screen:
            self.current_screen.destroy()
        
        self.current_screen = tk.Frame(self)
        self.current_screen.pack(expand=True, fill="both")
        
        tk.Label(self.current_screen, text=f"Código do Banco: {self.bank_code}").pack()
        tk.Label(self.current_screen, text=f"Número da Conta: {self.account_number}").pack()
        tk.Label(self.current_screen, text=f"BALANCE: {self.balance}").pack()
        
        tk.Button(self.current_screen, text="Refresh", command=self.refresh_information).pack()

    def validate_entry(self):
        self.bank_code = self.bank_code_entry.get()
        self.account_number = self.account_number_entry.get()

        self.accoun_controller.login(self.bank_code,self.account_number)
        self.balance = self.accoun_controller.get_balance()

        self.show_information_screen()


    def refresh_information(self):
        self.balance = self.accoun_controller.get_balance()
        self.show_information_screen()
    
    def first_entry_pattern(self):
        self.bank_code_entry.insert(0,131)
        self.account_number_entry.insert(0,111111111119)


    def second_entry_pattern(self):
        self.bank_code_entry.insert(0,132)
        self.account_number_entry.insert(0,222222222229)
