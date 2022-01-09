 
class Pair:
    def __init__(self, frm: str, to: str):
        self.frm: str = frm 
        self.to: str = to 

    def __eq__(self, other):
        return self.frm == other.frm and self.to == other.to

    def __hash__(self):
        return 0

