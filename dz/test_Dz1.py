import pytest
from Dz1 import *
@pytest.mark.parametrize('name, price', [('water', 25.0 ), ('juice', 50.0 ), ('iceTea',25.0)])
def test_name_price(name: str, price: float):
    test = Product(name, price)
    assert test.name == name
    assert test.price == price

@pytest.mark.parametrize('basket, idealBasket', [([Product('water', 25.0), Product('juice', 50.0 ), Product('iceTea',25.0)], [Product('water', 25.0), Product('juice', 50.0 ), Product('iceTea',25.0)]), ([Product('iceTea',25.0)], [Product('iceTea',25.0)])])
def test_add(basket: List[Product], idealBasket: List[Product]):
    basket_1 = Basket()
    for p in basket:
        basket_1.add(p)
    test = True
    for p1, p2 in zip(idealBasket, basket_1.basket):
        if not (p1.name == p2.name and p1.price == p2.price):
            test = False
            break
    assert test

@pytest.mark.parametrize('basket, idealBasket', [([Product('water', 25.0), Product('juice', 50.0 ), Product('iceTea',25.0)], [Product('water', 25.0), Product('juice', 50.0 ), Product('iceTea',25.0)]), ([Product('iceTea',25.0)], [Product('iceTea',25.0)])])
def test_remove(basket: List[Product], idealBasket: List[Product]):
    basket_2 = Basket()
    for p in basket:
        basket_2.add(p)
        basket_2.remove(p)
    test = True
    for p1, p2 in zip(idealBasket, basket_2.basket):
        if not (p1.name == p2.name and p1.price == p2.price):
            test = False
            break
    assert test

@pytest.mark.parametrize('productClass, productPrice', [([Product('water', 25.0), Product('juice', 50.0 ), Product('iceTea',25.0)], 100)])
def test_sum(productClass: Product, productPrice: float):

    basket_3 = Basket()
    for pb in productClass:
        basket_3.add(pb)
    assert productPrice == basket_3.count_sum()
