# Функция как атрибут класса

class Car:
    model = "BMW"
    engine = 1.6

    def drive():
        print("Let's go")

# Пометить функцию как метод

    @staticmethod
    def drive2():
        print("Let's go")

print(Car.__dict__)

# Вызов функции класса

Car.drive()

# Вызов функции класса через функцию getattr

getattr(Car, "drive")()

# Вызов функции класса через экземпляр класса

a = Car()
print(a.__dict__)
print(a.drive)
a.drive2()
