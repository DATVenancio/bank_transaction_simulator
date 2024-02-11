import tkinter as tk

class TerminalFrontend(tk.Tk):
    def __init__(self,terminal_controller):
        super().__init__()
        self.terminal_controller = terminal_controller

        self.result_message=""
        
        self.title("Frontend Python")
        self.geometry("400x400")
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

        tk.Button(button_frame, text="Pattern 01",command=self.first_login_entry_pattern).pack(side=tk.LEFT)
        tk.Button(button_frame, text="Pattern 02",command=self.second_login_entry_pattern).pack(side=tk.LEFT)
        
        
    def show_transaction_screen(self):
        
        if self.current_screen:
            self.current_screen.destroy()
        
        self.current_screen = tk.Frame(self)
        self.current_screen.pack(expand=True, fill="both")
        
        tk.Label(self.current_screen, text=f"BANK CODE: {self.bank_code}").pack()
        tk.Label(self.current_screen, text=f"ACCOUNT NUMBER: {self.account_number}").pack()
        
        tk.Label(self.current_screen, text="Amount:").pack()
        self.amount_entry = tk.Entry(self.current_screen)
        self.amount_entry.pack()
        
        tk.Label(self.current_screen, text="Card number:").pack()
        self.card_number_entry = tk.Entry(self.current_screen)
        self.card_number_entry.pack()
        
        tk.Label(self.current_screen, text="CVV:").pack()
        self.cvv_entry = tk.Entry(self.current_screen)
        self.cvv_entry.pack()
        
        tk.Button(self.current_screen, text="Enviar", command=self.submit_form).pack()

        extra_frame = tk.Frame(self.current_screen)
        extra_frame.pack(pady=10)  

        self.result_frame = tk.Frame(self.current_screen)
        self.result_frame.pack(pady=40)

        self.result_label = tk.Label(self.result_frame, text=self.result_message, font=("Arial", 10), bg="lightgray")
        self.result_label.pack(expand=True, fill="both")

        button_frame = tk.Frame(self.current_screen)
        button_frame.pack()

        tk.Button(button_frame, text="Pattern 01",command=self.first_entry_pattern).pack(side=tk.LEFT)
        tk.Button(button_frame, text="Pattern 02",command=self.second_entry_pattern).pack(side=tk.LEFT)
        tk.Button(button_frame, text="Pattern 03",command=self.third_entry_pattern).pack(side=tk.LEFT)
    
    def validate_entry(self):
        self.bank_code = self.bank_code_entry.get()
        self.account_number = self.account_number_entry.get()

        self.terminal_controller.login(self.bank_code,self.account_number)

        self.show_transaction_screen()

        
    def submit_form(self):
        amount = float(self.amount_entry.get())
        card_number = self.card_number_entry.get()
        cvv = self.cvv_entry.get()
        self.result_message=""
        self.result_message=self.terminal_controller.receive_form_information(card_number,amount,cvv)
        self.show_transaction_screen()

    def first_login_entry_pattern(self):
        self.bank_code_entry.insert(0,131)
        self.account_number_entry.insert(0,111111111119)


    def second_login_entry_pattern(self):
        self.bank_code_entry.insert(0,132)
        self.account_number_entry.insert(0,222222222229)

    def first_entry_pattern(self):
        self.amount_entry.insert(0,1)
        self.card_number_entry.insert(0,3131111111111119)
        self.cvv_entry.insert(0,1234)

    def second_entry_pattern(self):
        self.amount_entry.insert(0,2)
        self.card_number_entry.insert(0,4132222222222229)
        self.cvv_entry.insert(0,1234)
    
    def third_entry_pattern(self):
        self.amount_entry.insert(0,10)
        self.card_number_entry.insert(0,3131000000000000)
        self.cvv_entry.insert(0,1234)