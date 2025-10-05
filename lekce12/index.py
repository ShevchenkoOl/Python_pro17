# Стандартные библиотеки
# sys
# import sys
# print(sys.argv) # ['d:/step/Python_pro17/lekce12/index.py']

# # sys.exit()
# print(sys.version_info) # 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)]
# # print(sys.path)    # 'C:\\Users\\uzlab\\AppData\\Local\\Programs\\Python\\Python312', 'C:\\Users\\uzlab\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages']
# print(sys.executable) # C:\Users\uzlab\AppData\Local\Programs\Python\Python312\python.exe

# ver = sys.version_info
# if  sys.version < ("3.11"):
#     print("Обновите пайтон") # Обновите пайтон
# else:
#     print("OK")

# with open("log.txt", "w") as f:
#     sys.stdout = f
#     print("Записано в log.txt")

# name = sys.argv[1]
# print(f"Hello, {name}")


# os
# import os
# print(os.getcwd()) # D:\step\Python_pro17\lekce12
# os.chdir("Python_pro17")
# print(os.getcwd())
# print(os.listdir('.'))

# math
# import math
# print(math.pi) # 3.141592653589793
# print(math.floor(math.pi))
# print(math.ceil(math.pi))
# print(math.pow(5, 2))
# r = 5
# s = math.pi * math.pow(r, 2)
# print(round(6.5)) # до ближайщего чётного числа



# # random
# from random import *
# # a = random.randint(2, 8)
# # print(a)
# list1 = ["red", "yellow", "green", "black"]
# # print(random.choice(list1))
# # shuffle(list1)
# # print(list1)

# collections

# from collections import *

# text = "jalskkjlkljlkjas"
# print(Counter(text)) # Counter({'j': 4, 'l': 4, 'k': 4, 'a': 2, 's': 2})
# text = "кот кот собака кот рыба собака"
# print(Counter(text.split())) # Counter({'кот': 3, 'собака': 2, 'рыба': 1})


# datetime
# from datetime import date, datetime, timedelta

# # print(datetime.now()) # 2025-10-05 17:16:28.895621
# # formatedDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# # print(formatedDate)

# date_str = "2025-10-05"
# parsedDate = datetime.strptime(date_str, "%Y-%m-%d")
# print(parsedDate)




# 🧠 Задача: система прав доступа (Access Control System)
# Ты разрабатываешь мини-систему, которая управляет правами пользователей в приложении.
# Каждый пользователь может иметь разные права:
#      -чтение,
#      -запись,
#      -удаление,
#      -администрирование.
# Для эффективности система хранит права в виде битовой маски (побитовые флаги).
# Тебе нужно реализовать классы с множественным наследованием и миксинами, которые управляют этими правами.
# ⚙️ Условия:
# 1. Создай класс Permissions, который хранит права в виде целого числа (int), где каждый бит — это одно право:
# 1 << 0 → READ
# 1 << 1 → WRITE
# 1 << 2 → DELETE
# 1 << 3 → ADMIN
# 2. Создай миксин LoggerMixin, который при каждом изменении прав (добавление/удаление) выводит сообщение:
# [LOG] Добавлено право: WRITE
# [LOG] Удалено право: DELETE
# 3. Создай класс User, который хранит имя пользователя и объект Permissions.
# 4. Создай класс AdminUser, который наследуется от User и LoggerMixin.
# При создании AdminUser автоматически выдай все права (READ|WRITE|DELETE|ADMIN).

class Permissions:
    # READ = 0b0001
    # WRITE = 0b0010
    # DELETE = 0b0100
    # ADMIN = 0b1000
    READ = 1 << 0
    WRITE = 1 << 1
    DELETE = 1 << 2
    ADMIN =  1 << 3
    
    NAMES = {
        READ: "READ",
        WRITE: "WRITE",
        DELETE: "DELETE",
        ADMIN:  "ADMIN"
    }
    
    def __init__(self):
        self.flags = 0
        
    def add(self, permission):
        self.flags |= permission
        
    def remove(self, permission):
        self.flags &= ~permission
    
    def has(self, permission):
        return self.flags & permission
    
    def __str__(self):
        active = [name for perm, name in self.NAMES.items()  if self.has(perm)]
        return ", ".join(active) if active else "Нет права!"
    

class LoggerMixin:
    def log(self, message):
        print(f"[LOG] - {message}")
        
class User:
    def __init__(self, name):
        self.name = name
        self.permissions = Permissions()
        
class AdminUser(User, LoggerMixin):
    def __init__(self, name):
        super().__init__(name)
        
        self.permissions.add(Permissions.READ | Permissions.WRITE | Permissions.DELETE | Permissions.ADMIN)
        
    def remove(self, permission):
        self.log(f"Удалено право: {Permissions.NAMES[permission]}")
        self.permissions.remove(permission)
        
    def add(self, permission):
        self.log(f"Добавлено право: {Permissions.NAMES[permission]}")
        self.permissions.add(permission)
        
        
u = User("Alex")
u.permissions.add(Permissions.READ)
u.permissions.add(Permissions.WRITE)
u.permissions.add(Permissions.ADMIN)
print(u.permissions.has(Permissions.ADMIN))
print(bin(8))



# 🧠 Задача: система учёта заказов с миксинами и проверкой статусов
# Ты создаёшь систему, которая управляет заказами в интернет-магазине.
# Каждый заказ имеет:
#   - уникальный ID,
#   - дату создания,
#   - список товаров,
#   - текущий статус (новый, оплачен, отправлен, доставлен).
# Есть базовый класс Order, несколько миксинов для поведения и наследники для разных типов заказов.
# ⚙️ Условия:
# 1️⃣. Создай класс Order:
    #    - Имеет поля:
    #    - order_id — случайное число (используй random.randint).
#        - created_at — текущая дата/время (datetime.now()).
#        - items — список товаров (строки).
#        - status — "new" по умолчанию.
# Методы:
# __str__() → выводит строку вида: Заказ #1234 от 2025-10-04 (статус: new)
# 2️⃣. Создай абстрактный класс StatusMixin (через abc.ABC):
# Определяет обязательные методы:
#        - update_status(new_status)
#        - get_status()
# 3️⃣. Создай миксин LoggerMixin:
# При каждом изменении статуса выводит лог:
# [LOG] Статус изменён: new → paid
# 4️⃣. Создай класс OrderWithLogging, который наследуется от Order, LoggerMixin, StatusMixin:
# Реализуй методы:
#    - update_status(new_status) — обновляет статус и вызывает логирование.
#    - get_status() — возвращает текущий статус.
# 5️⃣. Создай класс OrderStats, который хранит все заказы и умеет считать статистику с помощью collections.Counter:
# Метод add_order(order)
# Метод status_summary() — возвращает количество заказов по статусам.
# # 📁 Структура проекта:
# # project/
# # │
# # ├── main.py
# # ├── orders.py
# # ├── utils.py
# # └── files.py