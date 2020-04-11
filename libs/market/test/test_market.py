import attr
import pytest 

from libs.market.market import Market

class DummyProduct1:
    pass

class DummyProduct2:
    pass

def test_market():
    market = Market({DummyProduct1: 100})

    assert market.can_buy(DummyProduct1)
    assert market.get_price(DummyProduct1) == 100
    
    instance1 = market.buy(DummyProduct1)
    assert isinstance(instance1, DummyProduct1)

    market.set_product_price(DummyProduct2, 1)
    assert market.get_price(DummyProduct1) == 100
    assert market.get_price(DummyProduct2) == 1

    instance2 = market.buy(DummyProduct2)
    assert isinstance(instance2, DummyProduct2)
