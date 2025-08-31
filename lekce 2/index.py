# # a = 5
# # b = 5
# # print(not 0)

# # a = "Hello"
# # b = "h"
# # print(b in a)

# # is
# # a = 500
# # b = 500
# # # b = a    # True
# # print(a is b)

# # a = 300
# # b = 300
# # # print(a is b)  # False

# # error_massege = 400

# # # match error_massege:
# # #     case 400:
# # #         print("Vad request")
# # #     case 401:
# # #         print("Unaothorized")
# # #     case 402:
# # #         print("Not fopund")


# # # value = 5
# # value = input("Что-то введите: ")
# # match value:
# #     case str():
# #         print("Это строка")
# #     case int():
# #         print("Это целое число")

# # point = (3, 0)

# # match point:
# #     case (0, 0):
# #         print("Ты в начальнрй точки координат")
# #     case (x, 0):
# #         print("Ты двигаешся по горизонтальной оси")
# #     case (0, y):
# #         print("Ты двигаешся по вертикальной оси")
# #     case (x, y):
# #         print(f"твои кадинаты по оси Х: {x}, а по оси y: {y}")

# # num = 22

# # match num:
# #     case a if a % 2 == 0:
# #         print(f"Твоё число {num} - чётное")
# #     case n if n % 2 != 0:
# #         print(f"Твоё число {num} - нечётное")


# # str1 = "Hello"
# # print(str1, id(str1))
# # str1 = "Ahoj"
# # # str1[2] = "G"
# # # print(str1)

# # print(str1, id(str1))

# # a = 15.5
# # print(a, id(a))

# # a = 15.5
# # print(a, id(a))

# fruits = ["orange", "apple", "bannan", "pineapple"]
# print(fruits[2])
# # print(id(fruits))
# fruits.append("potatoes")
# print(fruits)

# # del fruits[2]
# # print(fruits)

# # fruits.clear()
# # print(fruits)
# # print(id(fruits))
# fruits2 = fruits.copy()
# # print(id(fruits2))

# # # fruits2 = fruits
# # fruits2.append("Car")
# # # print(id(fruits2))
# # print(fruits, id(fruits))
# # print(fruits2, id(fruits2))

# list_num = [45, 14, 45, 52, 1, 45]
# # print(list_num.count(45))
# # print(fruits.count("bannan"))

# # fruits.extend(list_num)
# # print(fruits)

# # print(fruits.index(45))

# # fruits.insert(2, 5.5)
# # print(fruits)

# # print(fruits.pop())
# # print(fruits)

# fruits.remove("pineapple")
# # fruits.remove("pipple") # ValueError:
# print(fruits)

# fruits.reverse()
# print(fruits)

# fruits.sort(reverse=True)
# print(fruits)

# print(len(fruits))

string = "Hello, World! Hello, people"
# print(len(string))
# print(string[1])

# print(string.upper())
# print(string.lower())

# text = "    \nHello! Ahoj! Привет\n       "
# print(repr(text))
# newText = text.strip()

# print(newText, repr(newText))

# newList = string.split(", ")
# print(newList)

# print(string.replace("World", "people"))
# print(string.find("g")) # -1
# # print(string.index("g")) # ValueError

# print(string.count("g"))

# print(string.startswith("He"))
# print(string.endswith("g"))

# # newList = ", ".join(fruits)
# # print(newList, type(newList))

# name = "Alex"
# age = 35

# print("Hello, {}! You are {} years old!".format(name, age))
# print(f"Hello, {name}! You are {age} years old!")


# print(fruits[-1])
# print(string[-1])
# print(string[2:-1])
# print(string[2:])
# print(string[:2])
# print(string[::2])
# newText = string[:]
# print(newText)
# print(id(string))
# print(id(newText))

# fruits = ["orange", "apple", "bannan", "pineapple"]

# for el in fruits:
#     print(el)
    
    
list1 = [45, 14, 47, 78, 45, 45]
# newLIst = []
# for el in list1:
#     if el == 45:
#         newLIst.append(index(el))
#         # print(f"Число 45 в списке занимает позицию {list1.index(el)}")
# print(newLIst)

# for el in range(len(list1)):
#     if list1[el] == 45:
#         print(f"Число 45 в списке занимает позицию {el}")

# a = 500
# b = 500
# print(a is b) # True

# list1  = list(range(0, 10, 2)) # start, stop, step
# list1  = list(range(0, 10))    # start, stop
# list1  = list(range(8))        # stop
# print(list1)

# a = range(45, 85)
# print(a[-1])    # 84

# enumerate(text, start=5)

# text = "Hello Academy Step!"

# for i in enumerate(text, start=7):
#     print(i)


# for i, num in enumerate(list1):
#     if num == 45:
#         print(f"Число 45 в списке занимает позицию {i}")

# while

# count = 1
# while count > 0:
#     if count == 10:
#         break
#     print(count)
#     count += 1

# import getpass    
# password = ''
# while password != "password":
#     # password = input("Введите пожалуйста пароль, или для выхода введите exit ")
#     password = getpass.getpass("Введите пожалуйста пароль, или для выхода введите exit ")
#     if password == "exit":
#         print("Цыкл остановлен")
#         break


text = "Hello Academy Step!"
# list1 = ["aa", "sd", ]
# for char in text:
#     if char == "d":
#         break
#     print(char)

for char in text:
    if char == "de":
        continue
    print(char)