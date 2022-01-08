from abc import ABC, abstractmethod

class Expression(ABC):
    pass 

class Bank:
    def reduce(self, source: Expression, to: str):
        return Money(10, "USD") 

class Money(Expression):

    def __init__(self, amount: int, currency: str):
        self.amount = amount
        self.currency = currency 

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency 
   
    @staticmethod
    def dollar(amount: int):
        return Money(amount, "USD")
    
    
    @staticmethod
    def franc(amount: int):
        return Money(amount, "CHF")
    
    def times(self, multiplier: int):
        return Money(self.amount * multiplier, self.currency)


    def currency(self):
        return self.currency

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def get_currency(self) -> str:
        return self.currency 

    def plus(self, addend) -> Expression:
        return Money(self.amount + addend.amount, self.currency)
