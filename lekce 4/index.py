# a = None
# b = None 
# print(id(a), id(b))
# print(a is b) # True

# if a is b:
#     print("Ok")

# a = [1, 4, 78, "Ano"]
# print(all(a)) # True
# a = [0, 4, 78, "Ano"]
# print(all(a)) # False
# a = [1, None]
# print(all(a)) # False
# a = []
# print(all(a)) # True

# str1 = "hfgtgg"
# print(all(str1)) # True
# str1 = ""
# print(all(str1)) # True

# name = input("Задай своё имя")
# age = input("Задай свой аозраст")
# address = input("Задай свой адрес")
# input1 = [name, age, address]
# if all(input1):
#     print("All fields copled", name, age, address)
# else:
#     print("Some field does not copled", name, age, address)

# a = [1, 4, 78, "Ano"]
# print(any(a)) # True
# a = [0, ""]
# print(any(a)) # False
# a = []
# print(any(a))

# str1 = "hfgtgg"
# print(any(str1)) # True
# str1 = ""
# print(any(str1)) # False

# # user = "Oleg2022"
# user = "AlexPrag"
# users = ["AlexPrag", "Den21", "Irishka"]
# if any(u == user for u in users):
#     print("Такой пользователь ЕСТЬ!")
# else:
#     print("Такого пользователя НЕТ!")

# feedback = [1, 0, 0, 0, 0]
# if any(feedback):
#     print("Ура! Есть положтьельный отзыв")
# else:
#     print("К сожелению положтьельный отзывов нет!")

# sorted()
a = [11, 2, 55, 78]
# print(sorted(a)) # [2, 11, 55, 78]


list1 = ["Car", "metro", "HOME", "trAm"]
# print(sorted(list1, key=str)) # ['Car', 'HOME', 'metro', 'trAm']
# print(sorted(list1, key=str.lower)) # ['Car', 'HOME', 'metro', 'trAm']
# print(sorted(list1, key=len, reverse=True)) # ['metro', 'HOME', 'trAm', 'Car']

list2 = [14, -5, -7, 54]
# print(sorted(list2, key=abs)) # [-5, -7, 14, 54] сортировка по модулю числа

# print(sum(list2)) # 56
# print(sum(list2, start=100)) # 156
# # print(sum(list2, 2)) # 58
# print(list2[2] + list2[3])

str1 = "Hello"
# # print(sum(str1)) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(sorted(str1, key=abs)) # TypeError: bad operand type for abs(): 'str'

# print(max(list2))
# print(min(list1, key=len)) # Car
# print(max(list1)) # trAm
# print(max(str1)) # o

# str2 = "Гдеонииспользуются?-ихможноиспользоватьдляработысданнымииколлекциями;455785%&4"
# print(min(str2)) # " "
# print(max(str2)) # 
# # a = "U+1F970"  🥰
# print(chr(0x1F970)) # работа с unicode

#  создать список чичел от 0 до 9
# numbers_list = [num for num in range(10)]
# print(numbers_list) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# number_list = [x ** 2 for x in range(10)]
# print(number_list) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# numbers = [78, 13, 85, 101, 4, 1, 45]
# new_list = [pasha for pasha in numbers if pasha % 2 != 0]
# print(new_list) # [13, 85, 101, 1, 45]

# str1 = "Есть список слов, создать список который будет содержать первые буквы из каждого слова"
# # print(str1.split()) # ['Есть', 'список', 'слов,', 'создать', 'список', 'который', 'будет', 'содержать', 'первые', 'буквы', 'из', 'каждого', 'слова']
# new_list = [w for w in str1.split() if len(w) == 5] # ['слов,', 'будет', 'буквы', 'слова']
# print(new_list)

# # Используя any, выяснить есть ли в списке положительные числа
# a = [-1, 45, 74, 78, -4, 14]
# new_list = any([x > 0 for x in a])
# print(new_list) # True

# Робота с файлами
# file = open("text.txt", "r")
# if file:
#     print("File is open")
# else:
#     print("File does not open")
# file.close()
# if file:
#     print("File is close")
# else:
#     print("File does not close")

# import os
# print(os.path.exists("text.txt"))

# with open ("text.txt", "r", encoding="UTF-8") as file:
#     text = file.read()
# print(text)

# with open ("text.txt", "r", encoding="UTF-8") as file:
#     for line in file:
#         print(line)

# with open ("text.txt", "r", encoding="UTF-8") as file:
#     first_line = file.readline()
#     print(first_line)
#     # print("Это все строки: ", file.readlines())
#     print(file.readlines())
#     # text = file.read()
#     # print(text)

# with open ("text.txt", "r", encoding="UTF-8") as file:
#     text = file.read(50)
# print(text)

# with open ("text.txt", "w", encoding="UTF-8") as file:
#    file.write("This is new Text - Hello Python")

with open ("copy.txt", "a", encoding="UTF-8") as file:
   file.write("This is new Text - Hello Python")

# with open ("text.txt", "r", encoding="UTF-8") as file:
#    print(file.read())
