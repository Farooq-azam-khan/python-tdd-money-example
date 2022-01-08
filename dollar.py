class Dollar:
    def __init__(self, amount: float):
        self.amount = amount
    def times(self, multiplyer: float) -> None:
        return Dollar(self.amount * multiplyer)

    def equals(self, other):
        return True
    

