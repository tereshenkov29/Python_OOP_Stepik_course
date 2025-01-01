# Реализуйте класс Numbers, который предназначен для хранения произвольного количества чисел.
# Данный класс должен содержать:
#
# * метод __init__, принимающий произвольное количество чисел и сохраняющий их внутри экземпляра;
# * метод add_number, которой принимает числовое значение и добавляет его в конец коллекции экземпляра;
# * метод get_positive, который возвращает список всех положительных чисел из коллекции экземпляра;
# * метод get_negative, который возвращает список всех отрицательных чисел из коллекции экземпляра;
# * метод get_zeroes, который возвращает список всех нулевых значений из коллекции экземпляра.

class Numbers:
    def __init__(self, *args):
        self.numbers = list(args)

    def add_number(self, number):
        self.numbers.append(number)

    def get_positive(self):
        return [x for x in self.numbers if x > 0]

    def get_negative(self):
        return [x for x in self.numbers if x < 0]

    def get_zeroes(self):
        return [x for x in self.numbers if x == 0]