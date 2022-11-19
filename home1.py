

# Задание 1
# Создайте аналог телефонной книги. 
# Каждая запись в книге должна 
# иметь идентификационный номер, имя, фамилия, дату рождения, профессию.
# Напишите для этого класса метод get_information которая будет 
# выдавать информацию об экземпляре этого класса.

# Пример входных данных:

# >>>from datetime import date >>> >>>c = Contact(id=1,   
#     first_name='John',       last_name='Dow',   
#     birth_date=date(day=21, month=4, year=1996),   
#     profession='Python developer')

# Пример выходных данных:

# >>>c.get_information()

# ID - 1
# Full name - John Dow
# Birth Date - 21.04.1996
# Profession - Python developer

from datetime import date

class Contact:

    def __init__(self, id, full_name, birth_date, profession):
        self.id = id
        self.full_name = full_name
        self.birth_date = birth_date
        self.profession = profession

    def get_information(self):
        return f'ID - {self.id}\nFull name - {self.full_name}\nBirth Date - {self.birth_date}\nProfession - {self.profession}'

    
c = Contact(1, "John Dow", date(1996,4,21),"Python developer")  
      
print(c.get_information())




