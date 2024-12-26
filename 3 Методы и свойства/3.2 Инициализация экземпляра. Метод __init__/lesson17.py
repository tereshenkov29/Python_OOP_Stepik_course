# Поиск багов
# Перед Василием поставили задачу создать класс Person и реализовать в нем следующие методы:
#
# метод __init__, который устанавливает значения атрибутов name и age;
#
#   метод greet, возвращающий строку в следующем формате:
# «Hello, my name is [name], and I am [age] years old»
# Вот что нашкодил Василий, посмотрите реализацию кода ниже. Он не проходит проверки, которые написаны ниже
# определения класса Person. Ваша задача найти ошибки в коде и их исправить

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name.capitalize()}, and I am {self.age} years old"


# Ниже расположен код для проверок, его не нужно удалять
bro = Person('Nikolay', 34)
assert bro.age == 34
assert bro.name == 'Nikolay'
assert bro.greet() == 'Hello, my name is Nikolay, and I am 34 years old'

sister = Person('Elena', 21)
assert sister.age == 21
assert sister.name == 'Elena'
assert sister.greet() == 'Hello, my name is Elena, and I am 21 years old'
print('Good')