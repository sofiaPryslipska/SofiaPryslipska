class Product:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price
