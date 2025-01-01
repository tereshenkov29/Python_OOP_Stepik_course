# Создайте класс Rectangle, который имеет следующие методы:
#
# 1. метод __init__, который устанавливает значения атрибутов width и height
# 2. метод area, который возвращает площадь прямоугольника
# 3. метод perimeter , который возвращает периметр прямоугольника

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Ниже код для проверки методов класса Rectangle
r1 = Rectangle(2, 3)
assert r1.width == 2
assert r1.height == 3
assert r1.perimeter() == 10
assert r1.area() == 6

r2 = Rectangle(10, 0.5)
assert r2.width == 10
assert r2.height == 0.5
assert r2.perimeter() == 21.0
assert r2.area() == 5.0
print('Good')