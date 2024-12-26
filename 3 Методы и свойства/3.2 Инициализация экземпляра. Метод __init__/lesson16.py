# Создайте класс Vehicle, у которого есть:
#
# метод __init__, принимающий максимальную скорость и пробег. Их необходимо сохранить в атрибуты экземпляра max_speed и mileage соответственно.
# Ваша задача  — только определить класс Vehicle
#
# Sample Input 1:
#
# model_x = Vehicle(200, 18000)
# print(model_x.max_speed)
# print(model_x.mileage)
# Sample Output 1:
#
# 200
# 18000
# Sample Input 2:
#
# bmw = Vehicle(240, 18)
# audi = Vehicle(123, 43)
# print(bmw.__dict__)
# print(audi.__dict__)
# Sample Output 2:
#
# {'max_speed': 240, 'mileage': 18}
# {'max_speed': 123, 'mileage': 43}

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage