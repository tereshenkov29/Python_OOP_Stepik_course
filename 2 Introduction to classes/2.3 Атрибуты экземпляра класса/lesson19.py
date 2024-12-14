# Имеется пустой класс Config. Ваша задача написать функцию create_instance, которая принимает на вход
# положительное число N. Функция должна создать ЭК , создать у него N атрибутов и вернуть в качестве ответа
# полученный ЭК.
#
# Что касается атрибутов, они должны называться определенным образом и иметь определенное значение. В общем виде
# это можно записать так:
#
# attribute<n> = "value<n>"
# где n — порядковый номер атрибута. Значение атрибута — строковый тип.
#
# Если в функцию create_instance передали значение 3, то нужно создать следующие атрибуты и значения:
#
# # Если передать в функцию значение 3
# obj = Config()
# obj.attribute1 = "value1"
# obj.attribute2 = "value2"
# obj.attribute3 = "value3"
# Если передать в create_instance значение 5, то необходимо создать следующие атрибуты
#
# # Если передать в функцию значение 5
# obj = Config()
# obj.attribute1 = "value1"
# obj.attribute2 = "value2"
# obj.attribute3 = "value3"
# obj.attribute4 = "value4"
# obj.attribute5 = "value5"
# Ваша задача написать только определение функции create_instance , и не забывайте, что она должна вернуть ЭК.
#
# Примечание: в коде используется следующее определение функции create_instance:
#
# def create_instance(n: int) -> Config:
#     pass
# Если вам непонятны символы ->, то следует изучить тему «Типизация и аннотации типов».

class Config:
    pass

def create_instance(n: int) -> Config:
    obj = Config()
    for i in range(1, n+1):
        attribute_name = "attribute" + str(i)
        attribute_value = "value" + str(i)
        setattr(obj, attribute_name, attribute_value)
    return obj