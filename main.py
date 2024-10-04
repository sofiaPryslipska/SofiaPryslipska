from Laptop import Laptop
from Phone import Phone

laptop1 = Laptop(" MacBook Air M2", "Apple", 1200, 1.2)
laptop2 = Laptop("ZenBook 14", "ASUS", 850, 1.5)
laptop3 = Laptop("ThinkPad X1 Carbon", "Lenovo", 999, 1.7)

phone1 = Phone("Iphone 12", "Apple", 400, 0.7)
phone2 = Phone("Mi 11", "Xiaomi", 250, 0.8)
phone3 = Phone("Galaxy S21", "Samsung", 525, 0.6)


Phone.print_all()
Laptop.print_all()
phone1.buy()
laptop2.buy()
Phone.print_all()
Laptop.print_all()
