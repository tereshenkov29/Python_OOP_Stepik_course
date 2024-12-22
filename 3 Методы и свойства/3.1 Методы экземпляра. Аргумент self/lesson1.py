# Появляется ошибка, если в классе создать функцию без self и вызвать функцию для экземпляра класса
class Cat:
    def hello():
        print("Hello world")

Cat.hello()
bob = Cat()
# print(bob.hello()) # TypeError: Cat.hello() takes 0 positional arguments but 1 was given

# Метод - это функция, которая определена внутри класса и относится к конкретному объекту
# Вызов метода и вызов экземпляра класса ссылаются на одну область памяти
class Cat2:
    def hello(*args):
        print("Hello world", args)

jim = Cat2()
jim.hello() # Hello world (<__main__.Cat2 object at 0x0000022EB10E5A10>,)
print(jim) # <__main__.Cat2 object at 0x0000022EB10E5A10>

# Обращение к атрибуту класса через вызов метода для экземпляра класса
class Cat3:
    breed = "pers"
    def hello(*args):
        print("Hello world", args)

    def show_breed(instance):
        print(f"my breed is {instance.breed}")

# Проверка, есть ли такой атрибут у класса
    def show_name(instance):
        if hasattr(instance, "name"):
            print(f"my name is {instance.name}")
        else:
            print("Nothing")

    def set_value(instance, value):
        instance.name = value

walt = Cat3()
walt.show_breed()
walt.breed = "siam"
walt.show_breed()
print(walt.__dict__)
bob2 = Cat3()
bob2.show_breed()

mary = Cat3()
# mary.show_name() # AttributeError: 'Cat3' object has no attribute 'name'
mary.name = "MARY"
mary.show_name()

tom = Cat3()
tom.show_name()
tom.set_value("Tom")
tom.show_name()