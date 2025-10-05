# # Арифметические операторы
# # __add__(self, other): для оператора +   addition
# # __sub__(self, other): для оператора -    subtraction
# # __mul__(self, other): для оператора *    multiplication
# # __truediv__(self, other): для оператора / true division
# # __floordiv__(self, other): для оператора // integer division
# # __mod__(self, other): для оператора % modulus (remainder)
# # __pow__(self, other): для оператора **  power (exponentiation)


# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
        
#     def __add__(self, other):
#         return self.score + other.score
    
#     def __sub__(self, other):
#         return self.score - other.score
#         # return abs(self.score - other.score) # по модулю
        
#     def __mul__(self, other):
#         return self.score * other.score
    
#     def __truediv__(self, other):
#         # return self.score / other.score
#         bigger = max(self.score, other.score)
#         smaller = min(self.score, other.score)
#         if smaller == 0:
#             return ('inf')
#         return bigger / smaller
    
#     def __floordiv__(self, other):
#         return self.score // other.score
    
#     def __mod__(self, other):
#         return self.score % other.score
    
#     def __pow__(self, other):
#         return self.score ** other.score
    
    
# s1 = Student("Alex", 15)
# s2 = Student("Maria", 5)

# print(s1 + s2)  # 40
# print(s1 - s2)  # -10
# print(s1 * s2)  # 375
# print(s2 / s1)  # 3.0
# print(s1 // s2) # 3
# print(s1 % s2) # 0
# print(s1 ** s2) # 759375

# # __radd__(self, other): для оператора + (правосторонний)
# # __rsub__(self, other): для оператора - (правосторонний)
# # __rmul__(self, other): для оператора * (правосторонний)`
# # __rtruediv__(self, other): для оператора / (правосторонний)
# # __rfloordiv__(self, other): для оператора // (правосторонний)
# # __rmod__(self, other): для оператора % (правосторонний)
# # __rpow__(self, other): для оператора ** (правосторонний)

# # _iadd__(self, other): in-place addition (сложение с присваиванием, +=)
# # __isub__(self, other): in-place subtraction (вычитание с присваиванием, -=)
# # __imul__(self, other): in-place multiplication (умножение с присваиванием, *=)
# # __itruediv__(self, other): in-place true division (деление с присваиванием, /=)
# # __ifloordiv__(self, other): in-place floor division (целочисленное деление с присваиванием, //=)
# # __imod__(self, other): in-place modulo (остаток от деления с присваиванием, %=)
# # __ipow__(self, other): in-place exponentiation (возведение в степень с присваиванием, **=)

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
        
#     def __iadd__(self, other):
#         self.score += other.score
#         return self.score
# s1 += s2
# print(s1) # 20

# # __eq__(self, other): для оператора ==
# # __ne__(self, other): для оператора !=
# # __lt__(self, other): для оператора <
# # __le__(self, other): для оператора <=
# # __gt__(self, other): для оператора >
# # __ge__(self, other): для оператора >=\

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
        
#     def __lt__(self, other):
#         return self.score < other.score
    
#     def __gt__(self, other):
#         return self.score > other.score
    
#     def  __le__(self, other):
#         return self.score <= other.score

# studen1 = Student("Nina", 15)
# studen2 = Student("Petro", 17)
# print(studen1 > studen2) # True
# print(studen1 <= studen2) # True

# Логические операторы (побитовые)
# __and__(self, other): для оператора &
# __or__(self, other): для оператора |
# __xor__(self, other): для оператора ^  - eXclusive OR
# __invert__(self): для оператора ~
# __rand__(self, other): для оператора & (правосторонний)
# __ror__(self, other): для оператора | (правосторонний)
# __rxor__(self, other): для оператора ^ (правосторонний)
# __iand__(self, other): для оператора &=
# __ior__(self, other): для оператора |=
# __ixor__(self, other): для оператора ^=

s = 5 # dec
print(bin(15)) # 0b   101
print(int("1101", 2))  # 5

# & наличие 1 у двух чисел, если у двох ксть 1 возвращает 1 иначе 0
# a = 5    # 0101
# b = 8    # 1000
# #          0000 
# print(a & b) # 0


READ = 1      # 001
WRITE = 2     # 010
UPDATE = 4    # 100
DELETE = 8    # 1000
Any = 15      # 1111
#             00001
user_code = 1 # 0101

flags = {"READ": READ, "WRITE": WRITE, "UPDATE": UPDATE, "DELETE": DELETE}
for key, flag in flags.items():
    if user_code & flag:
        print(f"{key} - разрешено")
    else:
        print(f"{key} - запрещено")

# n = 16
# print("Нечётное" if n & 1 else "Чётное")

# __or__(self, other): для оператора | если xотябы один = 1 то  1, если все нули - 0

# a = 5    # 0101
# b = 8    # 1000
# #          1101
# print(a | b) # 13
# user_code = WRITE | DELETE
# print(user_code) # 10

# __xor__(self, other): для оператора ^  - eXclusive OR если биты разные тогда 1, если одинаковые тогда 0
print(45 ^ 75) # 102
# 0101101
# 1001011
print(int("1100110", 2)) # 102

new_user_code = user_code ^ DELETE

flags = {"READ": READ, "WRITE": WRITE, "UPDATE": UPDATE, "DELETE": DELETE}
for key, flag in flags.items():
    if new_user_code & flag:
        print(f"{key} - разрешено")
    else:
        print(f"{key} - запрещено")
        
        
# __invert__(self): для оператора ~ 
print(~10) # -11
print(~-10) # 9

class MyFlags:
    def __init__(self, value):
        self.value = value
        
    def __and__(self, other):
        print("Вызываеться: AND")
        return self.value & other
    
    def __rand__(self, other):
        print("Вызываеться: right AND")
        return other & self.value
    
    def __or__(self, other):
        print("Вызываеться: OR")
        return self.value | other
    
    def __ror__(self, other):
        print("Вызываеться: right OR")
        return other | self.value
    
    def __xor__(self, other):
        print("Вызываеться: XOR")
        return self.value ^ other
    
    def __rxor__(self, other):
        print("Вызываеться: right XOR")
        return other ^ self.value
    
    def __invert__(self):
        return ~self.value
    
flag1 = MyFlags(0b1101)
# flag2 = MyFlags(0b100111)

print(flag1 & 0b100111)
print(0b100111 & flag1)
print(0b100111 | flag1)
print(flag1 ^ 0b100111)
print(0b100111 ^ flag1)
print(~flag1)


# __iand__(self, other): для оператора &=
# __ior__(self, other): для оператора |=
# __ixor__(self, other): для оператора ^=
# x = 5
# y = 7
# x &= y
# print(x) # 5

# class Student:
#     def __init__(self, name):
#         self.name = name
        
#     def __complex__(self):
#         return complex(self.name, self.name)
    
# n = Student(3)
# z = complex(n) # 3 +3j
# print(z.real)
# print(z.imag)

# x2 + 1 = 0
# x2 = -1
# x = ^-1 i 
# 𝑈(𝑡)=𝑈0*sin(𝜔𝑡 + 𝜑)

# 🔹 Ситуация из жизни: переменный ток (AC) в электрике
# В электрике, когда работаешь с переменным током, у каждого элемента цепи есть сопротивление (импеданс).
# Резистор имеет только действительную часть сопротивления (тепло).
# Конденсатор или катушка имеют мнимую часть (реактивное сопротивление).
# Если мы создадим класс Impedance (сопротивление элемента), то можем перегрузить __complex__, чтобы наш объект автоматически превращался в комплексное число, с которым можно считать токи и напряжения.

# class  Impedance:
#     def __init__(self, res=0, kon=0):
#         self.res = res
#         self.kon = kon
    
#     def __complex__(self):
#          return complex(self.res, self.kon)
    
#     def __str__(self):
#         return f"Impedance(R={self.res}, X={self.kon}"
    
# R = Impedance(10, 0)
# L = Impedance(0, 50)
# total = complex(R) + complex(L)

# print("Резистор: ", complex(R))
# print("Катушка: ", complex(L))
# print("Полное сопротивоение: ", total)


# Интератор

# class Counter:
#     def __init__(self, max):
#         self.max = max
#         self.corrent = 0
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.corrent == self.max:
#             raise StopIteration
#         self.corrent += 1
#         return self.corrent
    
# c = Counter(5)
# for n in c:
#     print(n)

# class Welcome:
#     def __init__(self, name):
#         self.name = name
    
#     def __call__(self, greating, znak):
#         return f"{greating}, {self.name}{znak}"
    
# g = Welcome("Alice")
# print(g("Hello", "!"))


# банк с кошельками пользователей, где можно складывать, вычитать деньги, сравнивать балансы, и даже использовать объекты как функцию для быстрого пополнения.

# class Wallet:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#     def __str__(self):
#         return f"Кошелёк {self.owner} с балансом {self.balance}"
    
# alice = Wallet("Alice", 500)
# honza = Wallet("Honza", 750)
# print(alice)
# print(honza)


# множественное наследование:

# class Auto:
#     def ride(self):
#         print("Авто ездит по дорогам")
        
# class Boat:
#     def swim(self):
#         print("Катер хoдит по воде")
        
# class Other(Auto, Boat):
#     pass

# a = Other()
# a.ride()
# a.swim()

# from abc import ABC, abstractmethod

# class Transport(ABC):
#     @abstractmethod
#     def move(self):
#         pass
    
# class Auto(Transport):
#     def move(self):
#         print("Авто ездит по дорогам")
        
#     def __hidden(self):
#         print("Скрытый тип")
        
#     def ride(self):
#         print("Водителя любят ездить на авто")
        
# class Boat(Transport):
#     def move(self):
#         print("Катер хoдит по воде")
    
#     def __hidden(self):
#         print("Скрытый тип")
    
#     def swim(self):
#         print("Все любят прогулки на катере")
        
# class Other(Auto, Boat):
#     pass

# a = Other()
# a.move() # Авто ездит по дорогам
# a.ride() # Водителя любят ездить на авто
# a.swim() # Все любят прогулки на катере



# MIXIN
# class Car:
#     def ride(self):
#         print("Авто ездит по дорогам")
        
#     def music(self, song):
#         print(f"Сейчас играет {song}")
        
# c = Car()
# c.music("Queen") # Сейчас играет Queen

# class MusicMixin:
#     def music(self, song):
#         print(f"Сейчас играет {song}")
        
# class Smartphone(MusicMixin):
#     pass

# class Radio(MusicMixin):
#     pass

# class Car(Smartphone, Radio, MusicMixin):
#     pass

# c = Car()
# c.music("Queen") # Сейчас играет Queen



# Ситуация из жизни: интернет-магазин
# У нас есть разные классы: User, Product, Order.
# Мы хотим, чтобы некоторые классы имели:
#      - логирование действий (Логирование — это процесс сохранения информации о работе программы в файл, консоль или другой источник, чтобы потом можно было понять, что произошло, отследить ошибки или поведение программы.),
#      - возможность сериализации (Сериализация — это процесс преобразования объекта в формат, который можно сохранить или передать, то есть нам нужно сохранения в JSON, словарь),
#      -   отметку времени создания.
import json
from datetime import datetime 

class SerialMixin:
    def to_dict(self):
        return self.__dict__
    
    def to_json(self):
        return json.dumps(self.to_dict(), default=str)
    
class TimeMixin:
    def __init__(self, *args, **kwargs):
        self.creat = datetime.now()
        super().__init__(*args, **kwargs)
        
class LogMixin:
    def log(self, message):
        print(f"[LOG] {datetime.now()} - {message}")

class User(SerialMixin, TimeMixin, LogMixin):
    def __init__(self, username, email):
        super().__init__()
        self.username = username
        self.email = email
        
class Product(SerialMixin, LogMixin):
    def __init__(self, name, price):
        super().__init__()
        self.name = name
        self.price = price

class Order(SerialMixin, TimeMixin):
    def __init__(self, user, product):
        super().__init__()
        self.user = user
        self.product = product
        
u1 = User("Alice", "example@gmail.com")
u1.log("Время регистрации: ")
print(u1.to_dict()) # {'creat': datetime.datetime(2025, 10, 5, 15, 58, 25, 606755), 'username': 'Alice', 'email': 'example@gmail.com'}

o1 = Product("Laptop", 1500)
o1.log("Товар добавлен") # [LOG] 2025-10-05 16:01:14.028824 - Товар добавлен
print(o1.to_json())  # {"name": "Laptop", "price": 1500}
print(o1.to_dict())  # {'name': 'Laptop', 'price': 1500}


order = Order(u1.username, o1.name)
print(order.to_json()) # {"creat": "2025-10-05 16:06:55.081043", "user": "Alice", "product": "Laptop"}