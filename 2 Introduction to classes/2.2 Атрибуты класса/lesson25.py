# В вашем распоряжении класс Person, у которого имеется 7 атрибутов:
#
# class Person:
#     name = "John Smith"
#     age = 30
#     gender = "male"
#     address = "123 Main St"
#     phone_number = "555-555-5555"
#     email = "johnsmith@example.com"
#     is_employed = True
# Программа будет принимать на вход произвольное количество слов в одну строку, разделенных пробелом.
# Ваша задача проверить, является ли каждое из введенных слов названием атрибута. Регистр слов значения не имеет.
#
# Нужно вывести в каждой отдельной строке введенные слова по порядку и напротив через дефис указать, нашлось свойство
# с таким именем или нет (вывести YES или NO)

from lesson24 import is_obj_has_attr

class Person:
    name = "John Smith"
    age = 30
    gender = "male"
    address = "123 Main St"
    phone_number = "555-555-5555"
    email = "johnsmith@example.com"
    is_employed = True

list_with_words = list(input().split())

for word in list_with_words:
    if is_obj_has_attr(Person, word.lower()):
        print(word + "-YES")
    else:
        print(word + "-NO")

