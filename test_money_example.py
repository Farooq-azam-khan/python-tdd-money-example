from money import (Money, 
                   Bank, 
                   Sum)
from bank import Bank
import pytest 
from expression import Expression


def test_multiplication():
    five = Money.dollar(5)
    assert Money.dollar(10) == five.times(2) 
    assert Money.dollar(15) == five.times(3) 


def test_equality():
    assert Money.dollar(5) == Money.dollar(5)
    assert Money.dollar(5) != Money.dollar(6)
    assert Money.franc(5) == Money.franc(5)
    assert Money.franc(5) != Money.franc(6)
    assert Money.franc(5) != Money.dollar(5)


@pytest.fixture
def bank():
    return Bank()

@pytest.fixture
def five_bucks():
    return Money.dollar(5)


@pytest.fixture
def ten_francs():
    return Money.franc(10)


def test_franc_multiplication():
    five = Money.franc(5)
    assert Money.franc(10) == five.times(2)
    assert Money.franc(15) == five.times(3)


def test_currency():
    assert "USD" == Money.dollar(1).currency
    assert "CHF" == Money.franc(1).currency

def test_repr():
    assert Money.dollar(1).__repr__() == "1 USD"
    assert Money.franc(1).__repr__() == "1 CHF"

def test_different_class_equality():
    assert Money(10, "CHF") == Money.franc(10)


def test_simple_addition(bank, five_bucks):
    sm: Expression = five_bucks.plus(five_bucks)
    reduced: Money = bank.reduce(sm, "USD")
    assert reduced == Money.dollar(10)


def test_plus_returns_sum(five_bucks):
    sm: Sum = five_bucks.plus(five_bucks)
    assert five_bucks == sm.augend
    assert five_bucks == sm.addend


def test_reduce_sum(bank):
    sm: Expression = Sum(Money.dollar(3), Money.dollar(4))
    result: Money = bank.reduce(sm, "USD")
    assert Money.dollar(7) == result


def test_reduce_money(bank):
    result: Money = bank.reduce(Money.dollar(1), "USD")
    assert Money.dollar(1) == result

def test_reduce_money_different_currency(bank):
    bank.addRate("CHF", "USD", 2)
    result: Money = bank.reduce(Money.franc(2), "USD")
    assert Money.dollar(1) == result


def test_identity_rate(bank):
    assert 1 == bank.rate("USD", "USD")

def test_mixed_addition(bank, five_bucks, ten_francs):
    bank.addRate("CHF", "USD", 2)
    result: Money = bank.reduce(five_bucks.plus(ten_francs), "USD")
    assert Money.dollar(10) == result


def test_sum_plus_money(bank, five_bucks, ten_francs):
    bank.addRate("CHF", "USD", 2)
    sm: Expression = Sum(five_bucks, ten_francs).plus(five_bucks)
    result: Money = bank.reduce(sm, "USD")
    assert Money.dollar(15) == result


def test_sum_times(bank, five_bucks, ten_francs):
    bank.addRate("CHF", "USD",2)
    sm: Expression = Sum(five_bucks, ten_francs).times(2)
    result: Money = bank.reduce(sm, "USD")
    assert Money.dollar(20) == result

def test_plus_same_currency_return_money():
    sm: Expression = Money.dollar(1).plus(Money.dollar(1))
    assert isinstance(sm, Sum)
