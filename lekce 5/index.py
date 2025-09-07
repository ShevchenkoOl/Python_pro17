# a = (1, "Ano", True, None)
# print(type(a)) # <class 'tuple'>
# print(a[1]) # Ano
# a[1] = "Hello" # TypeError: 'tuple' object does not support item assignment

# tuple1 = "1", "Ano", 7
# a, b, c = tuple1
# print(a) # 1

# a, b = tuple1 # ValueError: too many values to unpack (expected 2)

# a, b, *rest = tuple1
# # *start, c = tuple1
# print(a, b, rest) # 1 Ano [1]

# list1 = list(tuple1)
# list1[1] = "Ne"
# print(type(tuple(list1)), tuple(list1))

# print(tuple1[:2])  # ('1', 'Ano')
# print(tuple1.index(7)) # 2
# print(tuple1.count("Ano")) # 1
# print(len(tuple1)) # 3


dict1 = {"Vasilii": [1, 2, 1],
         "b": True,
         "c": 45,
         "d": "Hello"
         }

# print(dict1.get("k", "ничего не найдено")) # ничего не найдено
# print(dict1.keys()) # dict_keys(['Vasilii', 'b', 'c', 'd'])
# print(dict1.values()) # dict_values([[1, 2, 1], True, 45, 'Hello'])
# print(dict1.items()) # dict_items([('Vasilii', [1, 2, 1]), ('b', True), ('c', 45), ('d', 'Hello')])
# dict1.update({"isOnline": True})
# print(dict1) # {'Vasilii': [1, 2, 1], 'b': True, 'c': 45, 'd': 'Hello', 'isOnline': True}
# dict2 = {"car": "Audi"}
# dict1.update(dict2)
# print(dict1) # {'Vasilii': [1, 2, 1], 'b': True, 'c': 45, 'd': 'Hello', 'isOnline': True, 'car': 'Audi'}

dict1["d"] = "Ahoj"
# print(dict1)  # {'Vasilii': [1, 2, 1], 'b': True, 'c': 45, 'd': 'Ahoj'}
# print(dict1["d"]) # Ahoj
# del dict1['b']
# print(dict1) # {'Vasilii': [1, 2, 1], 'c': 45, 'd': 'Ahoj'}
# # del dict1 # удялякт весь словарь
# print(dict1)
# new_value = dict1.pop("c") # {'Vasilii': [1, 2, 1], 'b': True, 'd': 'Ahoj'}
# print(dict1)
# print(new_value) # 45

# for key in dict1:
#     print(key, dict1[key])
    
# for v in dict1.values():
#     print(v)

# for k, v in dict1.items():
#     print(k, v)


# dict()
# d = dict()
# d = dict([("name", "Alex"), ("age", 35)])
# print(type(d), d)
# d = dict(id=14, login="AlexStep")
# print(type(d), d)

# a = ["Alex", "Ivan", "Yarik", "Ilia"]
# b = [35, 25, 27, 18]
# d = dict(zip(a, b))
# print(type(d), d) # <class 'dict'> {'Alex': 35, 'Ivan': 25, 'Yarik': 27, 'Ilia': 18}

# str1 = "asdewr"
# str2 = "lkjnvg"
# print(list(zip(str1, str2))) # [('a', 'l'), ('s', 'k'), ('d', 'j'), ('e', 'n'), ('w', 'v'), ('r', 'g')]

# k = ("a", "b", "c")
# d = dict.fromkeys(k, "Hello")
# print(d)

# fruits = ["Bannan", "apple", "orange", "cherry", "kokos", "pure"]
# # fruits_dict = {key: value for key, value in enumerate(fruits)}
# # print(fruits_dict) # {0: 'Bannan', 1: 'apple', 2: 'orange', 3: 'cherry'}
# fruits_dict = {key: value for key, value in enumerate(fruits) if len(value) > 5} 
# print(fruits_dict) # {0: 'Bannan', 2: 'orange', 3: 'cherry'}

# set1 = {1, 2, 4, 1, 2, 4, 7, 8}
# print(set1) # {1, 2, 4, 7, 8}
s = set("hello3")
# print(s)

# s.add(4)       # {1, 2, 3, 4} -  Добавление элемента
# s.remove(2)    # {1, 3, 4} - Удаление элемента

# print(3 in s)  # False
# t = {"h", 1}
# print(s | t)   # {1, 'h', 'l', '3', 'o', 'e'} - Проверка обьедтинение элементов
# print(s & t)   # {2, 3} - Пересечение
# print(s - t)   # {1} - Разность
# print(s ^ t)   # {1, 4} - Симметрическая разность
# newSet = frozenset(s)
# print(type(newSet))
# 
# print(hash("jakjhdshkjhjk"))

# import getpass
# password = getpass.getpass("Enter your password: ")

# from getpass import *
# password = getpass("Enter your password: ")
# print(password) # jhsdhjksdfhjkdshjksdhkjdjh

# from datetime import datetime as dt
# print(dt.now()) # 2025-09-07 17:03:12.229066

# import turtle

# turtle.color('red')
# turtle.fillcolor('yellow')


# from turtle import *
# bgcolor("black")
# color('red')
# fillcolor('yellow')
# speed(10)
# pensize(3) 
# # begin_fill("green")
# circle(100)
# # end_fill()
# done()



# import turtle
# t = turtle.Turtle()
# turtle.bgcolor("black")  # цвет фона
# t.pencolor("yellow")     # цвет линии
# t.pensize(3)             # толщина линии
# # Рисуем что-нибудь
# for _ in range(3):
#     t.forward(100)
#     t.right(170)
# t.penup()
# t.goto(-100, 50)  # перемещение без рисования
# t.pendown()
# t.circle(50)  
# # Оставляем окно открытым
# turtle.done()


# # Перевернуть словарь (было {1:2, 3:4} стало {2:1, 4:3}). После этого сделать это же через компрешеншен
# d = {1:2, 3:4}
# # revers_V = {}

# # for k, v in d.items():
# #     # revers_V.update({v:k}) # {2: 1, 4: 3}
# #     revers_V[v] = k          # {2: 1, 4: 3}
# # print(revers_V)

# reversed_d = {value: key for key, value in d.items()}
# print(reversed_d) # {2: 1, 4: 3}
# # fruits_dict = {key: value for key, value in enumerate(fruits)}

#  Вывести второе по величене число
list1 = [45, 74, 12, 58, 1, 65]  # 65
# maxValue = max(list1)
# print(maxValue) # 74
# list1.remove(maxValue)
# secondMax = max(list1)
# print(secondMax)  # 65

# print(sorted(list1, reverse=True)[1])


# Есть два списка одинаковой длинны, создать словарь, где ключи из это элементы первого списка, а значения элементы второго. Например [1,2,3], [4,5,6], результат {1:4, 2:5, 3:6}
# list1 = [1,2,3]
# list2 = [4,5,6]

# dict()
# newDict = dict(zip(list1, list2))
# print(newDict) # {1: 4, 2: 5, 3: 6}

# dict comperehention
# newDict = {k: v for k, v in zip(list1, list2)}
# print(newDict) # {1: 4, 2: 5, 3: 6}


# Есть строка с предложением, в котором есть повторяющиеся слова. Создать словарь, где ключи это слова из этого предложения, а значение, это кол-во раз которое встречается это слово, пример: "привет я хочу привет я", результат {" привет": 2, "я": 2, "хочу": 1}
# str1 = "привет я хочу привет я"
# words = str1.split()
# newDict = {}

# for num in words:
#     newDict[num] = newDict.get(num, 0) + 1
# print(newDict)
