# class Dog:
#     def bark(self):
#         print("Гав, гав!")
        
# my_dog = Dog()
# my_dog.bark()

# class Dog:
#     def __init__(self, family: str, name: str, age: int)-> None:
#         self.type_of_dog = family
#         self.name_of_dog = name
#         self.age_of_dog = age
        
#     def bark(self):
#         print(f"Собака породы: {self.type_of_dog}, по кличке: {self.name_of_dog}, возраст {self.age_of_dog} лет, говорит - Гав, гав!")
 
# dog1 = Dog("Пидбуль", "Шарик", 2)
# dog2 = Dog("Пикинес", "Вампир", 7)
# dog3 = Dog("Пудель", "Артемон", 3)

# dog1.bark()

# Задача 1: Класс Book
# Условие:
#  Класс Book должен хранить:
#        1. название книги (атрибут экземпляра)
#        2. автора (атрибут экземпляра)
#        3. количество страниц (атрибут экземпляра)
#    - Атрибут класса: жанр книг (например, "Фантастика")
#  Методы:
#      1. info() — выводит информацию о книге
#      2. is_long() — возвращает True, если страниц больше 300

# class Book:
#     gener: str = "Фантастика"  # Атрибут класса
   
#     def __init__(self, title: str, author: str, pages: int, gener=gener)-> None: # атрибут экземпляра
#         self.books_name = title
#         self.author_of_book = author
#         self.number_of_pages = pages
#         self.gener = gener
        
#     def info(self)-> str:
#         return f"Книга с названием {self.books_name}, написана автором {self.author_of_book}, имеет {self.number_of_pages} страниц, жанр {self.gener}"
    
#     def isLong(self) -> bool:
#         # if self.number_of_pages > 300:
#         #     return True
#         return self.number_of_pages > 300
    
# book1 = Book("451 градус по Фарингейту", "Рей Бредбери", 451)
# book2 = Book("Babička", "Božená Nemcová", 150, gener="Anti")
# # book3 = Book("Python для чайников", "Erik Metis", 298)
# # book4 = Book("Мальчик в полосатой пижаме", "One Momemt", 301)

# print(book1.info())
# print(book2.info())
# print(book2.isLong())

# # books = [book1, book2, book3, book4]

# # for book in books:
# #     print(book.info())
# #     print(book.isLong())


# Задача 2: Класс Student
# Условие:
#       Класс Student должен хранить:
#          1. имя студента (атрибут экземпляра)
#          2. возраст (атрибут экземпляра)
#          3. список оценок (атрибут экземпляра)
#       Атрибут класса: школа (например, "Step IT Academy")
#       Методы:
#          1. average_score() — возвращает среднюю оценку
#          2. add_score(score) — добавляет новую оценку

# class Student:
#     school: str = "Step IT Academy"
    
#     def __init__(self, name: str, age: int, raitig_list: list, school: str | None = None) -> None:
#         self.name = name
#         self.age = age
#         self.raitings = raitig_list
#         if school:
#            self.school = school
        
#     def average_score(self) -> float:
#         return round(sum(self.raitings) / len(self.raitings), 2)
    
#     def add_score(self, score) -> list:
#         self.raitings.append(score)
#         return self.raitings
        
# student1 = Student("Denys", 18, [1, 1, 2, 1, 2, 2], school="VSE")
# print(student1.average_score())
# print(student1.add_score(3))
# print(student1.average_score())
# print(student1.school)



# Принципы ООП
# Наследование
# class Student:
#     school: str = "Step IT Academy"
    
#     def __init__(self, name: str, age: int, raitig_list: list, school: str | None = None) -> None:
#         self.name = name
#         self.age = age
#         self.raitings = raitig_list
#         if school:
#            self.school = school
        
#     def average_score(self) -> float:
#         return round(sum(self.raitings) / len(self.raitings), 2)
    
#     def add_score(self, score) -> list:
#         self.raitings.append(score)
#         return self.raitings


# class SchoolarshipStudent(Student):   
#     def __init__(self, name, age, raitig_list, salary: float, school: str | None = None) -> None:
#         super().__init__(name, age, raitig_list, school)
#         self.salary = salary
    
#     def info(self) -> str:
#         return f"Студент {self.name}, получает стипендиюв размере {self.salary} kč"
    
    
# student1 = SchoolarshipStudent("Honza", 21, [5, 1, 1, 2, 4, 3, 1, 1], 1500)
# print(student1.info())
# print(student1.average_score())


#  Полиморфизм
# class Student:
#     school: str = "Step IT Academy"
    
#     def __init__(self, name: str, age: int, raitig_list: list, school: str | None = None) -> None:
#         self.name = name
#         self.age = age
#         self.raitings = raitig_list
#         if school:
#            self.school = school
    
#     def info(self) -> str:
#         return f"Студент {self.name}, возраст {self.age} лет, с оценками {self.raitings}, ходит в {self.school}"
    
#     def average_score(self) -> float:
#         return round(sum(self.raitings) / len(self.raitings), 2)
    
