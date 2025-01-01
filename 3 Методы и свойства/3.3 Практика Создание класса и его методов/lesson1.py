# Практика "Создание класса и его методов"
from math import sqrt


class Point:

    list_points = []

    def __init__(self, coord_x = 0, coord_y = 0):
        # self.x = coord_x
        # self.y = coord_y
        self.move_to(coord_x, coord_y)
        Point.list_points.append(self)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        # self.x = 0
        # self.y = 0
        self.move_to(0,0)

    def print_point(self):
        print(f"Точка с координатами ({self.x}, {self.y})")

    def calc_dictance(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError("Аргумент должен принадлежать классу Point")

        return sqrt((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2)

p1 = Point(3, 4)
p2 = Point(-54, 32)

p3 = Point()
p3.move_to(4, 5)
p3.move_to(-90, 5)

p4 = Point(4)
p4.move_to(4, 8)
p4.move_to(8,8)
p4.go_home()

p5 = Point()
p5.print_point()
p5.move_to(7, -43)
p5.print_point()

p7 = Point(6, 0)
p8 = Point(0,8)

print(p7.calc_dictance(p8))

p11 = Point()
print(Point.list_points)