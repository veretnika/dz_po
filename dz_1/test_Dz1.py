import pytest
from Dz1 import *
@pytest.mark.parametrize('name, price', [('water', 25.0 ), ('juice', 50.0 ), ('iceTea',25.0)])
def test_name_price(name: str, price: float):
    kek = Product(name, price)
    assert kek.name == name
    assert kek.price == price

@pytest.mark.parametrize('productClass, productPrice', [([Product('water', 25.0), Product('juice', 50.0 ), Product('iceTea',25.0)], 'мы добавили что-то')])
def test_add(productClass: Product, productPrice: str):
    basket_1 = Basket()
    for p in productClass:
        basket_1.add(p)
        assert productPrice == basket_1.add(p)
@pytest.mark.parametrize('productClass, productPrice', [([Product('water', 25.0), Product('juice', 50.0 ), Product('iceTea',25.0)], 'мы удалили что-то')])
def test_remove(productClass: Product, productPrice: str):
    basket_2 = Basket()
    for p in productClass:
        basket_2.add(p)
        assert productPrice == basket_2.remove(p)


@pytest.mark.parametrize('productClass, productPrice', [([Product('water', 25.0), Product('juice', 50.0 ), Product('iceTea',25.0)], 100)])
def test_sum(productClass: Product, productPrice: float):
    basket_3 = Basket()
    for p in productClass:
        basket_3.add(p)
    assert productPrice == basket_3.count_sum()
