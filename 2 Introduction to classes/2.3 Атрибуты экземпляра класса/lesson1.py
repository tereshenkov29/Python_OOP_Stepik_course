# создание класса
class Car:
    model = "BMW"
    engine = 1.6

# создание экземпляров класса
a1 = Car()
a2 = Car()

# добавление уникального атрибута для экземпляра класса
a1.seat = 4
print(a1.__dict__)
print(a2.__dict__)
print(Car.__dict__)

# изменение значения атрибута класса для одного из экземпляров
a1.model = "Lada"
print(a1.__dict__)
print(a2.__dict__)
print(Car.__dict__)

a2.size = 80

# создание нового атрибута класса добавит этот атрибут всем экземплярам класса
Car.r = 100
print(a1.__dict__)
print(a2.__dict__)
print(Car.__dict__)

# после удаления атрибута экземпляра класса обращение к такому же атрибуту в экземпляре вернет атрибут класса
print(a1.model)
print(a1.__dict__)
del a1.model
print(a1.model)