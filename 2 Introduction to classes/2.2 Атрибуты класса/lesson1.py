# Атрибуты класса
class Person:
    name = "Ivan"
    age = 30

# Получить все атрибуты класса
print(Person.__dict__)

# Получить значение атрибута класса
print(getattr(Person, "name"))

# Выводить значение по умолчанию, если нет такого атрибута в классе
print(getattr(Person, "x", 100))

# Проверка наличия определенного атрибута в классе
print('salary' in Person.__dict__) # False

# Проверка наличия определенного атрибута в классе
print(hasattr(Person, 'name')) # True

# Изменение значения атрибута
Person.name = "Misha"

# Попытка изменения несуществующего атрибута добавит этот атрибут в класс
Person.x = 100

# Изменение значения атрибута через функцию
setattr(Person, "x", 500)

# Создание атрибута через функцию
setattr(Person, "y", 200)

# Удаление атрибута
del Person.x

# Удаление атрибута через функцию
delattr(Person, "y")

# Изменения атрибутов для класса влияют на каждый экземпляр класса
a = Person()
b = Person()
print(dir(a))
print(dir(b))
Person.z = 100
del Person.age
print(dir(a))
print(dir(b))

# Изменения атрибутов для экземпляра класса влияют только на этот экземпляр класса
a.b = 100500
print(dir(a))
print(dir(b))