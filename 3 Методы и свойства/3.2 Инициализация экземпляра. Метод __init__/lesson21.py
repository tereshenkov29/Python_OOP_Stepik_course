# Создайте класс Zebra, внутри которого есть метод which_stripe , который поочередно печатает фразы «Полоска белая»,
# «Полоска черная» без кавычек, начиная именно с фразы «Полоска белая».
#
# Также реализуйте метод run_away, который печатает фразу «Oh, Sugar Honey Ice Tea».
#
# Ваша задача написать только определение класса Zebra

class Zebra:
    def __init__(self):
        self.stripe = 0

    def which_stripe(self):
        if self.stripe == 0:
            print("Полоска белая")
            self.stripe = 1
        else:
            print("Полоска черная")
            self.stripe = 0

    def run_away(self):
        print("Oh, Sugar Honey Ice Tea")