#     def add_score(self, score) -> list:
#         self.raitings.append(score)
#         return self.raitings


# class SchoolarshipStudent(Student):   
#     def __init__(self, name, age, raitig_list, salary: float, school: str | None = None) -> None:
#         super().__init__(name, age, raitig_list, school)
#         self.salary = salary
    
#     def info(self) -> str:
#         return f"Студент {self.name}, получает стипендиюв размере {self.salary} kč"
    

# student1 = SchoolarshipStudent("Honza", 21, [5, 1, 1, 2, 4, 3, 1, 1], 1500)
# student2 = Student("Мария", 18, [1, 1, 1, 2, 2, 3, 1], school="VSE")

# students = [student1, student2]
# for s in students:
#     print(s.info())
#     print(s.average_score())



# Инкапсуляция
#  _name - защищённый атрибут
#  __name - приватный атрибут

# публичный
# class Student:
#     def __init__(self, name):
#         self.name = name
        
# student1 = Student("Alex")
# print(student1.name) # Alex
# student1.name = "Anna"
# print(student1.name) # Anna

# защищённый атрибут
# class Student:
#     def __init__(self, name):
#         self._name = name
        
# student1 = Student("Мария")
# print(student1._name) # Мария
# student1._name = "Иван"
# print(student1._name) # Иван


# приватный атрибут
# class Student:
#     def __init__(self, name):
#         self.__name = name
        
        
# student1 = Student("Мария")
# # print(student1._Student__name)
# student1.__name = "Иван"
# print(student1.__name) # Иван


# class Student:
#     def __init__(self, name):
#         self.__name = name
    
#     def get_name(self):
#         return self.__name
    
#     def set_name(self, new_name):
#         if isinstance(new_name, str) and new_name.strip():
#             self.__name = new_name
#         else:
#             print(f"Not correct name")
        
    
        
# student1 = Student("Мария")
# Первый способ обхода приватности через название класса
# print(student1.__name) # AttributeError: 'Student' object has no attribute '__name'
# print(student1._Student__name) # Мария
# print(student1.__dict__)
# student1.__name = "Honza"
# student1._Student__name = "Alex"
# print(student1._Student__name) # Alex
# print(student1.__dict__)

# Второй способ обхода приватности через методы get и set
# print(student1.get_name()) # Мария
# student1.set_name("Светлана")
# print(student1.get_name()) # Светлана

#  Третий способ обхода приватности через @proprety
# @property
# <имя пропрети> - геттер
# <имя пропрети>.setter - для изменения setter
# <имя пропрети>.delattr - контроль удаления

# class Student:
#     def __init__(self, name):
#         self.__name = name


#     @property
#     def getName(self):
#         return self.__name
    
#     @getName.setter
#     def getName(self, new_name: str) -> None:
#         if isinstance(new_name, str) and new_name.strip():
#             self.__name = new_name
#         else:
#             print(f"Not correct name")
            
#     @getName.deleter
#     def getName(self):
#         print("Warning!")
    
# student1 = Student("Мария")
# print(student1.getName)   # Мария
# student1.getName = "Lenka"
# print(student1.getName)   # Lenka
# del student1.getName




#Четвёртый способ обхода приватности через
# Магические классы
# __getattribute__ Вызывается при любом доступе к атрибуту
# __getattr__      Вызывается только если атрибут НЕ найден обычным способом. Удобен для обработки «неизвестных» атрибутов или подстановки значений по умолчанию.
# __setattr__      Вызывается при каждой попытке присваивании значения к атрибуту
# __delattr__      Вызывается при удалении атрибута

# class Student:
#     def __init__(self, name):
#         self.__name = name

#     def __getattribute__(self, name_attr):
#         if name_attr == "__name":
#             raise ArithmeticError("Прямой допуск к имени запрещён!")
#         return object.__getattribute__(self, name_attr)
    
#     def __getattr__(self, name_attr):
#         return f"Имя атрибута {name_attr} не найдено"
    
#     def __setattr__(self, name_attr, value):
#         object.__setattr__(self, name_attr, value)
        
#     def __delattr__(self, name_attr):
#         print(f"Недьзя удалять {name_attr}")
#         return f"Недьзя удалять {name_attr}"
  
    
# student1 = Student("Мария")
# print(object.__getattribute__(student1, "_Student__name")) # Мария
# print(student1._Student__name) # Мария
# print(student1._Student__ower) # Имя атрибута _Student__ower не найдено
# student1.__setattr__("Age", 25)
# print(student1.__dict__)  # {'_Student__name': 'Мария', 'Age': 25}
# del student1._Student__name



# Условие задачи: Зоопарк
# Ты разрабатываешь систему учёта животных в зоопарке.

# Требования:
# Инкапсуляция
# 1. У каждого животного есть имя и возраст.
# 2. Возраст должен храниться в приватном атрибуте, чтобы нельзя было напрямую менять его на некорректное значение.
# 3. Сделай методы get_age() и set_age(value), где при установке проверяется: возраст не может быть отрицательным.

