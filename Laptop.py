from Product import Product
from Deliver import Deliver


class Laptop(Product, Deliver):
    all_laptops = []

    def __init__(self, name, brand, price, weight):
        super().__init__(name, brand, price)
        Deliver.__init__(self, weight)

        Laptop.all_laptops.append(self)

    @staticmethod
    def print_all():
        for i, laptop in enumerate(Laptop.all_laptops, start=1):
            print(f"Laptop #{i}: {laptop.name}, {laptop.brand}, Price: {laptop.get_price()}")
        print("\n")

    def buy(self):
        print(f"You bought laptop: {self.name} {self.brand}")
        total_price = self.get_price()
        total_price += self.weight * 10
        print(f"your price with delivery is {total_price}\n")
        if self in Laptop.all_laptops:
            Laptop.all_laptops.remove(self)
