# Конструктор
# Создайте класс Constructor, в котором реализованы:
#
# Метод add_atribute, принимающий на вход название атрибута в виде строки и его значение. Задача метода add_atribute
# — создать или изменить атрибут экземпляра по переданному имени атрибута;
#
# Метод display, печатающий на экран словарь __dict__ у экземпляра.
# Необходимо написать только определение класса Constructor
#
# 🚀Подсказка🚀
# Для проверки наличия атрибута воспользуйтесь функцией setattr

class Constructor:
    def add_atribute(self, attribute_name, attribute_value):
        setattr(self, attribute_name, attribute_value)

    def display(self):
        print(self.__dict__)