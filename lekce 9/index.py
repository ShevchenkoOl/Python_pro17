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
#         if isinstance(new_name) and new_name.strip():
#             self.__name = new_name
#         else:
#             print(f"Not correct name")
        
    
        
# student1 = Student("Мария")
# print(student1.get_name()) # Мария
# student1.set_name("Светлана")
# print(student1.get_name())
