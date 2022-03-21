from typing import List
class Product():
    name: str
    price: float
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Basket:
    basket: List[Product] = []
    def add(self, product: Product):
        self.basket.append(product)
    def remove(self, product: Product):
        self.basket.remove(product)
    def count_sum(self):
        sums = 0
        for i in range(0, len(self.basket)):
            sums += self.basket[i].price
        return sums

