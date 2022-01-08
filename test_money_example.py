from dollar import Dollar

def test_multiplication():
    five = Dollar(5)
    product = five.times(2)
    #assert 10 == product.amount
    # Dollar to Dollar test
    assert Dollar(10) == product
    product = five.times(3)
    #assert 15 == product.amount
    assert Dollar(15) == product

def test_equality():
    assert Dollar(5).equals(Dollar(5))
    # Triangulation: when the second test demands a more general solution, then and only then do we generalize
    assert not Dollar(5).equals(Dollar(6))
