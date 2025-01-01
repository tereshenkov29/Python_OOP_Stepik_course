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
        if self.check_exist_coord():
            return (self.x ** 2 + self.y ** 2) ** 0.5
        return None

    def get_distance(self, point2):
        if not isinstance(point2, Point):
            print('Передана не точка')
            return None
        # проверяем наличие координат
        if self.check_exist_coord() and point2.check_exist_coord():
            return (abs(self.x - point2.x) ** 2 + abs(self.y - point2.y) ** 2) ** 0.5
        print('Координаты не заданы')
        return None

    def check_exist_coord(self) -> bool:
        return hasattr(self, 'x') and hasattr(self, 'y')

    def display(self):
        if self.check_exist_coord():
            print(f"Point({self.x}, {self.y})")
        else:
            print('Координаты не заданы')