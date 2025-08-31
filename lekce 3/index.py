# Простой пример деление на ноль
# 1/0
# За обработку исключений в python отвечают ключевые слова try/except.
# try:
#     1 / 0
# except ZeroDivisionError:
#     print("You cannot divide by zero!")
# Или полеая версия обработки оштибки:
# try:
#     # код, который может вызвать ошибку
# except SomeError:
#     # код при ошибке
# else:
#     # код, который выполнится, если ошибки не было
# finally:
#     # код, который выполнится в любом случае


# except – обязательный, если используете try, иначе Python выдаст синтаксическую ошибку.

# else – полностью необязательный. Он нужен только если вы хотите выполнить что-то только при успешном выполнении try, без ошибок.

# finally – тоже необязательный. Используется, когда нужно гарантировать выполнение кода в любом случае, например закрыть файл или соединение.

# В блоке try должен выполняться код в котором мы ожидаем какое-либо исключение. И если исключение происходит, то код перестает выполняться, и переходит к блоку/блокам except, и пытается понять произошло ли то исключение, которое описано в блоке except

# Блоков except может быть любое количество, так же в одном блоке except может быть больше одного исключения, если вам для разных ошибок нужны одинаковые действия, такие исключения должны быть указаны в скобках и через запятую. Рассмотрим такой пример:

# bottles_of_beer = 10
# try:
#     amount_of_people = int(input("Please input amount of people:"))
#     bottle_per_person = bottles_of_beer / amount_of_people
#     print(bottle_per_person)
# except (ValueError, ZeroDivisionError):
#     print('Incorrect amount of people!')

# В этом случае когда мы введем не число, или введем 0, программа продолжит работу, потому что мы обработали исключение и описали что код должен сделать

# Или вот такой:

# bottles_of_beer = 10
# try:
#     amount_of_people = int(input("Please input amount of people:"))
#     bottle_per_person = bottles_of_beer / amount_of_people
#     print(bottle_per_person)
# except ValueError:
#     print('Your input is not a number')
# except ZeroDivisionError:
#     print('You are trying divide to zero')

# если мы укажим другую ошибку:
# try:
#     bottles_of_beer = 10
#     amount_of_people = int(input("Please input amount of people:"))
#     bottle_per_person = bottles_of_beer / bottles_of_beer
#     print(bottle_per_person)
# # except SyntaxError:
# #     print('Your input is not a number') # ValueError: invalid literal for int() with base 10: 'аааа'
# except:
#     print("У вас ошибка") # но это не правильно! На жаргоне Python это известно как "голое исключение"
    

# Оператор finally очень прост в использовании. Давайте взглянем на нижеизложенный пример:

try:
    value = int("ABC")
except ValueError:
    print("ValueError произошлa!")
finally:
    print("Наконец-то оператор выполнен!")
# Что произойдет? Часть finally выполниться вообще всегда, хоть попали в исключение хоть нет.


# Оператор else
# Оператор try/except также имеет блок else. Он работает только в том случае, если в вашем коде нет ни единой ошибки. Давайте потратим немного времени и взглянем на парочку примеров:

# try:
#     value = int(input("Please enter value"))
# except ValueError:
#     print("A ValueError occurred!")
# else:
#     print("No error occurred!")
# В этом примере, если мы введем число, то исключения не случится, и это именно тот случай когда мы попадем в else.

# Вся конструкция целиком try-except-else-finally:
# Целиком вся конструкция состоит из 4 блоков

# try:
#     value = int(input("Please enter value"))
# except ValueError:
#     print("A ValueError occurred!")
# else:
#     print("No error occurred!")
# finally:
#     print("The finally statement ran!")


# Оператор raise
# Если в вашем коде какие-либо данные не соответствуют вашим ожиданиям, вы всегда можете вызвать исключение, если вам это необходимо, для этого используется ключевое слово raise.
# odds = 15
# if odds % 2 != 1:
#     raise ValueError("Не получил нечетное число")


# try:
#     # Блок, который может вызвать ошибки
#     login = input("Введите логин: ")
#     if not login:
#         raise ValueError("Логин не может быть пустым")

#     password = input("Введите пароль: ")
#     if not password:
#         raise ValueError("Пароль не может быть пустым")

# except ValueError as e:
#     # Обработка ошибок
#     print("Ошибка:", e)

# else:
#     # Выполняется, если в try не было ошибок
#     if login == "admin" and password == "1234":
#         print("Доступ разрешен")
#     else:
#         print("Неверный логин или пароль")

# finally:
#     # Выполняется всегда
#     print("Проверка завершена")
