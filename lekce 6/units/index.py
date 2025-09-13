# def welcome(name):
#     # print(f"{name}, welcome to our team!")
#     return f"{name}, welcome to our team!"
    
# # result = welcome("Alex")
# # print(result)

# # print(welcome("Iryna"))
# welcome("Iryna")

# result = 0 # глобальная переменная

# def multiply(a, b):
#     res = a * b + result  # локальная переменная
#     return res

# result = multiply(5, 4)
# print(result)

# x = 5
# def change():
#     x = 10
#     return x
# x = 15
# print(change()) # 10
# print(x) # 5

# def power(a, b=2):
#     result = a ** b
#     return result
# print(power(3)) # 9
# print(power(3, 4)) # 81

# def add(a: int, b: int) -> int:
#     return a + b
# print(add(5, 7)) # 12 Success: no issues found in 1 source file
# print(add("Hi", " Alex")) # Hi Alex

# pip install mypy или python3 -m pip install mypy
# mypy --version или python3 -m mypy --version
# mypy nameFile.py или python3 -m mypy nameFile.py

# index.py:37: error: Argument 1 to "add" has incompatible type "str"; expected "int"  [arg-type]
# index.py:37: error: Argument 2 to "add" has incompatible type "str"; expected "int"  [arg-type]
# Found 2 errors in 1 file (checked 1 source file)

#  *args передаёт неопределённое количество аргументов
# def print_el(*args: int) ->int:
#     for arg in args:
#         print(arg)
# print_el(45, 15, 78, 1, 0, 45, 12)


# from typing import Any, List
# #  *args передаёт неопределённое количество аргументов
# def print_el(*args: Any) -> Any:
#     for arg in args:
#         print(arg)
# print_el(45, "Alex", None, 1, 0, True, 12)




# # **kwargs передаёт неопределённое количество именнованых аргументов в виде словаря
# def prin_dict(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
        
# prin_dict(name="Alex", age=25, isOnline=True)

# def mixArgs(arg1, *args, kwarg="default", **kwargs):
#     print(f"Это обезательный аргумент: {arg1}")
#     print(f"Это дополнительные аргументы (*args): {args}")
#     print(f"Это обезательный именованный аргумент: {kwarg}")
#     print(f"Это дополнительный именованный аргумент (**kwargs): {kwargs}")

# mixArgs("First", "Second", "Third", key1="value1", key2="value2")
# Это обезательный аргумент: First
# Это дополнительные аргументы (*args): ('Second', 'Third')
# Это обезательный именованный аргумент: default
# Это дополнительный именованный аргумент (**kwargs): {'key1': 'value1', 'key2': 'value2'}


# def orders(costumer: str, table: int, *items: str, drink: str="water", **extra) -> None:
#     print(f"Клиент: {costumer}, за столом номер: {table}")
#     print("Список блюд: ")
#     for item in items:
#         print(f'- {item}')
#     print(f"Напиток: {drink}")
    
#     if extra:
#         print("Дополнительно: ")
#         for key, value in extra.items():
#             print(f"- {key}:{value}")
            
# orders("Ivan", 5, "pizza", "cheess", drink="pivo", discount="ISIC", payment="Cash")
# Клиент: Ivan, за столом номер: 5
# Список блюд: 
# - pizza
# - cheess
# Напиток: pivo
# Дополнительно: 
# - discount:ISIC
# - payment:Cash


# def submits(rep: str, *messages: str, priority: str="Normal", **extras: dict) -> None:
#     print(f"Абонент: {rep}")
#     print(f"Приоритет: {priority}")
#     print("Сообщение: ")
#     for message in messages:
#         print(f" - {message}")
#     if extras:
#        print("Дополнительно: ")
#        for key, value in extras.items():
#             print(f"- {key}:{value}")
            
# submits("Yaroslav", "Давай срочно встретимся", priority="Urgent!", время="10.55", место="Ресторан У Калича")
# Абонент: Yaroslav
# Приоритет: Urgent!
# Сообщение:
#  - Давай срочно встретимся
# Дополнительно:
# - время:10.55
# - место:Ресторан У Калича



# def multiply(a: int, b:int) -> int:
# def multiply(*args: int) -> int:
#    result = args[0] * args[1]
#    return result

# tuple1 = (2, 5)
# list1 = [4, 5]

# print(multiply(*tuple1))
# print(multiply(*list1))

# def people_info(name: str, age: int) -> dict:
#     return (f"Имя: {name}, возраст: {age} лет")

# user = {
#         "name": "Igor",
#         "age": 25
#         }

# result_myFunc = people_info(**user)
# print(result_myFunc) # Имя: Igor, возраст: 25 лет

# def mix(*args, **kwargs):
#     for arg in args:
#         print(arg)
        
#     for key, value in kwargs.items():
#         print(key, value)
    
# user = {
#         "name": "Igor",
#         "age": 25
#         }

# list1 = [4, 5]

# print(mix(*list1, **user))


# map()
# numbers = [1, 4, 2, 8]
# def squera(x):
#     return x ** 2

# result = map(squera, numbers)
# print(list(result))

# filter()
# def isEven(x):
#     return x % 2 == 0

# numbers = [1, 4, 2, 8, 7, 9]
# eventList = filter(isEven, numbers)
# print(list(eventList)) # [4, 2, 8]

# boolList = map(isEven, numbers) 
# print(list(boolList))  # [False, True, True, True, False, False]

# square = lambda x: x ** 2
# print(square(5))  # Выведет 25

# square = lambda x: x ** 2
# numbers = [12, 14, 74, 1]
# print(list(map(square, numbers))) # [144, 196, 5476, 1]
