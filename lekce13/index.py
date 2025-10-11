# def sumNumber(a, b):
#     return a + b

# a = sumNumber

# print(a(5, 7))

# def num(*func):
#     return sumNumber(*func)

# print(num(7, 5))

# def simple_deration(func):
#     def wrapper():
#         print("Что-то происходит до вызова функции")
#         func()
#         print("Что-то происходит после вызова функции")
#     return wrapper

# @simple_deration
# def great():
#     print("Hello")
    
# great()

# def make_order(user):
#     if not user["isLogin"]:
#         print("Вы не зарегистрированы")
#         return
#     print("Заказ оформлен!")
    
# def make_pay(user):
#     if not user["isLogin"]:
#         print("Вы не зарегистрированы")
#         return
#     print("Заказ оплачен!")
    
    
    
# def check_log(func):
#     def wrapper(user, *arg, **kwargs):
#         if not user["isLogin"]:
#             print("Вы не зарегистрированы")
#             return
#         return func(user, *arg, **kwargs)
#     return wrapper
        
# @check_log
# def make_order(user):
#      print("Заказ оформлен!")
        
# @check_log
# def make_pay(user):
#     print("Заказ оплачен!")


    
# user1 = {
#         "name": "Alex", 
#         "isLogin": False
#         }


# make_order(user1)
# make_pay(user1)

# def isClient(func):
#     def wrapper(name):
#         if name == "Alex":
#             print(f"Пользователь {name} зарегистрирован")
#             return func(name)
#         print("Такой пользователь не найден!")
#     return wrapper

# @isClient
# def make_order(name):
#     print(f"Пользователь {name} сделал заказ")
    
# @isClient
# def make_pay(name):
#     print(f"Пользователь {name} успешно олатил заказ")
    
# make_order("Alex")

# def check_role(role):
#     def decoration(func):
#         def wrapper(user, *arg, **kwargs):
#             if user.get("role") != role:
#                 print("Доступ запрещён!")
#                 return
#             print("Доступ разрещён")
#             return func(user, *arg, **kwargs)
#         return wrapper
#     return decoration

# @check_role("admin")
# def delete(user):
#     print(f"Пользовктель {user["name"]} удалён")
    

# @check_role("user")
# def view_profil(user):
#     print(f"Просмотр профиля {user["name"]}")         
                
                

# user1 = {
#         "name": "Alex", 
#         "role": "admin"
#         }

# user2 = {
#         "name": "Denis", 
#         "role": "user"
#         }

# # # delete(user2) # Доступ запрещён!
# # # delete(user1) # Пользовктель Alex удалён
# view_profil(user1)

# Декораторы классов (staticmethod, classmethod, property)
# class A:
#     def great(self):
#         print("Hello")
        
# a = A()
# a.great()
# staticmethod

# class Example:
#     def usual_method(self):
#         print("Это обычный метод")
        
#     @staticmethod
#     def static_method():
#         print("Это какой-то статистический метод, self - не нужен")
        
# obj = Example()
# obj.static_method() # Это какой-то статистический метод, self - не нужен
# obj.usual_method()  # Это обычный метод

# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b
    
# print(Math.add(12, 25))


# classmethod self -> cls - сам класс, а не обьектом

# class Person:
#     population = 0
    
#     def __init__(self, name):
#         self.name = name
#         Person.population += 1
        
#     def great(self):
#         print(f'Привет, меня зовут: {self.name}')
        
#     @classmethod
#     def howMany(cls):
#         print(f"Создано {cls.population} людей")
        
# p1 = Person("Anna")
# p2 = Person("Tolja")
# p3 = Person("Denis")

# p1.great() # Привет, меня зовут: Anna
# Person.howMany() # Создано 3 людей




# # property
# class Rectangle:
#     def __init__(self, w, h):
#         self.width = w
#         self.heigth = h
        
#     @property
#     def area(self):
#         return self.width * self.heigth
    
# a = Rectangle(3, 4)
# print(a.area)




# Задача
# Создадим класс BankAccount, который будет имитировать банковский счёт.
# Требования:
# 1. Каждый объект хранит balance (остаток) и owner (имя владельца).
# 2. Должен быть метод для снятия денег, который проверяет минимальный баланс через декоратор с аргументом.
# 3. Нужно иметь класс-метод, который возвращает количество всех созданных аккаунтов.
# 4. Статический метод, который проверяет корректность суммы (например, > 0) без доступа к объекту.
# 5. Свойство (@property), которое возвращает информацию о владельце и балансе, и сеттер, который запрещает устанавливать отрицательный баланс.

def check_balance(min_balance):
    def decaration(func):
        def wrapper(self, amount):
            if self.balance - amount < min_balance:
                print(f"Баланс после выдачи не может быть меньше: {min_balance}")
                return
            return func(self, amount)
        return wrapper
    return decaration

class BankAccount:
    create_owner = 0
    
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
        BankAccount.create_owner += 1
        
    @check_balance(50)
    def withdraw(self, amount):
        self._balance -= amount
        print(f"Сумма в {amount} крон снята, ваш баланс {self._balance}")
        
    @classmethod
    def total_accounts(cls):
        return cls.create_owner
    
    @staticmethod
    def isValid(amount):
        return amount > 0
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Баданс не может быть отрицательным")
        self._balance = value
        
    @property
    def info(self):
        return f"Владелец: {self.owner}, баланс: {self._balance} крон"
    
    
a1 = BankAccount("Alice", 100)
a2 = BankAccount("Alice", 350)
a3 = BankAccount("Alice", 400)
        
# print(BankAccount.total_accounts()) # 3
# print(BankAccount.isValid(10)) # True
# a1.withdraw(60) # Баланс после выдачи не может быть меньше: 50
print(a2.balance) # 350
print(a1.info) # Владелец: Alice, баланс: 100 крон