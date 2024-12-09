# Создаем класс
class Car:
    model = "BMW"
    engine = 1.6

# Создаем экземпляр класса
a = Car()

# Узнаем тип экземпляра класса
print(type(a))

# Проверяем, что переменная является экземпляром указанного класса
print(isinstance(a, Car))

# Создаем еще несколько экземпляров класса
b = Car()
c = Car()
d = Car()

b.model = "VAZ"  # Изменяем значение атрибута model в ЭК
b.color = 'white'  # Добавляем новый атрибут в ЭК
print(b.model, b.color)  # Вывод: VAZ white


print(a == c)
num1 = 1
num2 = 1
print(type(num1))
print(type(num2))
print(num1 == num2)