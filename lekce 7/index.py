# python -m mypy --version
# python -m mypy imjaFaila.py

# Факториал числа. Напишите функцию factorial, которая принимает целое число и возвращает его факториал.
# 5! = 1 * 2 * 3 * 4 * 5

# def factorial(n: int) -> int:
#     if n == 0:
#         return 1
#     else:
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#     return result
# print(factorial(5)) #120

# def factorial(n: int) -> int:
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)
# print(factorial(5)) # 120

# # 5 , 4, 3, 2, 1
# # 120

# "hello" -> "olleh"
# def reverse_str(a: str) -> str:
#     if len(a) <= 1:
#         return a
#     return reverse_str(a[1:]) + a[0]

# print(reverse_str("hello"))
# # reverse_str("ello") + "h"
# # reverse_str("llo") + "e"
# # reverse_str("lo") + "l"
# # reverse_str("o") + "l"
# # reverse_str("o") -> o

# # Фибоначчи
# # 0, 1, 1, 2, 3, 5, 8, 13, 21
# def fibonacci(n: int) -> int:
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(8)) # 21


# Задача 1 — Учет заказов в интернет-магазине
# 1. получите список всех сумм заказов.
# 2. Напишите функцию, которая считает общую сумму заказов по каждому клиенту
# и возвращает словарь вида {имя_клиента: сумма_его_заказов}.
# 3. Напишите функцию для добавления нового заказа в существующий словарь заказов.

from typing import Dict, Tuple, List
import json

Order = Tuple[int, str, int]

# orders: Dict[str, Order] = {
#     "1": (1, "Maria", 1500),
#     "2": (2, "Alice", 700),
#     "3": (3, "Olga", 2200),
#     "4": (4, "Patrik", 3700),
#     "5": (5, "Honza", 1100),
#     "6": (6, "Maria", 1800),
#     "7": (7, "Patrik", 32000),
# }
with open("data.json", "r", encoding="utf-8") as f:
    orders: Dict[str, Order] = json.load(f)

def list_sum(orders: Dict[str, Order]) -> List[float]:
    # price = lambda v: v[2]
    # return list(map(price, orders.values()))
    price = [el[2] for _, el in orders.items()]
    total_sum = sum(price)
    return price, total_sum

def add_order(orders: Dict[str, Order], newOrder: Order)->Dict:
    orders[newOrder[0]] = newOrder
    
    with open("data.json", "w", encoding="utf-8") as f:
         json.dump({k: list(v) for k, v in orders.items()}, f, ensure_ascii=False)


print(f"Список потраченных денег{list_sum(orders)}")
newOrder = (8, "Pasha", 1700)
add_order(orders, newOrder)