import tkinter as tk

class TerminalFrontend(tk.Tk):
    def __init__(self,terminal_controller,bank_code,account_number):
        super().__init__()
        self.terminal_controller = terminal_controller
        self.bank_code = bank_code
        self.account_number = account_number
        
        self.title("Frontend Python")
        self.geometry("400x300")
        self.current_screen = None
        
        
        self.show_screen()
        
        
    def show_screen(self):
        
        if self.current_screen:
            self.current_screen.destroy()
        
        self.current_screen = tk.Frame(self)
        self.current_screen.pack(expand=True, fill="both")
        
        tk.Label(self.current_screen, text=f"Código do Banco: {self.bank_code}").pack()
        tk.Label(self.current_screen, text=f"Número da Conta: {self.account_number}").pack()
        
        tk.Label(self.current_screen, text="Valor:").pack()
        self.amount_entry = tk.Entry(self.current_screen)
        self.amount_entry.pack()
        
        tk.Label(self.current_screen, text="Número do Cartão:").pack()
        self.card_number_entry = tk.Entry(self.current_screen)
        self.card_number_entry.pack()
        
        tk.Label(self.current_screen, text="PIN:").pack()
        self.pin_entry = tk.Entry(self.current_screen)
        self.pin_entry.pack()
        
        tk.Button(self.current_screen, text="Enviar", command=self.submit_form).pack()

        extra_frame = tk.Frame(self.current_screen)
        extra_frame.pack(pady=10)  
        test_label = tk.Label(self.current_screen, text="TESTS")
        test_label.pack()

        button_frame = tk.Frame(self.current_screen)
        button_frame.pack()

        tk.Button(button_frame, text="Pattern 01",command=self.first_entry_pattern).pack(side=tk.LEFT)
        tk.Button(button_frame, text="Pattern 02",command=self.second_entry_pattern).pack(side=tk.LEFT)

        
    def submit_form(self):
        amount = float(self.amount_entry.get())
        card_number = self.card_number_entry.get()
        pin = self.pin_entry.get()

        self.terminal_controller.receive_form_information(card_number,amount,pin)

    def first_entry_pattern(self):
        self.amount_entry.insert(0,10)
        self.card_number_entry.insert(0,313111111111)
        self.pin_entry.insert(0,1234)

    def second_entry_pattern(self):
        self.amount_entry.insert(0,10)
        self.card_number_entry.insert(0,413222222222)
        self.pin_entry.insert(0,1234)