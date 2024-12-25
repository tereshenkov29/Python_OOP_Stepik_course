# Добавление магического метода __init__
class Cat:
    # breed = "pers"

    # def set_value(self, value, age=0):
    #     self.name = value
    #     self.age = age

    def __init__(self, name, breed = "pers", age = 1, color = "white"):
        print("Hello new object is", self, name, breed, age, color)
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

cat = Cat("Tom", "siam", 40, "black")
walt = Cat("Walt")
kelly = Cat("Kelly", age = 40)