# Наследование
# 1. Создай базовый класс Animal.
# 2. От него унаследуй классы Lion, Elephant и Monkey.
# 3. Каждый подкласс может иметь свои дополнительные свойства (например, у слона — длина бивней, у обезьяны — любимый фрукт).

# Полиморфизм
# Сделай метод make_sound(), который у каждого животного работает по-своему:
# 1. Лев рычит: "Р-р-р!"
# 2. Слон трубит: "Тру-у-у!"
# 3. Обезьяна кричит: "У-у-а-а!"

# Если у тебя есть список разных животных, можно пройтись по ним циклом и вызвать у каждого make_sound() — результат будет разным.

# from abc import ABC, abstractmethod

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
        
#     def info(self):
#         return f"Животное по кличке {self.name}, {self.__age} лет"
    
#     def get_age(self):
#         return self.__age
    
#     def set_age(self, new_age):
#         if new_age < 0:
#             return "Возраст животного не может быть отрицательным!"
#         else:
#             self.__age = new_age
    
#     @abstractmethod      
#     def make_sound(self):
#         pass
            
            
# class Lion(Animal):
#     def __init__(self, name, age, height):
#         super().__init__(name, age)
#         self.height = height
        
#     def info(self):
#         return f"Животное по кличке {self.name}, {self.get_age()} лет, высотой {self.height} cm"
    
#     def make_sound(self):
#         return "Р-р-р!"

    

# class Elephant(Animal):
#     def __init__(self, name, age, tooth_size):
#         super().__init__(name, age)
#         self.tooth_size = tooth_size
        
#     def info(self):
#         return f"Животное по кличке {self.name}, {self.get_age()} лет, розмер бивней {self.tooth_size} cm"
    
#     def make_sound(self):
#         return "Тру-у-у!"
    
    
# class Monkey(Animal):
#     def __init__(self, name, age, tail):
#         super().__init__(name, age)
#         self.tail = tail
        
#     def info(self):
#         return f"Животное по кличке {self.name}, {self.get_age()} лет, длина хвоста {self.tail} cm"
    
#     def make_sound(self):
#         return "У-у-а-а!"
    
    
    
# animal1 = Lion("Murka", 7, 150)
# animal2 = Elephant("Emma", 3, 25)
# animal3 = Monkey("Edik", 7, 32)
# animal4 = Animal("Barbos", 5)


# animals = [animal1, animal2, animal3, animal4]
# # for a in animals:
# #     if hasattr(a, "make_sound"):
# #        print(a.info(), a.make_sound())
# #     else:
# #         print(a.info())
# for a in animals:
#     print(a.info(), a.make_sound())    

    


# __str__
# __repr__

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
    
#     # def __repr__(self):
#     #     return f"{self.__class__}: {self.title}, {self.author}"
    
#     def __str__(self):
#         return f"{self.__class__}: {self.title}, {self.author}"
    
    
# book1 = Book("Harry Potter", "Jose Wilsson")
# book1
# print(book)     # <class '__main__.Book'>: Harry Potter Jose Wilsson
# book      

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
        
#     def __add__(self, other):
#         return self.score + other.score

# studen1 = Student("Nina", 15)
# studen2 = Student("Petro", 13)
# print(studen1 + studen2) # 28

# st = [studen2, studen1]
# # print(sum(st)) TypeError: unsupported operand type(s) for +: 'int' and 'Student'


# __eq__, __lt__, __gt__

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
        
#     # def __lt__(self, other):
#     #     return self.score < other.score
    
#     def __gt__(self, other):
#         return self.score > other.score

# studen1 = Student("Nina", 15)
# studen2 = Student("Petro", 13)
# print(studen1 > studen2)




# Опишите класс для шахматной фигуры.
# Фигура должна содержать такие атрибуты:
# 1. Цвет (белый или черный).
# 2. Место на доске (тут есть варианты, или два отдельных поля, для описания координат или одно, но, например, кортеж из двух чисел).
    #   И такие методы как:
        # -  Изменить цвет (ничего не принимает, только меняет цвет на противоположный).
        # -  Изменить место на доске (принимает или две переменные, или один кортеж из двух элементов), не забудьте проверить, что мы не пытаемся поставить фигуру за пределы доски (оба значения от 0 до 7).
        # - Абстрактный метод проверки потенциального хода. На данном этапе фигуры могут стоять на одной и той же клетке, пока нам это не важно.
    
# 3. Опишите классы для пешки, коня, офицера, ладьи, ферзя и короля. Все, что в них нужно добавить - это один метод для проверки, возможно, ли за один ход поменять место фигуры на доске (все ходят по-разному, у пешек будет еще и разница от цвета). Метод принимает опять же или две цифры, или один кортеж. И опять же проверяем, не выходит ли значение за пределы доски (Так как нам необходим этом функционал дважды, я бы делал его как отдельный защищенный метод в родительском классе)
# 4. И функцию, которая принимает список фигур и потенциальную новую клетку, а возвращает список из фигур. Но только тех, которые могут за один ход добраться до этой клетки.