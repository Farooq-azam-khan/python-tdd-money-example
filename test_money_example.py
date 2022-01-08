from dollar import Dollar, Franc

def test_multiplication():
    five = Dollar(5)
    # Dollar to Dollar test
    assert Dollar(10) == five.times(2) 
    assert Dollar(15) == five.times(3) 
    # Note: above test is easy to read as if it were assertions of truth rather than sequences of operations
def test_equality():
    assert Dollar(5).equals(Dollar(5))
    # Triangulation: when the second test demands a more general solution, then and only then do we generalize
    assert not Dollar(5).equals(Dollar(6))

def test_franc_multiplication():
    five = Franc(5)
    assert Franc(10) == five.times(2)
    assert Franc(15) == five.times(3)
