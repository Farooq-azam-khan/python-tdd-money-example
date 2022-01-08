from abc import ABC, abstractmethod

class Money(ABC):
    def __init__(self, amount: int):
        self.amount = amount
     
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
    def currency(self): # -> 'str'
        pass 


class Dollar(Money):
   
    def times(self, multiplyer: int):
        return Dollar(self.amount * multiplyer)
    
    def currency(self):
        return "USD"

class Franc(Money):

    def times(self, multiplier):
        return Franc(self.amount * multiplier)
   
    def currency(self):
        return "CHF"


