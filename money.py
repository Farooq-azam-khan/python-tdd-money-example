class Dollar:
    def __init__(self, amount: float):
        self.amount = amount
    
    def times(self, multiplyer: float):
        return Dollar(self.amount * multiplyer)

    def equals(self, other):
        return self.amount == other.amount 

    def __eq__(self, other):
        return self.equals(other)
    
class Franc:
    def __init__(self, amount):
        self.amount = amount 

    def times(self, multiplier):
        return Franc(self.amount * multiplier)
    
    def equals(self, other):
        return self.amount == other.amount

    def __eq__(self, other):
        return self.equals(other)

