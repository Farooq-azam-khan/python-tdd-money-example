from expression import Expression

class Bank:
    
    def __init__(self):
        self.rates = {}


    def reduce(self, source: Expression, to: str) -> 'Money':
        return source.reduce(self, to)
    

    def rate(self, frm: str, to: str) -> int:
        if frm == to:
            return 1
        return self.rates.get((frm, to)) 


    def addRate(self, frm: str, to: str, rate: int) -> None:
        self.rates[(frm, to)] = rate


