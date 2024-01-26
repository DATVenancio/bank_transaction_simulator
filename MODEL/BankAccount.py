class BankAccount():
    def __init__(self,user,bank):
        self.user = user
        self.bank = bank
        self.money = 0
        self.bankCard = None
    
    def printInfos(self):
        print("User: " ,self.user.name)
        print("Money: " , self.money)
    
    def hasEnoughMoney(self,amount):
        if(amount <= self.money):
            return True
        else:
            return False

    def increaseMoney(self,amount):
        self.money += amount
    
    def decreaseMoney(self,amount):
        self.money -= amount

    def requestCard(self):
        self.bankCard= self.bank.createBankCard(self)
    