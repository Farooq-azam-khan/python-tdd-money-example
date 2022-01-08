from money import Franc, Money

def test_multiplication():
    five = Money.dollar(5)
    # Dollar to Dollar test
    assert Money.dollar(10) == five.times(2) 
    assert Money.dollar(15) == five.times(3) 
    # Note: above test is easy to read as if it were assertions of truth rather than sequences of operations
def test_equality():
    assert Money.dollar(5) == Money.dollar(5)
    # Triangulation: when the second test demands a more general solution, then and only then do we generalize
    assert Money.dollar(5) != Money.dollar(6)
    assert Franc(5) == Franc(5)
    assert Franc(5) != Franc(6)
    # dollars and franc comparison
    assert Franc(5) != Money.dollar(5)

def test_franc_multiplication():
    five = Franc(5)
    assert Franc(10) == five.times(2)
    assert Franc(15) == five.times(3)
