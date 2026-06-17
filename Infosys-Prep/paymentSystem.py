from abc import ABC,abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class cardPayment(payment):
    def pay(self,amount):
        print(f"Paid {amount} using Card")

class TokenPayment(payment):
    def pay(self,amount):
        print(f"Paid{amount} using Token Payment")

class UPIPayment(payment):
    def pay(self,amount):
        print(f"Paid {amount} using UPI")

def process_payment(payment:payment , amount):
    payment.pay(amount)


process_payment(TokenPayment(),5000)