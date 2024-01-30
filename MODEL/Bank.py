from BankAccount import BankAccount
from BankCard import BankCard
from bank_transaction_simulator.MODEL.BankNetworkServer import BankNetwork

class Bank:
    def __init__(self,name):
        self.name = name

    
    def createAccount(self,user):
        if(not self.userHasAccount(user)):
            print("Account created!")
            userAccount = BankAccount(user,self)
            user.account = userAccount
            self._accounts.append(userAccount)
        else:
            print("User already has an account!")
    def createBankCard(self,account):
        cardNumber = self._generateCardNumber()
        bankCard = BankCard(cardNumber,account.user)
        account.user.bankCard = bankCard

    def userHasAccount(self,user):
        for account in self._accounts:
            if account.user==user:
                return True
        return False
    
    def showAccountInfo(self,user):
        if(self.userHasAccount(user)):
            user.account.printInfos()
    
    def credit(self,user,amount):
        user.account.increaseMoney(amount)
    
    def debit(self,user,amount):
        if(user.account.hasEnoughMoney(amount)):
            user.account.decreaseMoney(amount)
    
    def authorizationRequest(self,cardNumber,amount):
        self.bankNetwork.authorizationRequest(cardNumber,amount)




    def _generateCardNumber(self):
        #gera numero
        #checagem se nao tem no bd
        return "ABCDEFGHIJKLMNOP"
