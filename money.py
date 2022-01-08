class Money:
    def __init__(self, amount: int):
        self.amount = amount
     
    def __eq__(self, other):
        self_class_name = type(self).__name__
        other_class_name = type(other).__name__
        return self.amount == other.amount and self_class_name == other_class_name
   
    @staticmethod
    def dollar(amount: int):
        return Dollar(amount) 


class Dollar(Money):
   
    def times(self, multiplyer: int):
        return Dollar(self.amount * multiplyer)


class Franc(Money):

    def times(self, multiplier):
        return Franc(self.amount * multiplier)
    


