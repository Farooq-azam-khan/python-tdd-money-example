from abc import ABC, abstractmethod

class Money(ABC):
    def __init__(self, amount: int, currency: str):
        self.amount = amount
        self.currency = currency 

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency 
   
    @staticmethod
    def dollar(amount: int):
        return Dollar(amount, "USD")
    
    
    @staticmethod
    def franc(amount: int):
        return Franc(amount, "CHF")
    
    
    #@abstractmethod
    #def times(self, multiplyer: int): # -> 'Money'
    #    pass 

    
    #@abstractmethod
    #def get_currency(self): # -> 'str'
    #    pass 

    def currency(self):
        return self.currency

    def __repr__(self):
        return f"{self.amount} {self.currency}"

class Dollar(Money):
  
    def __init__(self, amount: int, currency: str = "USD") -> None:
        Money.__init__(self, amount, currency)


    def times(self, multiplyer: int):
        return Money.dollar(self.amount * multiplyer)

    def get_currency(self) -> str:
        return self.currency 


class Franc(Money):

    def __init__(self, amount: int, currency: str = "CHF") -> None:
        Money.__init__(self, amount, currency)

    def times(self, multiplier):
        return Money.franc(self.amount * multiplier)
   
    def get_currency(self) -> str:
        return self.currency


