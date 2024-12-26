#  Создайте класс Laptop, у которого есть:
#
# конструктор __init__, принимающий 3 аргумента: бренд, модель и цену ноутбука. На основании этих аргументов нужно для
# экземпляра создать атрибуты brand, model, price и также атрибут laptop_name  — строковое значение, следующего вида:
# «<brand> <model>»
# hp = Laptop('hp', '15-bw0xx', 57000)
# print(hp.price) # выводит 57000
# print(hp.laptop_name) # выводит "hp 15-bw0xx"
# И затем создайте 2 экземпляра класса Laptopи сохраните их в переменные laptop1 и laptop2.

class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = self.brand + " " + self.model

laptop1 = Laptop("xxx", "yyy", 100)
laptop2 = Laptop("nnn", "kkk", 500)