# Давайте теперь добавим в класс Book два новых атрибута:
#
# атрибут rating с числовым значением 8.7;
# атрибут genre со строковым значением «dystopian»;
# Создайте один атрибут обязательно через функцию setattr, второй через присвоение.
#
# Остальные атрибуты удалять или изменять не нужно. Ничего выводить на экран также не требуется

class Book:
    name = '1984'
    writer = 'Джордж Оруэлл'
    pages = 213

setattr(Book, "rating", 8.7)
Book.genre = "dystopian"