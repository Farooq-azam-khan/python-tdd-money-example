from abc import ABC, abstractmethod
from pair import Pair 

class Expression(ABC):
    @abstractmethod
    def reduce(self, bank, to: str): # -> Money
        pass 
    
    @abstractmethod
    def times(self, multiplier: int) -> 'Expression':
        pass 

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
    
    def times(self, multiplier: int) -> Expression:
        amnt = self.amount * multiplier
        return Money(amnt, self.currency)

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def get_currency(self) -> str:
        return self.currency 

    def plus(self, addend: Expression) -> Expression:
        return Sum(self, addend) 

    def reduce(self, bank: 'Bank', to: str): # -> Money
        rate: int = bank.rate(self.currency, to) 
        return Money(int(self.amount / rate), to) 

class Bank:
    
    def __init__(self):
        self.rates = {}


    def reduce(self, source: Expression, to: str) -> Money:
        return source.reduce(self, to)
    

    def rate(self, frm: str, to: str) -> int:
        if frm == to:
            return 1
        return self.rates.get(Pair(frm, to)) #.get return none instead of throwing error


    def addRate(self, frm: str, to: str, rate: int) -> None:
        self.rates[Pair(frm, to)] = rate

class Sum(Expression):
    
    def __init__(self, augend: Expression, addend: Expression):
        self.augend = augend
        self.addend = addend


    def plus(self, addend):
        return Sum(self, self.addend)

    def times(self, multiplier: int):
        aug = self.augend.times(multiplier)
        add = self.addend.times(multiplier)
        return Sum(aug, add)


    def reduce(self, bank, to: str) -> Money: 
        amnt: int = self.augend.reduce(bank, to).amount + self.addend.reduce(bank, to).amount
        return Money(amnt, to)



