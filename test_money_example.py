from money import Money


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
    assert Money.franc(5) == Money.franc(5)
    assert Money.franc(5) != Money.franc(6)
    # dollars and franc comparison
    assert Money.franc(5) != Money.dollar(5)


def test_franc_multiplication():
    five = Money.franc(5)
    assert Money.franc(10) == five.times(2)
    assert Money.franc(15) == five.times(3)


def test_currency():
    assert "USD" == Money.dollar(1).currency()
    assert "CHF" == Money.franc(1).currency()
