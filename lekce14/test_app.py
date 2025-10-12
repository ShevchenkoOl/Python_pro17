# import unittest

# class TestSum(unittest.TestCase):
#     def test_sum(self):
#         self.assertEqual(sum([1, 2, 3]), 6)
        
#     def test_sum_tuple(self):
#         self.assertEqual(sum((2, 2, 3)), 7, "Должно быть 6")
        
        
# if __name__ == '__main__':
#     unittest.main()
    
# .assertEqual(a, b)  Проверяет, что a == b и можно использовать для проверки результатов арифметики, строк, списков и т.д. 
#     a = [1,2,3]
#     b = a
#     c = [1,2,3]

#     self.assertEqual(a, c)  # True, значения списков одинаковы

# .assertTrue(x)  # bool(x) is True - возвращает True
# .assertFalse(x)  # bool(x) is False - возвращает False
# .assertIs(a, b)  # a is b - логичский оператор is Проверяет (т.е. оба объекта — один и тот же объект в памяти
        # self.assertIs(a, b)     # True, это один объект
        # self.assertIs(a, c)     # False, разные объекты в памяти

# .assertIsNone(x)  # x is None - проверка на None
# .assertIn(a, b)  # a in b - логичский оператор in Например: assertIn(3, [1,2,3])
# .assertIsInstance(a, b)  # isinstance(a, b) a является экземпляром класса b 
#             self.assertIsInstance(5, int)  # True
#             self.assertIsInstance("hi", str)  # True

# import unittest
# from main import mul, powNum, roundNum

# class TestMathFunc(unittest.TestCase):
#     def test_mul(self):
#         self.assertEqual(mul(4, 0), 0, "Должно быть 0")
#         self.assertEqual(mul(-1, 5), -5, "Должно быть -5")
#         self.assertEqual(mul(-2, -6), 12, "Должно быть 12")
#         self.assertEqual(mul(45.5, 2), 91, "Должно быть 91")
        
#     def test_pow(self):
#         self.assertEqual(powNum(-2, 3), -8, "Должно быть 8")
#         self.assertEqual(powNum(-2, 2), 4, "Должно быть 4")
#         self.assertEqual(powNum(5, 2), 25, "Должно быть 25")
        
#     def test_round(self):
#         self.assertEqual(roundNum(2.5), 2, "Должно быть 2")
#         self.assertEqual(roundNum(3.5), 4, "Должно быть 4")
        
        
        
# if __name__ == "__main__":
#     unittest.main()
    


# Mock имитация в Python
# from unittest.mock import Mock

# fake_api = Mock()
# fake_api.get_user.return_value = {"name": "Alex", "age": 25}
# print(fake_api.get_user(1))   # {'name': 'Alex', 'age': 25}


# Patch подменяет обьект или функцию
# from main import get_weather
# from unittest.mock import patch
# import unittest


# class TestMathFunc(unittest.TestCase):
#     def test_wether(self):
#         with patch("main.get_weather") as mock_weather:
#             mock_weather.return_value = "Солнечно"
#             result = mock_weather()
#             assert result == "Солнечно"
        
# if __name__ == "__main__":
#     unittest.main()
    
# pip install pytest
from main import add_task, remove_task, complete_task

def test_add_task():
    assert add_task([], "Купить хлеб") == ["Купить хлеб"]
    assert add_task(["Купить хлеб"], "Продать хлеб") == ["Купить хлеб","Продать хлеб"]
    
def test_remove():
    assert remove_task(["Купить хлеб"], "Купить хлеб") == []
    assert remove_task(["Купить хлеб", "Продать хлеб"], "Продать хлеб") == ["Купить хлеб"]
    
def test_complete():
    assert complete_task(["Купить хлеб", "Продать хлеб"], "Купить хлеб") == [ "X Купить хлеб",  "Продать хлеб"]