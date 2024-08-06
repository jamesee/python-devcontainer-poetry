import pytest
from shopping_cart import ShoppingCart  # Adjust the import according to your project structure

@pytest.fixture
def price_map():
    return {
        'apple': 1.0,
        'banana': 0.5,
        'orange': 0.8
    }

@pytest.fixture
def cart():
    return ShoppingCart(max_size=3)

def test_add_item(cart):
    cart.add('apple')
    assert cart.size() == 1
    assert cart.get_items() == ['apple']

def test_add_multiple_items(cart):
    cart.add('apple')
    cart.add('banana')
    assert cart.size() == 2
    assert cart.get_items() == ['apple', 'banana']

def test_add_item_overflow(cart):
    cart.add('apple')
    cart.add('banana')
    cart.add('orange')
    with pytest.raises(OverflowError):
        cart.add('grape')

def test_get_total_price(cart, price_map):
    cart.add('apple')
    cart.add('banana')
    assert cart.get_total_price(price_map) == 1.5

def test_get_total_price_empty_cart(cart, price_map):
    assert cart.get_total_price(price_map) == 0.0

def test_get_items(cart):
    cart.add('apple')
    cart.add('banana')
    assert cart.get_items() == ['apple', 'banana']

def test_cart_initially_empty(cart):
    assert cart.size() == 0
    assert cart.get_items() == []