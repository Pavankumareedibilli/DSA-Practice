class BankAccount:
    def __init__(self,balance=0):
        self.__balance=balance

    def deposit(self,amount):
        if(amount<0):
            print("Invalid amount!")
        self.__balance = self.__balance+amount
        print(f"Amount:{amount} deposited to bank!")

    def withdraw(self,amount):
        if(amount > self.__balance):
            print("Insufficient amount!")
        print(f"Amount:{amount} Withdrawd!") 
        self.__balance = self.__balance-amount

    def getBalance(self):
        print(self.__balance)

acc1 = BankAccount()
acc1.deposit(500)
acc1.withdraw(300)
acc1.getBalance()