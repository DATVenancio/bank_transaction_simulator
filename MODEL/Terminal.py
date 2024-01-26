class Terminal:
    def __init__(self,bankAccount):
        self.bankAccount=bankAccount

    def startTransaction(self,bankCard,amount):
        if(self.checkInformation(bankCard)):
            self.bank.authorizationRequest(bankCard.cardNumber,amount)
        


    def checkInformation(bankCard):
        #validade,pin,
        return True