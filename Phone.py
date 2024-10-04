from Product import Product
from Deliver import Deliver


class Phone(Product, Deliver):
    all_phones = []

    def __init__(self, name, brand, price, weight):
        super().__init__(name, brand, price)
        Deliver.__init__(self, weight)

        Phone.all_phones.append(self)

    @staticmethod
    def print_all():
        for i, phone in enumerate(Phone.all_phones, start=1):
            print(f"Phone #{i}: {phone.name}, {phone.brand}, Price: {phone.get_price()}")
        print("\n")

    def buy(self):
        print(f"You bought phone: {self.name} {self.brand}")
        total_price = self.get_price()
        total_price += self.weight * 10
        print(f"Your price with delivery is {total_price}\n")
        if self in Phone.all_phones:
            Phone.all_phones.remove(self)
