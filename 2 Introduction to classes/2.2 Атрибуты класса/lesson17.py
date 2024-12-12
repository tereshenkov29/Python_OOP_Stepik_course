# Ниже определен класс Book. Наша задача вывести на разных строках сначала значение атрибута
# класса writer, а затем — атрибута name

class Book:
    name = '1984'
    writer = 'Джордж Оруэлл'
    pages = 213

print(Book.writer)
print(Book.name)