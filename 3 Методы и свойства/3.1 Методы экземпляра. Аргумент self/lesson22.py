# Класс Point. Часть 2
# Продолжим реализацию класса Point из предыдущего задания. Вам необходимо добавить в него реализацию еще одного метода
# get_distance, который обязательно принимает экземпляр класса Point. Результатом работы метода get_distance должно
# быть вычисленное расстояние между двумя точками. Его также можно найти при помощи теоремы Пифагора.
#
# Но расстояние можно вычислить только в том случае, если у двух точек имеются координаты x и y. Если хотя бы у одной
# точки отсутствуют атрибуты x или y, необходимо вывести сообщение «Координаты не заданы» и вернуть значение None.
#
# В случае, если в данный метод передается не экземпляр класса Point, необходимо вывести сообщение «Передана не точка»
# и вернуть значение None.
#
# 🚀Подсказка🚀
# Вспоминаем функцию isinstance для проверки принадлежности

class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance_to_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5 if hasattr(self, "x") and hasattr(self, "y") else None

    def get_distance(self, point):
        if isinstance(point, Point) == False:
            print("Передана не точка")
        else:
            if (hasattr(self, "x") == False or hasattr(self, "y") == False) or (hasattr(point, "x") == False or
                                                                                hasattr(point, "y") == False):
                print("Координаты не заданы")
            else:
                return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5

    def display(self):
        if hasattr(self, "x") == False or hasattr(self, "y") == False:
            print("Координаты не заданы")
        else:
            print(f"Point({self.x}, {self.y})")