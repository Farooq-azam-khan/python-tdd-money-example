from abc import ABC, abstractmethod


class Expression(ABC):
    
    @abstractmethod
    def reduce(self, bank, to: str) -> 'Money':
        pass 
    
    @abstractmethod
    def times(self, multiplier: int) -> 'Expression':
        pass 


