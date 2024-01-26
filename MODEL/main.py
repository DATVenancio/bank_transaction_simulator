from Bank import Bank
from User import User
from Terminal import Terminal
from BankNetwork import BankNetwork





print("----- Creating banks -----")
bank01 = Bank("Credit Agricole",3,131)
bank02 = Bank("Credit Mutual",4,132)



print("----- Creating accounts -----")
user01 = User("Daniel")
bank01.createAccount(user01)
bank01.credit(user01,1000)
bank01.showAccountInfo(user01)
user01.requestCard()
print(user01.bankCard.cardNumber)


print("--")
user02 = User("LojaFernando")
bank02.createAccount(user02)
bank02.showAccountInfo(user02)

print("-----Terminal-----")

terminal01 = Terminal(user02.account)
#terminal01.startTransaction(user01.bankCard,user02,100)

#terminal01.makeTransaction()










