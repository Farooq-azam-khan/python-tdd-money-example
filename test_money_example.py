from money import (Money, 
                   Bank, 
                   Expression, 
                   Sum, 
                   Pair)


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
    assert "USD" == Money.dollar(1).get_currency()
    assert "CHF" == Money.franc(1).get_currency()

def test_repr():
    assert Money.dollar(1).__repr__() == "1 USD"
    assert Money.franc(1).__repr__() == "1 CHF"

def test_different_class_equality():
    assert Money(10, "CHF") == Money.franc(10)


def test_simple_addition():
    five: Money = Money.dollar(5)
    sm: Expression = five.plus(five)
    bank: Bank = Bank()
    reduced: Money = bank.reduce(sm, "USD")
    assert reduced == Money.dollar(10)


def test_plus_returns_sum():
    five: Money = Money.dollar(5)
    result: Expression = five.plus(five)
    sm: Sum = result
    assert five == sm.augend
    assert five == sm.addend


def test_reduce_sum():
    sm: Expression = Sum(Money.dollar(3), Money.dollar(4))
    bank: Bank = Bank()
    result: Money = bank.reduce(sm, "USD")
    assert Money.dollar(7) == result


def test_reduce_money():
    bank: Bank = Bank()
    result: Money = bank.reduce(Money.dollar(1), "USD")
    assert Money.dollar(1) == result

def test_reduce_money_different_currency():
    bank: Bank = Bank()
    bank.addRate("CHF", "USD", 2)
    result: Money = bank.reduce(Money.franc(2), "USD")
    assert Money.dollar(1) == result

def test_array_equals():
    assert ["abc"] == ["abc"]

def test_pair_creation():
    p = Pair("asdf", "def")
    assert p.frm == "asdf"
    assert p.to == "def"

def test_identity_rate():
    assert 1 == Bank().rate("USD", "USD")
