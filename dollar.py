class Money:
   def __init__(self, amount: float):
        self.amount = amount
    
    def __eq__(self, other):
        return self.amount == other.amount 
 
class Dollar(Money):
   
    def times(self, multiplyer: float):
        return Dollar(self.amount * multiplyer)

   
class Franc:
    def __init__(self, amount):
        self.amount = amount 

    def times(self, multiplier):
        return Franc(self.amount * multiplier)
    
    def __eq__(self, other):
        return self.amount == other.amount


