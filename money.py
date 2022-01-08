from abc import ABC, abstractmethod

class Money(ABC):
    def __init__(self, amount: int):
        self.amount = amount
        self.currency = None 

    def __eq__(self, other):
        self_class_name = type(self).__name__
        other_class_name = type(other).__name__
        return self.amount == other.amount and self_class_name == other_class_name
   
    @staticmethod
    def dollar(amount: int):
        return Dollar(amount) 
    
    
    @staticmethod
    def franc(amount: int):
        return Franc(amount)
    
    
    @abstractmethod
    def times(self, multiplyer: int): # -> 'Money'
        pass 

    
    @abstractmethod
    def get_currency(self): # -> 'str'
        pass 

    def currency(self):
        return self.currency


class Dollar(Money):
  
    def __init__(self, amount: int, currency: str = "USD") -> None:
        Money.__init__(self, amount)
        self.currency = currency 


    def times(self, multiplyer: int):
        return Dollar(self.amount * multiplyer)

    def get_currency(self) -> str:
        return self.currency 


class Franc(Money):

    def __init__(self, amount: int, currency: str = "CHF") -> None:
        Money.__init__(self, amount)
        self.currency = currency 

    def times(self, multiplier):
        return Money.franc(self.amount * multiplier)
   
    def get_currency(self) -> str:
        return self.currency


